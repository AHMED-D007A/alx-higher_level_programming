#!/usr/bin/python3
"""This is a text_indentation module."""


def text_indentation(text):
    "this function prints the given text wiht indentation"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace("?", "?^")
    text = text.replace(":", ":^")
    text = text.replace(".", ".^")
    print("\n\n".join(map(lambda x: x.strip(), text.split("^"))), end="")
