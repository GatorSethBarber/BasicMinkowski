# https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html#sphx-glr-gallery-mplot3d-surface3d-2-py
# https://stackoverflow.com/questions/51574861/plotting-3d-surface-using-python-raise-valueerrorargument-z-must-be-2-dimensi

import matplotlib.pyplot as plt
import numpy as np
import minkowski


TETRAHEDRON = [(0, 0, 0), (2, 0, 0), (1, np.sqrt(3), 0), (1, 1/np.sqrt(3), np.sqrt(8/3))]
TRIANGLE = [(0, 0, 0), (2, 0, 0), (1, np.sqrt(3), 0)]


def flip_dimension(shape, *args):
    for i in range(len(shape)):
        new_vec = list(shape[i])
        for n in args:
            new_vec[n] = - new_vec[n]
        shape[i] = tuple(new_vec)


def scale_dimension(shape, factor, *args):
    for i in range(len(shape)):
        new_vec = list(shape[i])
        for n in args:
            new_vec[n] = factor * new_vec[n]
        shape[i] = tuple(new_vec)


def to_arrays_3d(shape):
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
