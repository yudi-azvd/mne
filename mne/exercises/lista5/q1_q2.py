from matplotlib import pyplot as plt

from mne.ode.euler import euler
import numpy as np


def derivative(y, x):
    return -2 * x**3 + 12 * x**2 - 20 * x + 8.5


def f_exact(x):
    return -(0.5) * x**4 + 4 * x**3 - 10 * x**2 + 8.5 * x + 1


if __name__ == '__main__':
    h = 0.5
    interval_h2 = np.arange(0, 4.1, h)
    N = len(interval_h2)
    y_true_h2 = np.zeros(N)
    y_euler_h2 = np.zeros(N)

    x = 0
    for i in range(0, N):
        y_true_h2[i] = f_exact(x)
        x += h

    x = 0
    y = 1
    for i in range(0, N):
        y_euler_h2[i] = y
        y = euler(derivative, y, x, h)
        x += h

    errors_p_h2 = abs((y_true_h2 - y_euler_h2) / y_true_h2)

    h = 0.25
    interval_h4 = np.arange(0, 4.1, h)
    N = len(interval_h4)
    y_true_h4 = np.zeros(N)
    x = 0
    for i in range(0, N):
        y_true_h4[i] = f_exact(x)
        x += h

    x = 0
    y = 1
    y_euler_h4 = np.zeros(N)
    for i in range(0, N):
        y_euler_h4[i] = y
        y = euler(derivative, y, x, h)
        x += h
    errors_p_h4 = abs((y_true_h4 - y_euler_h4) / y_true_h4)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(interval_h2, y_true_h2, label='Exato')
    ax1.plot(interval_h2, y_euler_h2, label='Euler h=0.5')
    ax1.plot(interval_h4, y_euler_h4, label='Euler h=0.25')
    ax1.legend()
    ax2.plot(interval_h2, errors_p_h2, label='Erro %', c='r')
    ax2.plot(interval_h4, errors_p_h4, label='Erro %', c='b')
    ax2.set_ylim(bottom=0, top=1.0)
    ax2.legend()
    plt.show()
