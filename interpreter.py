"""
Send a random (action, theme) combination to Claude and return its interpretation.
"""

import os

from dotenv import load_dotenv
from anthropic import Anthropic


def interpret_combination(combination):
    """Send the (action, theme) tuple to Claude and return the interpretation.

    Args:
        combination: A tuple of (action, theme) strings.

    Returns:
        A string containing the AI's interpretation of the combination.
    """
    load_dotenv()

    action, theme = combination

    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (
                    f"You are a TTRPG game master. Interpret this random combination "
                    f"for a tabletop RPG scenario.\n\n"
                    f"Action: {action}\n"
                    f"Theme: {theme}\n\n"
                    f"Provide a brief, evocative scenario description that a game master "
                    f"could use. Keep it genre-neutral and under 100 words."
                ),
            }
        ],
    )

    return response.content[0].text
