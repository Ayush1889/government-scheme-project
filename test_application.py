from application_agent import application_agent


scheme = {
    "scheme_name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",

    "documents_required":
        "Identity/Aadhaar details, bank details and "
        "land/farmer records as required.",

    "application_process":
        "Use New Farmer Registration on the PM-KISAN "
        "portal and complete verification/eKYC.",

    "application_url":
        "https://pmkisan.gov.in/",

    "source_url":
        "https://www.pmkisan.gov.in/"
}


result = application_agent(scheme)


print("===================================")
print("       APPLICATION AGENT")
print("===================================")

print("\nScheme:")
print(result["scheme_name"])

print("\nDocuments Required:")
print(result["documents"])

print("\nHow to Apply:")
print(result["steps"])

print("\nOfficial Application Website:")
print(result["official_website"])

print("\nOfficial Source:")
print(result["source"])