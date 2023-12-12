import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')


def logistic_map(x: float, r: float):
    """
    Umas observações interessantes sobre mapa logístico:
    https://blbadger.github.io/logistic-map.html
    """
    return x * r * (1 - x)


def simulate(x0, rate_span: np.ndarray):
    _x = []
    _y = []
    for r in rate_span:
        x = x0
        for _ in range(500):
            x = logistic_map(x, r)

        for i in range(100):
            x = logistic_map(x, r)
            _x.append(r)
            _y.append(x)
    return _x, _y


markersize = 0.05
x0 = 0.3
r_inicio = 3.48
r_fim = 4.0
r_samples = 8000
r_span = np.linspace(r_inicio, r_fim, r_samples)
x, y = simulate(x0, r_span)

plt.title('Mapa de bifurcação')
plt.ylim((0, 1))
plt.plot(x, y, '^', alpha=0.5, markersize=markersize)
plt.show()
