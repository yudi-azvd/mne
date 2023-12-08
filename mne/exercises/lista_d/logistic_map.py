import matplotlib.pyplot as plt
import numpy as np

time_samples = 1000
x0 = 0.4
x = x0
r = 2.6
total_time = 500
time_span = np.linspace(0, total_time, total_time)
rates = np.linspace(0, 4, time_samples)


list_of_repeated_values = []


def close_to_any(a: float, values: list[float], **kwargs):
    return np.any(np.isclose(a, values, **kwargs))


def get_repeated_points(r: float, values: list[float]):
    xs: list[float] = []
    ys: list[float] = []

    if r < 3:
        ys.append(values[-1])
        xs.append(r)
        list_of_repeated_values.append(ys)
        return xs, ys

    for i, v in reversed(list(enumerate(values))):
        if close_to_any(v, ys, rtol=0.0000000000000000000000000000001):
            break
        else:
            ys.append(v)
            xs.append(r)

    list_of_repeated_values.append(ys)
    return xs, ys


population_values_r: list[list[float]] = []
final_populations: list[float] = []

_x = []
_y = []
for r in rates:
    pop_values = []
    x = x0
    for i in range(len(time_span)):
        x = r * x * (1.0 - x)
        pop_values.append(x)
    population_values_r.append(pop_values)
    final_populations.append(pop_values[-1])
    xs, ys = get_repeated_points(r, pop_values)
    _x.extend(xs)
    _y.extend(ys)


i = int(len(rates) * 0.72)
print(rates[i])
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Mapa logístico: G(x) = r x (1-x)')

ax1.plot(time_span, population_values_r[i])
ax1.set_ylim((-0.1, 1))

ax2.scatter(_x, _y, s=0.05, alpha=0.3, c='k')

plt.show()
