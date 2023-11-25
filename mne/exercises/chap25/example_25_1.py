from matplotlib import pyplot as plt

from mne.ode.euler import euler
import numpy as np


def derivative(y, x):
    return -2 * x**3 + 12 * x**2 - 20 * x + 8.5


def f_exact(x):
    return -(0.5) * x**4 + 4 * x**3 - 10 * x**2 + 8.5 * x + 1


if __name__ == '__main__':
    h = 0.5

    interval = np.arange(0, 4.1, h)
    N = len(interval)
    y_true = np.zeros(N)
    y_euler = np.zeros(N)

    x = 0
    for i in range(0, N):
        y_true[i] = f_exact(x)
        x += h

    x = 0
    y = 1
    for i in range(0, N):
        y_euler[i] = y
        y = euler(derivative, y, x, h)
        x += h
        print(x, '%.2f' % y)

    errors_p = abs((y_true - y_euler) / y_true)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(interval, y_true, label='Exato')
    ax1.plot(interval, y_euler, label='Euler')
    ax1.legend()
    ax2.plot(interval, errors_p, label='Erro %', c='r')
    ax2.legend()
    plt.show()
