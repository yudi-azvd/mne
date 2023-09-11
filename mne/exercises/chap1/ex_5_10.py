from mne.roots.closed_methods import root_false_position, StopOption


def f(x: float) -> float:
    return x**4 - 8*x**3 - 35*x**2 + 450*x - 1001
    
    
def main():
    res = root_false_position(f, 4.5, 6, max_iterations=5, option=StopOption.ITERATIONS)
    # res = root_false_position(f, 4.5, 6, _rel_err=1.0)
    print(res.to_str(xt=5.60979))

main()