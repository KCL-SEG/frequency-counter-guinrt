"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    # new list with all elements in items list as strings
    string_list = []
    for i in items:
        string_list.append(str(i))
    # making a dictionary from our items list removes all duplicates because
    # there cannot be duplicate keys in a dictionary
    no_duplicates = dict.fromkeys(string_list)
    # here we initialize an empty dictionary
    frequencies = {}
    # here, for every unique key in the dictionary no_duplicates, we add it as a
    # key in our frequencies dictionary, and the count of it in the items list
    # as the value pair (using the count() method)
    #str() method converts an int to a string
    for i in no_duplicates:
        frequencies[str(i)] = string_list.count(str(i))
    return frequencies
