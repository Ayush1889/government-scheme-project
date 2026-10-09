from llm import extract_user_profile


user_query = """
I am 24 years old.
I am a farmer from Karnataka.
My annual income is 2 lakh.
"""


profile = extract_user_profile(user_query)

print("\nExtracted User Profile:")
print(profile)