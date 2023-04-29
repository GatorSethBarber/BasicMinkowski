"""
Implements Minkowski addition

Author: Seth Barber
Date: April 29, 2023
"""

def minkowski_basic(first, second):
    """
    Brute force Minkowski addition
    :param first: The first shape (as an iterable of iterable position vectors)
    :param second: The second shape (as an iterable of iterable position vectors)
    :return: The Minkowski sum
    """
    new_shape = set()
    dimension = 0
    if len(first) > 0:
        dimension = len(first[0])
    elif len(second) > 0:
        dimension = len(second[0])
    for vec1 in first:
        for vec2 in second:
            if len(vec1) != dimension or len(vec2) != dimension:
                raise SyntaxError('All of the vectors should be the same dimension')
            new_pair = list()
            for el1, el2 in zip(vec1, vec2):
                new_pair.append(el1 + el2)
            new_shape.add(tuple(new_pair))
    return new_shape


if __name__ == '__main__':
    t1 = [(0, 0), (1, 0), (0.5, 3**0.5)]
    t2 = t1.copy()
    t3 = [(0,0), (1, 0), (0.5, -3**0.5)]
    print(minkowski_basic(t1, t2))
    print(minkowski_basic(t1, t3))
