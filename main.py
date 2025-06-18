import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
if user_prompt == None:
    print("Error: No argument given")
    sys.exit(1)

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)
if len(sys.argv) > 2:
    if sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}\n")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)