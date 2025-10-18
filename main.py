# import os
# import sys
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types
# load_dotenv()
# api_key = os.environ.get("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)


# messages = [
#     types.Content(role="user", parts=[types.Part(text=user_prompt)]),
# ]

# response = client.models.generate_content(
#     model="gemini-2.0-flash-001",
#     contents=messages,
# )

# if sys.argv[2] == "--verbose":
#     print( f"User prompt: ")
#     print( f"Response tokens: {response.usage_metadata.candidates_token_count}")
#     print( f"Prompt tokens: {response.usage_metadata.prompt_token_count}")

# import os
# import sys
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types
# load_dotenv()
# api_key = os.environ.get("GEMINI_API_KEY")

# if not api_key:
#     print("Error: GEMINI_API_KEY not found")
#     sys.exit(1)
# client = genai.Client(api_key=api_key)

# verbose = False
# prompt_parts = []

# for arg in sys.argv[1:]:
#     if arg == "--verbose":
#         verbose = True
#     else:
#         prompt_parts.append(arg)
# user_prompt = " ".join(prompt_parts).strip()
# if not user_prompt:
#     print("Error in User")
#     sys.exit(1)
# messages = [
#     types.Content(role="user", parts=[types.Part(text=user_prompt)]),
# ]

# response = client.models.generate_content(
#     model="gemini-2.0-flash-001",
#     contents=messages,
# )
# if len(sys.argv) > 2 and sys.argv[2] == 

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Get user prompt from command line
# if len(sys.argv) < 2:
#     print("Please provide a prompt as argument")
#     sys.exit(1)

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

# print(response.text)

if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    # print("\n" + "="*50)
    print(f"User prompt: {user_prompt}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")