"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    no_duplicates = dict.fromkeys(items)
    frequencies = {}
    for i in no_duplicates:
        frequencies[str(i)] = str(items.count(i))
    return frequencies
