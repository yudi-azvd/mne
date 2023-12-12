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


def plot_r(
    ax,
    r_inicio: float = 0,
    r_fim: float = 4,
    markersize: float = 0.013,
    rate_samples=1000,
) -> None:
    x0 = 0.4
    r_span = np.linspace(r_inicio, r_fim, rate_samples)
    x, y = simulate(x0, r_span)
    ax.set_title(f'$r \in [{r_inicio}, {r_fim}]$')
    ax.set_ylim((0, 1))
    ax.plot(x, y, '^', alpha=0.4, markersize=markersize)
    return


# fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig, (ax1, ax2) = plt.subplots(1, 1)
fig.suptitle('Mapa logístico: $G(x) = rx(1-x)$')

r_inicio = 2.6
r_fim = 4.0
# plot_r(ax1, r_inicio, r_fim, markersize=0.05, rate_samples=1000)

r_inicio = 3.5
r_fim = 4
plot_r(ax2, r_inicio, r_fim, markersize=0.05, rate_samples=8000)

# r_inicio = 3.82
# r_fim = 3.86
# plotar(ax3, r_inicio, r_fim, markersize=0.1)

# r_inicio = 3.5
# r_fim = 5
# x0 = 0.4
# r_amostras = 4000
# r_intervalo = np.linspace(r_inicio, r_fim, r_amostras)
# x, y = simular(x0, r_intervalo)
# plt.title(f'$r \in [{r_inicio}, {r_fim}]$')
# plt.plot(x, y, '^', alpha=0.4, markersize=0.13)

plt.show()
