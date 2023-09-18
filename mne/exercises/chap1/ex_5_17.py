from math import pi

from mne.roots.closed_methods import root_false_position_mod, StopOption
from mne.roots.plot import plot


def f(h: float) -> float:
    return -h**3*pi/3 + h**2 * 3 * pi - 30
    
x1 = 0
x2 = 3


def main():
    res = root_false_position_mod(f, x1, x2, max_iterations=3, option=StopOption.ITERATIONS)
    print(res.to_str())
    plot(f, x1, x2)

main()