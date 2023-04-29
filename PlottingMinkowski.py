"""
Basic functionality for plotting Minkowski sums of 3 and 2 dimensional shapes.

Author: Seth Barber
Date: April 29, 2023

Citations:

For information about plotting in 3 dimensions using Matplotlib:
# https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html#sphx-glr-gallery-mplot3d-surface3d-2-py
# https://stackoverflow.com/questions/51574861/plotting-3d-surface-using-python-raise-valueerrorargument-z-must-be-2-dimensi
"""

import matplotlib.pyplot as plt
import numpy as np
import minkowski


TETRAHEDRON = [(0, 0, 0), (2, 0, 0), (1, np.sqrt(3), 0), (1, 1/np.sqrt(3), np.sqrt(8/3))]
TRIANGLE = [(0, 0, 0), (2, 0, 0), (1, np.sqrt(3), 0)]


def flip_dimension(shape, *args):
    """
    Flip the shape through one or more dimensions. For example, in flipping across the x-axis, it is actually y that
    is effected, so 1 for y is passed.
    :param shape: An iterable container of tuples representing position vectors in the shape
    :param args: 0 for x, 1 for y, 2 for z
    :return: None
    """
    for i in range(len(shape)):
        new_vec = list(shape[i])
        for n in args:
            new_vec[n] = - new_vec[n]
        shape[i] = tuple(new_vec)


def scale_dimension(shape, factor, *args):
    """
    Scale the shape so that
    :param shape: An iterable container of tuples representing position vectors in the shape
    :param factor: The factor to scale by
    :param args: The dimensions to scale (0 for x, 1 for y, 2 for z)
    :return: None
    """
    for i in range(len(shape)):
        new_vec = list(shape[i])
        for n in args:
            new_vec[n] = factor * new_vec[n]
        shape[i] = tuple(new_vec)


def to_arrays_3d(shape):
    """
    Used to convert a shape into three separate numpy arrays for graphing using Matplotlib
    :param shape: An iterable of tuples representing position vectors in the shape
    :return: Numpy arrays x, y, and z
    """
    temp_x = list()
    temp_y = list()
    temp_z = list()
    for vec in shape:
        temp_x.append(vec[0])
        temp_y.append(vec[1])
        temp_z.append(vec[2])
    x = np.array(temp_x)
    y = np.array(temp_y)
    z = np.array(temp_z)

    return x, y, z


def plot_shape(shape):
    """
    Plot the shape
    :param shape: An iterable of tuples representing position vectors in the shape
    :return: None
    """
    x, y, z = to_arrays_3d(shape)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_trisurf(x, y, z)
    plt.show()


if __name__ == '__main__':
    tetraOne = TETRAHEDRON.copy()
    tetraTwo = tetraOne.copy()
    flip_dimension(tetraTwo, 1)
    scale_dimension(tetraTwo, 2, 1)
    plot_shape(tetraOne)
    plot_shape(tetraTwo)
    plot_shape(minkowski.minkowski_basic(tetraOne, tetraTwo))

    triOne = TRIANGLE.copy()
    triTwo = TRIANGLE.copy()
    flip_dimension(triTwo)
    plot_shape(triOne)
    plot_shape(triTwo)
    plot_shape(minkowski.minkowski_basic(triOne, triTwo))
