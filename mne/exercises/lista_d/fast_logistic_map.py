import matplotlib.pyplot as plt
import numpy as np


def mapa_logistico(x: float, r: float):
    return x * r * (1 - x)


def simular(x0, rate_span):
    _x = []
    _y = []
    for r in rate_span:
        x = x0
        for _ in range(500):
            x = mapa_logistico(x, r)

        for i in range(100):
            x = mapa_logistico(x, r)
            _x.append(r)
            _y.append(x)
    return _x, _y


def plotar(
    ax, r_inicio: float = 0, r_fim: float = 4, markersize: float = 0.013
) -> None:
    x0 = 0.4
    r_amostras = 1000
    r_intervalo = np.linspace(r_inicio, r_fim, r_amostras)
    x, y = simular(x0, r_intervalo)
    ax.plot(x, y, '^', alpha=0.4, markersize=markersize)
    return


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Mapa logístico: $G(x) = rx(1-x)$')

ax1.set_title('Plot 1')
plotar(ax1, r_inicio=2.6, r_fim=4, markersize=0.05)

ax2.set_title('Plot 2')
plotar(ax2, r_inicio=3.62, r_fim=3.64, markersize=0.1)

plt.show()
