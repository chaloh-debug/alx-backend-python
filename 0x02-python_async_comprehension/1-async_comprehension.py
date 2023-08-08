#!/usr/bin/env python3
""" Async Comprehensions """
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ comprehension form generating 10 numbers """
    return [var async for var in async_generator()]
