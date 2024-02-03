#!/usr/bin/python3
"""Define a function for text indentation."""


def text_indentation(text):
    """Indent text by adding two new lines after each '.', '?', or ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters to split the text on
    split_chars = ['.', '?', ':']

    # Initialize an empty line
    current_line = ""

    # Iterate through each character in the input text
    for char in text:
        # Add the character to the current line
        current_line += char

        # Print the current line with two new lines
        if char in split_chars:
            print(current_line.strip())
            print()
            current_line = ""

    # Print the remaining text if any
    print(current_line.strip(), end='')
