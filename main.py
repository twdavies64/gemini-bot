import env_setup  # isort: skip # Ensure env_setup is imported before any other imports

import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def get_client():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "No Gemini API key found in environment. Please set the GEMINI_API_KEY environment variable."
        )
    return genai.Client(api_key=api_key)


def get_prompt():    
    parser = argparse.ArgumentParser(description="Gemini AI Bot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()

def print_verbose(prompt, usage_metadata):
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
    print(f"Response tokens: {usage_metadata.candidates_token_count}")

def main():
    client = get_client()
    args = get_prompt()

    prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )
    if not response.usage_metadata:
        raise RuntimeError("No usage metadata returned from Gemini API")
    if args.verbose:
        print_verbose(prompt, response.usage_metadata)
    print(f"Response:")
    print(response.text)


if __name__ == "__main__":
    main()
