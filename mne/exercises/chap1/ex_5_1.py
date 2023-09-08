from mne.roots.closed_methods import root_bisection, StopOption
from mne.roots.closed_methods_plot import plot_closed_result


def f(x: float) -> float:
    return -.5*x**2 + 2.5*x + 4.5
    
    
def main():
    res = root_bisection(f, 5, 10, max_iterations=10, option=StopOption.ITERATIONS)
    plot_closed_result(res, step=0.05)
    print(res)


main()