"""Generator Function Exercises."""
from collections.abc import Iterable

def unique(iterable):
    """Yield iterable elements in order, skipping duplicate values."""
    seen_items = set()
    for item in iterable:
        if item not in seen_items:
            yield item
            seen_items.add(item)


def float_range(start, stop, step=1):
    """Return iterable of numbers from start to stop by step."""   
    while start < stop:
        yield start
        start += step
        


def head(iterables, n=1):
    """Return first n items of a given iterable."""
    for index, item in enumerate(iterables):
        if index >= n:
            break
        yield item

def interleave(iter1, iter2):
    """function that takes two iterables and returns a generator object.
       with each of hte given items interleaved
    >>>list(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
    [1, 5, 2, 6, 3, 7, 4, 8]
    """
    for pairs in zip(iter1, iter2):
        yield from pairs
    

def pairwise(iterable):
    """
    Yield a tuple containing each item and the item following it.

    The item after the last one is treated as ``None``.
    """
    previous, current = None, None
    
    for current in iterable:
        if previous:
            yield previous, current
        previous = current
    if current:
        yield current, None
            
        


def around(elements):
    """
    Yield a tuple of the previous, current, and next items.

    The previous item should start at ``None`` and the next item should
    be ``None`` for the last item in the iterable.
    """
    previous, current = None, None
    for next_item in elements:
        if current:
            yield previous, current, next_item
        previous, current = current, next_item
    if current:
        yield previous, current, None


def stop_on(elements, stop_item):
    """Yield from the iterable until the given value is reached."""
    for item in elements:
        if item == stop_item:
            break
        yield item

def deep_flatten(elements):
    """Flatten an iterable of iterables."""
    try:
        for iterables in elements:
            yield from deep_flatten(iterables)
    except TypeError:
        yield elements


def get_primes_over(limit):
    """Return given number of primes over 1,000,000."""
    candidate = 1000000
    count = 0
    while count < limit:
        if is_prime(candidate):
            yield candidate
            count += 1
            candidate += 1
        else:
            candidate += 1
            

def is_prime(candidate):
    for n in range(2, candidate):
        if candidate % n == 0:
            return False
    return True


