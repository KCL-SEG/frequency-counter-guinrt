"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import pytest

def frequencies(items):
    no_duplicates = dict.fromkeys(items)
    frequencies = {}
    for i in no_duplicates:
        frequencies[str(i)] = items.count(i)
    return frequencies
