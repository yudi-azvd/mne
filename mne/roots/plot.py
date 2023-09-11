import numpy as np
import matplotlib.pyplot as plt

from mne.roots.closed_methods import Function


def plot(f: Function, x1: float, x2: float):
    samples = 100
    xs = np.linspace(x1, x2, samples)
    values = np.full(samples, 0, np.float32)
    
    for i, x in enumerate(xs):
        values[i] = f(x)
        
    plt.grid(visible=True)
    plt.plot(xs, values)
    plt.savefig('img.png')
