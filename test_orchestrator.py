from orchestrator import run_assistant


user_profile = {
    "age": 24,
    "income": 200000,
    "state": "Karnataka",
    "occupation": "farmer",
    "gender": "male",
    "category": "general"
}

user_query = """
I am a farmer with low income.
Which government schemes can I apply for?
"""


run_assistant(
    user_query,
    user_profile
)