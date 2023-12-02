#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace  element of list at given position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
