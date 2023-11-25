import numpy as np
import matplotlib.pyplot as plt

from mne.roots.closed_methods import ClosedResult


def scale_interval(x1: float, x2: float, scale: float = 1.2) -> tuple[float, float]:
    return x1 / scale, x2 * scale


def plot_closed_result(result: ClosedResult, step: float = 0.1) -> None:
    iter = result.iterations
    assert (
        iter == len(result.xrs) == len(result.x1s) == len(result.x2s)
    ), f'{iter} == {len(result.xrs)} == {len(result.x1s)} == {len(result.x2s)}'

    x1 = result.x1s[0]
    x2 = result.x2s[0]
    xs = np.arange(x1, x2, step)
    values = np.full(len(xs), 0, np.float32)

    for i, x in enumerate(xs):
        # print(i, x)
        values[i] = result.f(x)

    zeros = np.full(len(result.xrs), 0, np.float32)
    alphas = np.linspace(0.1, 1, len(zeros))
    assert len(zeros) == len(alphas) == len(result.xrs)
    plt.scatter(result.xrs, zeros, c='r', alpha=alphas, marker='|')

    xl, xu = scale_interval(x1, x2)
    plt.axis([xl, xu, min(values), max(values)])

    plt.grid(visible=True)
    plt.plot(xs, values)
    plt.plot([x1], [0], 'bo')
    plt.plot([x2], [0], 'bo')

    plt.savefig('img.png')
