import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray

plt.style.use('dark_background')


x0 = 0.4
time_samples = 500
time_start = 1.1
time_end = time_samples
time_span = np.linspace(time_start, time_end, time_samples)

r_samples = 1000
r_start = 0
r_end = 4
r_span = np.linspace(r_start, r_end, r_samples)


def get_last_100_values(r: float, values: list[float]):
    xs: list[float] = []
    ys: list[float] = []

    for v in values[len(values) - 100 : len(values)]:
        ys.append(v)
        xs.append(r)
    return xs, ys


population_values_r: list[list[float]] = []

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Mapa logístico: G(x) = r x (1-x)')


def simulate(x0: float = 0.4, rate_span: ndarray = [], time_span: ndarray = []):
    _x = []
    _y = []
    for r in rate_span:
        pop_values = []
        x = x0
        for i in range(len(time_span)):
            x = r * x * (1.0 - x)
            pop_values.append(x)
        population_values_r.append(pop_values)
        xs, ys = get_last_100_values(r, pop_values)
        _x.extend(xs)
        _y.extend(ys)
    return _x, _y


def simulate_time_span(x0, r, time_span):
    x = x0
    _y = []
    _x = []
    for i in range(len(time_span)):
        _y.append(x)
        _x.append(i)
        x = r * x * (1.0 - x)
    return _x, _y


ax1.set_ylim((0, 1))
ax1.set_xlim((-1, 100))
r = 3.68
x0 = 0.30
x, y = simulate_time_span(x0, r, time_span)
ax1.plot(x, y)

x0 = 0.50
x, y = simulate_time_span(x0, r, time_span)
# ax1.plot(x, y)

x, y = simulate(x0, r_span, time_span)
ax2.plot(x, y, '^', markersize=0.13, alpha=0.3)

# r = 3.1
# i = int(len(rate_span) * 0.774)
# print('i', i, 'rate = ', rate_span[i])
# ax1.set_ylim((-0.1, 1))
# ax1.set_xlim((-1, 30))
# ax1.plot(time_span, population_values_r[i])

plt.show()
