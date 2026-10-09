from rag import search_schemes


print("===================================")
print("   GOVERNMENT SCHEME ASSISTANT")
print("===================================")


while True:

    query = input("\nWhat are you looking for? ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    results = search_schemes(query)

    if not results:

        print("\nNo relevant schemes found.")
        continue

    print("\nRelevant schemes:\n")

    for result in results:

        scheme = result["scheme"]

        print("-----------------------------------")

        print("Scheme:")
        print(scheme.get("scheme_name", "N/A"))

        print("\nWhy it may be relevant:")
        print(scheme.get("description", "N/A"))

        print("\nTarget Group:")
        print(scheme.get("target_group", "N/A"))

        print("\nEligibility:")
        print(scheme.get("eligibility", "N/A"))

        print("\nBenefits:")
        print(scheme.get("benefits", "N/A"))

        print("\nDocuments Required:")
        print(scheme.get("documents_required", "N/A"))

        print("\nApplication Process:")
        print(scheme.get("application_process", "N/A"))

        print("\nOfficial Source:")
        print(scheme.get("source_url", "N/A"))