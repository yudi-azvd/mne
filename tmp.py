#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import numpy as np

counter = 0


def plot_graph():
    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    ax.scatter(x, y)
    global counter
    counter += 1
    print("plot", counter)
    # Chamar .draw toda vez que se requer atualizar o frame
    canvas.draw()


# Não é obrigatório, mas finaliza o programa mais rápido e libera o terminal
def on_close():
    exit(0)


root = tk.Tk()

fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig, master=root)
label = tk.Label(text="Matplotlib + Tkinter!")
label.config(font=("Courier", 32))

frame = tk.Frame(root)
label.pack()
frame.pack()
canvas.get_tk_widget().pack()

tk.Button(frame, text="Plot graph", command=plot_graph).pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
