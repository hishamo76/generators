"""List comprehension exercises"""


def get_vowel_names(names: str):
    """Return a list containing all names given that start with a vowel."""
    return [
        name
        for name in names
        if name.lower()[0] in 'aeouiy'
    ]


def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [ item for lst in matrix for item in lst ]


def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    # l0 = []
    # for row in string.splitlines():
    #     l1 = []
    #     for x in row.split():
    #         l1.append(int(x))
    #     l0.append(l1)
    # return l0

    return [
        [int(x) for x in row.split()]
        for row in string.splitlines()
        ]
        
        


def power_list(n):
    """Return a list that contains each number raised to the i-th power."""
    # l = []
    # for index, num in enumerate(n):
    #     l.append(num**(index))
    # return l
    return [
        num**index 
        for index, num in enumerate(n)]

def matrix_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    # result = []
    # for arr1, arr2 in zip(matrix1, matrix2):
    #     temp = []
    #     for i1, i2 in zip(arr1, arr2):
    #         temp.append(i1+i2)
    #     result.append(temp)
    # return result
            
    return [
        [n + m for n, m in zip(row1, row2)] 
         for row1, row2 in zip(matrix1, matrix2)
    ]

def identity(size):
    """Return an identity matrix of size x size."""
    return [
        [same_value(x, y) for x in range(size)] 
        for y in range(size)]


def same_value(x, y):
    return 1 if x == y else 0

def triples(num):
    """Return list of Pythagorean triples less than input num."""
    #! A Pythagorean triple is a group of 3 integers a, b, and c, such that they satisfy 
    #! the formula a**2 + b**2 = c**2
    # result = []
    # for a in range(1, num):
    #     for b in range(a+1, num):
    #         for c in range(b+1, num):
    #             if a**2 + b**2 == c**2:
    #                 result.append((a, b, c))
    # return result

    return [
        (a, b, c)
        for a in range(1, num)
        for b in range(a+1, num)
        for c in range(b+1, num)
        if a**2 + b**2 == c**2
    ]