from mne.roots.closed_methods import (
    root_false_position,
    root_bisection,
    root_false_position_mod,
    StopOption,
)


def f(x: float) -> float:
    return x**10 - 1


x1 = 0.0
x2 = 1.3
iter = 5
option = StopOption.ITERATIONS
xt = 1


def main():
    res = root_bisection(f, x1, x2, max_iterations=iter, option=option)
    print('> BISECTION')
    print(res.to_str(xt))
    print()
    print('> FALSE POSITION')
    res = root_false_position(f, x1, x2, max_iterations=iter, option=option)
    print(res.to_str(xt))


def main2():
    res = root_bisection(f, x1, x2, _rel_err=0.01)
    print('> BISECTION')
    print(res.to_str(xt))
    print()
    print('> FALSE POSITION')
    # FIXME: O livro disse que era pra esse método parar em 39 iterações "naturalmente"
    # Eu to tendo que forçar a parada pq o erro relativo nunca fica menor que o especificado.
    res = root_false_position(
        f, x1, x2, _rel_err=0.01, max_iterations=42, option=option
    )
    print(res.to_str(xt))
    print()
    print('> FALSE POSITION MOD')
    res = root_false_position_mod(f, x1, x2, _rel_err=0.01)
    print(res.to_str(xt))


main()
# main2()
