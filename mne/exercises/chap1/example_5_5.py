from math import exp

from mne.roots.closed_methods import root_false_position, StopOption


def f(x: float) -> float:
    return 9.81*68.1/x*(1 - exp(-10*x/68.1)) - 40
    
    
def main():
    '''
    Note que x1 muda quase nada ao longo das iterações. Nesse exemplo, o inter.
    [x1, x2] não encolhe, mas converge para um valor fixo.
    ''' 

    res = root_false_position(f, 12, 16, max_iterations=4, option=StopOption.ITERATIONS)
    print(res)


main()