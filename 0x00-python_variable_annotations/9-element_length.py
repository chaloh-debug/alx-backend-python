#!/usr/bin/env python3
""" Let's duck type an iterable object """


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Compute length of iterable and return list of tuples """
    return [(i, len(i)) for i in lst]