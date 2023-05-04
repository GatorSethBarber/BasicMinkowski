"""
Basic functionality for plotting Minkowski sums of 3 and 2 dimensional shapes.

Author: Seth Barber
Date: April 29, 2023

Citations:

[1] and [2] for triangularization, [3] and [4] for general 3d plotting

[1] JohanC, "How to visualize polyhedrons defined by their vertices in 3D with matplotlib or/and plotly offline?",
StackOverflow, Aug. 1, 2020. [Online.]
Available: https://stackoverflow.com/questions/63207496/how-to-visualize-polyhedrons-defined-by-
their-vertices-in-3d-with-matplotlib-or. [Accessed May 3, 2023]

[2] "scipy.spatial.ConvexHull", SciPy Documentation, 2023. [Online.]
Available: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html. [Accessed May 3, 2023]

[3] "3D surface (solid color)", Matplotlib, 2023. [Online.]
Available: https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html#sphx-glr-gallery-mplot3d-surface3d-2-py.
[Accessed May 3, 2023]

[4] dtward, "Plotting 3D surface using python: raise ValueError("Argument Z must be 2-dimensional.")
matplotlib [duplicate]", StackOverflow, Jul. 28, 2018. [Online.]
Available: https://stackoverflow.com/questions/51574861/plotting-3d-surface-using-python-raise-valueerrorargument
-z-must-be-2-dimensi. [Accessed May 3, 2023]
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
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


def get_triangularization(shape):
    """
    Gets the triangularization of the shape. Based off of information and code
    provided by [1] and [2]
    """
    if len(shape) < 3:
        raise SyntaxError("Cannot compute triangulization for under 3 vertices.")
    if len(shape) == 3:
        return np.array([[0, 1, 2]])
    else:
        return ConvexHull(np.array([list(vec) for vec in shape])).simplices


def plot_shape(shape):
    """
    Plot the shape. Note: Learned about plotting 3d through sources [3] and [3] and
    the animation from source [5].
    :param shape: An iterable of tuples representing position vectors in the shape
    :return: None
    """
    # x, y, z = to_arrays_3d(shape)
    new_array = np.array([list(vec) for vec in shape])
    x = new_array[:, 0]
    y = new_array[:, 1]
    z = new_array[:, 2]

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Set lables (from source [5])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Case 1: Two dimensional: Default triangulization is fine.
    if np.argmax(x) == np.argmin(x) or np.argmax(y) == np.argmin(y) or np.argmin(z) == np.argmax(z):
        ax.plot_trisurf(x, y, z)

    # Case 2: Three dimensional: Get Convex hull
    else:
        ax.plot_trisurf(x, y, z, triangles=get_triangularization(shape), antialiased=False)

    plt.show()


if __name__ == '__main__':
    tetraOne = TETRAHEDRON.copy()
    tetraTwo = tetraOne.copy()
    flip_dimension(tetraTwo, 1, 2)
    plot_shape(tetraOne)
    plot_shape(tetraTwo)
    plot_shape(minkowski.minkowski_basic(tetraOne, tetraTwo))

    triOne = TRIANGLE.copy()
    triTwo = TRIANGLE.copy()
    flip_dimension(triTwo)
    plot_shape(triOne)
    plot_shape(triTwo)
    plot_shape(minkowski.minkowski_basic(triOne, triTwo))
