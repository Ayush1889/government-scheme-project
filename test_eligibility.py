from eligibility import check_eligibility


# Example user
user_profile = {
    "age": 24,
    "income": 200000,
    "state": "Karnataka",
    "occupation": "farmer"
}


# Example scheme
scheme = {
    "scheme_name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",

    "target_group":
        "Eligible landholding farmer families",

    "eligibility":
        "Eligible landholding farmer families identified by "
        "State/UT authorities, subject to exclusion criteria; "
        "eKYC is mandatory for registered farmers."
}


result = check_eligibility(
    scheme,
    user_profile
)


print("===================================")
print("       ELIGIBILITY RESULT")
print("===================================")

print("\nScheme:")
print(scheme["scheme_name"])

print("\nStatus:")
print(result["status"])

print("\nReasons:")

for reason in result["reasons"]:
    print("-", reason)

print("\nInformation to verify:")

for warning in result["warnings"]:
    print("-", warning)