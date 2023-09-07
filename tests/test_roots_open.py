from pytest import approx

from mne.roots.open_methods import root_nr, MAX_ITER
from mne.functions import sqrt_of_4


def test_root_nr():
    def f_prime(x):
        return 2*x

    ''' 0.01 - ((0.01)**2 - 4)/(2*0.01) '''    
    res = root_nr(sqrt_of_4, f_prime, 0.01)
    assert res.iterations < MAX_ITER
    assert approx(2.0, 0.1) == res.root

    print(res)