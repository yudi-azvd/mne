import matplotlib.pyplot as plt
import numpy as np

x0 = 0.4
x = x0
time_samples = 600
time_end = time_samples
time_span = np.linspace(0, time_end, time_samples)

rate_samples = 1000
r_start = 0
r_end = 4
rate_span = np.linspace(r_start, r_end, rate_samples)


def get_last_100_values(r: float, values: list[float]):
    xs: list[float] = []
    ys: list[float] = []

    for v in values[len(values) - 100 : len(values)]:
        ys.append(v)
        xs.append(r)
    return xs, ys


population_values_r: list[list[float]] = []
final_populations: list[float] = []

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Mapa logístico: G(x) = r x (1-x)')


def simulate(rate_span):
    _x = []
    _y = []
    for r in rate_span:
        pop_values = []
        x = x0
        for i in range(len(time_span)):
            x = r * x * (1.0 - x)
            pop_values.append(x)
        population_values_r.append(pop_values)
        final_populations.append(pop_values[-1])
        xs, ys = get_last_100_values(r, pop_values)
        _x.extend(xs)
        _y.extend(ys)

        # ax1.plot(time_span, pop_values)
        # ax2.scatter(xs, ys, s=0.05, alpha=0.3, c='k')
        # plt.show()
    return _x, _y


x, y = simulate(time_span)


i = int(len(rate_span) * 0.65)
# ax1.plot(time_span, population_values_r[i])
# ax1.set_ylim((-0.1, 1))

ax2.scatter(x, y, s=0.05, alpha=0.3, c='k')

plt.show()
