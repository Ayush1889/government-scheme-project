import os
import json
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

# Create Gemini client
client = genai.Client(api_key=api_key)


def extract_user_profile(user_query):

    prompt = f"""
You are a profile extraction system for a Government Scheme Assistant.

Extract ONLY information explicitly provided by the user.

User query:
{user_query}

Return ONLY valid JSON using exactly these fields:

{{
    "age": null,
    "income": null,
    "state": null,
    "occupation": null,
    "gender": null,
    "category": null
}}

Rules:

1. Do not guess missing information.
2. If information is not provided, use null.
3. Age must be a number.
4. Income must be a yearly amount in INR.
5. Convert expressions like "2 lakh" to 200000.
6. Keep state as a string.
7. Keep occupation as a string.
8. Keep gender as a string.
9. Keep category as a string.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown code fences if Gemini returns them
    if text.startswith("```"):
        text = text.replace("```json", "")
        text.replace("```", "")
        text = text.strip()

    return json.loads(text)