from mne.roots.open_methods import root_nr


def f(x: float):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5


def fprime(x: float):
    return 6*x**2 - 23.4*x + 17.7


x0 = 3
res = root_nr(f, fprime, x0, rel_err=0.001, max_iterations=5)
print(res.to_str())
