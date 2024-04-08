#!/usr/bin/python3
""" A module for text indentations """


def text_indentation(text):
    """
    Prints each sentence in the given text on a new line.

    Args:
        text (str): The text containing one or more sentences.
     """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = ''

    for ch in text:
        if ch in ('.', '?', ':'):
            print(sentence.strip() + ch)
            print()
            sentence = ''
        else:
            sentence += ch

    print(sentence.strip(), end="")
