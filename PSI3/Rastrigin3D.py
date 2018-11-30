from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt
import numpy as np

def rastrigin(*X, **kwargs):
    A = kwargs.get('A', 10)
    return A * len(X) + sum([(x ** 2 - A * np.cos(2 * math.pi * x)) for x in X])

def rastrigin_show(axis_X, axis_Y, axis_Z, filename = 'show'):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(axis_X, axis_Y, axis_Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
    if filename == 'show':
        plt.show()
    else:
        plt.savefig(filename + '.png')

def make_data(min,max,range):
    X = np.linspace(min, max, range)
    Y = np.linspace(min, max, range)
    X, Y = np.meshgrid(X, Y)
    return X, Y

if __name__ == '__main__':

    X,Y = make_data(-2,2,200)
    Z = np.asarray(rastrigin(X,Y))
    print(X)
    rastrigin_show(X,Y,Z)
    print(Z)


