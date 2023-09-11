from mne.roots.closed_methods import root_false_position, root_bisection, StopOption


def f(x: float) -> float:
    return x**10 - 1
    
    
def main():
    res = root_bisection(f, 0, 1.3, max_iterations=5, option=StopOption.ITERATIONS)
    print('> BISECTION')
    print(res)
    print()
    print('> FALSE POSITION')
    res = root_false_position(f, 0, 1.3, max_iterations=5, option=StopOption.ITERATIONS)
    print(res)


main()