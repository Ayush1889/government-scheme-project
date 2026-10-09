from discovery_agent import discovery_agent


query = "I am a farmer with low income. Which government schemes can I apply for?"


results = discovery_agent(query)


print("===================================")
print("       DISCOVERY AGENT")
print("===================================")

if not results:

    print("\nNo relevant schemes found.")

else:

    print(f"\nFound {len(results)} relevant schemes:\n")

    for result in results:

        scheme = result["scheme"]

        print("-----------------------------------")

        print("Scheme:")
        print(scheme["scheme_name"])

        print("\nRelevance Score:")
        print(round(result["score"], 3))