from mne.roots import root_bisection

def f_5_1(x: float) -> float:
    return -.5*x**2 + 2.5*x + 4.5

def ex_5_1():
    res = root_bisection(f_5_1, 5, 10, iterations=3)

    print(res)

    return

if __name__ == '__main__':
    ex_5_1()