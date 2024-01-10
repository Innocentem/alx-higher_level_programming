#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        initial_position = file.tell()
        file.write(text)
        final_position = file.tell()

    characters_added = final_position - initial_position
    return characters_added
