"""
Detect whether user input is requesting a random TTRPG combination.
"""

# Keywords that suggest the user wants a random combo.
# A match requires at least one word from ACTION_WORDS *and* one from SUBJECT_WORDS.
ACTION_WORDS = {"roll", "generate", "give", "create", "make", "get", "need"}
SUBJECT_WORDS = {"random", "combo", "combination", "scenario", "table", "tables"}


def is_trigger(user_input):
    """Return True if the input looks like a request for a random TTRPG combination."""
    words = set(user_input.lower().split())
    has_action = bool(words & ACTION_WORDS)
    has_subject = bool(words & SUBJECT_WORDS)
    return has_action and has_subject
