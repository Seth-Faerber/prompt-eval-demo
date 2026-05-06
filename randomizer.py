"""
Randomly select an action and theme from the TTRPG random tables.
"""

import random

from tables import action_table, theme_table


def get_random_combination():
    """Return a (action, theme) tuple chosen at random from the tables."""
    action = random.choice(action_table)
    theme = random.choice(theme_table)
    return (action, theme)
