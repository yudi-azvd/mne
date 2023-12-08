import matplotlib.pyplot as plt
import numpy as np


x0 = 0.4
r_start = 3.63
r_end = 3.6325
rate_samples = 1600
rate_span = np.linspace(r_start, r_end, rate_samples)


def logistic_map(x: float, r: float):
    return x * r * (1 - x)


population_values_r: list[list[float]] = []
final_populations: list[float] = []

_x = []
_y = []

for r in rate_span:
    x = x0
    for i in range(500):
        x = logistic_map(x, r)

    for i in range(100):
        x = logistic_map(x, r)
        _x.append(r)
        _y.append(x)

plt.ylim((-0.1, 1))
plt.title('Mapa logístico: G(x) = r x (1-x)')
plt.scatter(_x, _y, s=0.05, alpha=0.2, c='k')
plt.show()
