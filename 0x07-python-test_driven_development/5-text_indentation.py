#!/usr/bin/python3
"""Define a function for text indentation."""


def text_indentation(text):
    """Indent text by adding two new lines after each '.', '?', or ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    without_dot = text.replace('. ', '.\n\n')
    without_question = without_dot.replace('? ', '?\n\n')
    without_colon = without_question.replace(': ', ':\n\n')
    print(without_colon)
