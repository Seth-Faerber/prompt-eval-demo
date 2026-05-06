"""
Prompt Eval Demo — A simple CLI for testing prompts with Claude.

Run with: python main.py
Type your prompt, get Claude's response. Type 'quit' or 'exit' to stop.
"""

# 'import' is like 'using' in C# or 'require' in Ruby.
# We pull in specific things from libraries we installed.
import os                          # Built-in: access environment variables
from dotenv import load_dotenv     # Reads .env file into environment variables
from anthropic import Anthropic    # The Claude SDK client
from trigger import is_trigger
from randomizer import get_random_combination
from interpreter import interpret_combination


def main():
    """Entry point for the app. This function runs the interactive loop."""

    # Load variables from the .env file so os.environ can see them.
    # Similar to how Rails loads config/credentials.
    load_dotenv()

    # Read the API key from the environment.
    # os.environ.get() returns None if the key isn't set, instead of crashing.
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key or api_key == "your-key-here":
        print("ERROR: Set your real API key in the .env file.")
        print("  Open .env and replace 'your-key-here' with your Anthropic API key.")
        return  # Exit the function early (like 'return' in C#/Ruby)

    # Create the API client. This is like instantiating a service class.
    # In C# terms:  var client = new Anthropic(apiKey);
    client = Anthropic(api_key=api_key)

    # Pick which Claude model to use.
    model = "claude-haiku-4-5-20251001"

    print("=== Prompt Eval Demo ===")
    print(f"Model: {model}")          # f-strings are Python's string interpolation (like $"..." in C#)
    print("Type a prompt and press Enter. Type 'quit' or 'exit' to stop.\n")

    # This is an infinite loop — it keeps running until we 'break' out of it.
    while True:
        # input() prints the prompt text, waits for the user to type, and returns what they typed.
        user_input = input("You: ")

        # .strip() removes leading/trailing whitespace (like .Trim() in C#).
        # .lower() converts to lowercase for comparison.
        if user_input.strip().lower() in ("quit", "exit"):
            print("Goodbye!")
            break  # Exit the while loop

        # Skip empty inputs
        if not user_input.strip():
            continue  # Jump back to the top of the while loop

        # Check if the user wants a random TTRPG combo.
        if is_trigger(user_input):
            try:
                combo = get_random_combination()
                print(f"\n🎲 Rolled: Action = {combo[0]}, Theme = {combo[1]}")
                interpretation = interpret_combination(combo)
                print(f"\nClaude: {interpretation}\n")
            except Exception as e:
                print(f"\nERROR: {e}\n")
            continue

        # Send the request to Claude.
        # 'messages' is a list of dicts — each dict has a 'role' and 'content'.
        # This is similar to how chat APIs work everywhere.
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": user_input}
                ],
            )

            # The response contains a list of content blocks.
            # For a simple text response, we grab the first block's text.
            assistant_text = response.content[0].text

            print(f"\nClaude: {assistant_text}\n")

        # 'except' is Python's version of catch (try/catch in C#, rescue in Ruby).
        except Exception as e:
            print(f"\nERROR: {e}\n")


# This is a Python convention. It means: "only run main() if this file
# is executed directly (not imported as a module by another file)."
# Similar to: static void Main() in C#.
if __name__ == "__main__":
    main()
