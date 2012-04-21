import numpy as np
import matplotlib.pyplot as plt

import sympy
from sympy.abc import x, y


plt.rc('contour', negative_linestyle='solid')


def velocity_field(psi):
    u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
    v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
    return u, v


def plot_streamlines(u, v, xlim=(-1, 1), ylim=(-1, 1), ax=None):
    x0, x1 = xlim
    y0, y1 = ylim
    Y, X =  np.ogrid[y0:y1:100j, x0:x1:100j]
    ax.streamplot(X, Y, u(X, Y), v(X, Y), color='cornflowerblue')


def format_axes(ax):
    ax.set_aspect('equal')
    ax.figure.subplots_adjust(bottom=0, top=1, left=0, right=1)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    for spine in ax.spines.itervalues():
        spine.set_visible(False)


if __name__ == '__main__':
    from mpltools import layout
    plt.rcParams['figure.figsize'] = (4, 4)

    # Cylinder flow
    def cylinder_stream_function(U=1, R=1):
        r = sympy.sqrt(x**2 + y**2)
        theta = sympy.atan2(y, x)
        return U * (r - R**2 / r) * sympy.sin(theta)

    psi = cylinder_stream_function()
    u, v = velocity_field(psi)

    xlim = ylim = (-3, 3)
    figsize = layout.figaspect(1)
    fig, ax = plt.subplots(figsize=figsize)
    plot_streamlines(u, v, xlim, ylim, ax)

    c = plt.Circle((0, 0), radius=1, facecolor='none')
    ax.add_patch(c)
    format_axes(ax)
    plt.savefig('plotting-streamlines-with-matplotlib-and-sympy-1.png')

    # Corner flow
    def corner_stream_function(n=1, A=1):
        r = sympy.sqrt(x**2 + y**2)
        theta = sympy.atan2(y, x)
        return A * r**n * sympy.sin(n * theta)

    psi = corner_stream_function(n=2)
    u, v = velocity_field(psi)

    figsize = layout.figaspect(0.5)
    fig, ax = plt.subplots(figsize=figsize)
    plot_streamlines(u, v, ylim=(0, 1), ax=ax)
    ax.plot([-1, 1], [0, 0], 'k')
    format_axes(ax)
    plt.savefig('plotting-streamlines-with-matplotlib-and-sympy-2.png')

    psi = corner_stream_function(n=3/2.)
    u, v = velocity_field(psi)

    figsize = layout.figaspect(0.5)
    fig, ax = plt.subplots(figsize=figsize)
    plot_streamlines(u, v, ylim=(0, 1), ax=ax)
    ax.plot([np.cos(125 * np.pi/180), 0, 1], [1, 0, 0], 'k')
    format_axes(ax)
    plt.savefig('plotting-streamlines-with-matplotlib-and-sympy-3.png')

    psi = corner_stream_function(n=-2)
    u, v = velocity_field(psi)

    fig, ax = plt.subplots()
    plot_streamlines(u, v, ax=ax)
    format_axes(ax)
    plt.savefig('plotting-streamlines-with-matplotlib-and-sympy-4.png')

    plt.show()

