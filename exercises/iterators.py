"""Iterator exercises"""
from collections import Iterable

def first(elements):
    """Return the first item in given iterable."""
    return next(iter(elements))


def is_iterator(elements):
    """Return True if given iterable is an iterator."""
    return iter(elements) is elements


class Point:
    """3-D Point objects"""
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __iter__(self):
        yield from (self.x, self.y, self.z)


def all_same(iterable):
    """Return True if all items in the given iterable are the same."""
    for first_item in iterable:
        break
    for item in iterable:
        if item != first_item:
            return False
    return True

def minmax(iterable):
    """Return minimum and maximum values from given iterable."""
    try:
        min = max = next(iter(iterable)) 
    except StopIteration as e:
        raise ValueError('Iterable empty') from e
    
    for item in iterable:
        if item > max:
            max = item
        if item < min:
            min = item
    
    return min, max   

class RandomNumberGenerator:
    """Return infinite series of randomly generator numbers."""
