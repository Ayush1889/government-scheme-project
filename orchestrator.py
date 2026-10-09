from discovery_agent import discovery_agent
from eligibility import check_eligibility
from application_agent import application_agent


def run_assistant(user_query, user_profile):

    # --------------------------------
    # 1. DISCOVERY AGENT
    # --------------------------------

    print("\n===================================")
    print("       DISCOVERY AGENT")
    print("===================================")

    results = discovery_agent(
        user_query,
        top_k=3
    )

    if not results:
        print("\nNo relevant schemes found.")
        return

    print(f"\nFound {len(results)} candidate schemes.")

    suitable_schemes = []
    rejected_schemes = []

    # --------------------------------
    # 2. ELIGIBILITY AGENT
    # --------------------------------

    for result in results:

        scheme = result["scheme"]
        relevance_score = result["score"]
        print("Scheme:")
        print(scheme["scheme_name"])
        print("\nRelevance Score:")
        print(round(relevance_score,3))

        eligibility_result = check_eligibility(
            scheme,
            user_profile
        )

        if eligibility_result["status"] == "Not Eligible":

            rejected_schemes.append({
                "scheme": scheme,
                "eligibility": eligibility_result
            })

        else:

            suitable_schemes.append({
                "scheme": scheme,
                "eligibility": eligibility_result
            })

    # --------------------------------
    # 3. SHOW SUITABLE SCHEMES
    # --------------------------------

    print("\n===================================")
    print("       SUITABLE SCHEMES")
    print("===================================")

    if not suitable_schemes:

        print("\nNo schemes passed the initial eligibility check.")

    else:

        for item in suitable_schemes:

            scheme = item["scheme"]
            eligibility_result = item["eligibility"]

            print("\n-----------------------------------")

            print("Scheme:")
            print(scheme["scheme_name"])

            print("\nEligibility Status:")
            print(eligibility_result["status"])

            print("\nReasons:")

            for reason in eligibility_result["reasons"]:
                print("✓", reason)

            if eligibility_result["information_needed"]:

                print("\nInformation to verify:")

                for information in eligibility_result["information_needed"]:
                    print("⚠", information)

            # --------------------------------
            # 4. APPLICATION AGENT
            # --------------------------------

            application_result = application_agent(
                scheme
            )

            print("\nDocuments Required:")
            print(application_result["documents"])

            print("\nHow to Apply:")
            print(application_result["steps"])

            print("\nOfficial Application Website:")
            print(application_result["official_website"])

    # --------------------------------
    # 5. SHOW REJECTED SCHEMES
    # --------------------------------

    if rejected_schemes:

        print("\n===================================")
        print("       FILTERED OUT")
        print("===================================")

        for item in rejected_schemes:

            scheme = item["scheme"]
            eligibility_result = item["eligibility"]

            print("\n-----------------------------------")

            print("Scheme:")
            print(scheme["scheme_name"])

            print("\nStatus:")
            print("Not Eligible")

            print("\nReason:")

            for reason in eligibility_result["reasons"]:

                if "does not match" in reason.lower():
                    print("✗", reason)