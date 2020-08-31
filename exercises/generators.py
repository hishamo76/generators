"""Generator Expression Exercises."""


def sum_all(matrix):
    """Return the sum of all numbers in the given list-of-lists."""
    total = 0
    # for numbers in matrix:
    #     total += sum(numbers)
    # return total
    
    return sum (
        n
        for arr in matrix
        for n in arr
    )


def all_together(*args):
    """String together all items from the given iterables."""
    #! normal function
    # arr = []
    # for itr in args:
    #     for item in itr:
    #         arr.append(item)
    # return arr
    
    #! generator expression
    # return (
    #     element
    #     for arr in args
    #     for element in arr
    # )
        
    #! generator function
    # for iterable in args:
    #     for item in iterable:
    #         yield item
        
    #! even shorter by using yield from only  python > 3.5
    for iterable in args:
        yield from iterable

def interleave(iter1, iter2):
    """Return iterable of one item at a time from each list."""
    return (
        item
        for pair in zip(iter1, iter2)
        for item in pair
    )


def deep_add():
    """Return sum of values in given iterable, iterating deeply."""


def parse_ranges():
    """Return a list of numbers corresponding to number ranges in a string"""


def is_prime():
    """Return True if candidate number is prime."""
