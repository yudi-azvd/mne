from mne.roots.closed_methods import root_false_position, root_bisection, StopOption


def f(x: float) -> float:
    return x**10 - 1
    
    
def main():
    x1 = 0
    x2 = 1.3
    iter = 5
    option = StopOption.ITERATIONS
    xt = 1

    res = root_bisection(f, x1, x2, max_iterations=iter, option=option)
    print('> BISECTION')
    print(res.to_str(xt))
    print()
    print('> FALSE POSITION')
    res = root_false_position(f, x1, x2, max_iterations=iter, option=option)
    print(res.to_str(xt))


main()