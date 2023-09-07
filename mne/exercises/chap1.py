from mne.roots.closed_methods import root_bisection

def ex_5_1():
    def f(x: float) -> float:
        return -.5*x**2 + 2.5*x + 4.5

    res = root_bisection(f, 5, 10, iterations=3)

    print(res)
    return

def ex_5_2():
    def f(x):
        return 5*x**3 - 5*x**2 + 6*x - 2
    
    res = root_bisection(f, 0, 1)
    print(res)

if __name__ == '__main__':
    # ex_5_1()
    ex_5_2()