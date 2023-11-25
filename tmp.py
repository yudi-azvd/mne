#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import customtkinter as ctk
import numpy as np

ctk.set_default_color_theme('blue')
print(ctk.ThemeManager.theme)


counter = 0
# https://stackoverflow.com/questions/48391568/matplotlib-creating-plot-for-black-background-presentation-slides
plt.style.use('dark_background')


def plot_graph():
    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    ax.scatter(x, y, c=['red'])
    global counter
    counter += 1
    print('plot', counter)
    # Chamar .draw toda vez que se requer atualizar o frame
    _canvas.draw()
    canvas.draw()


# Não é obrigatório, mas finaliza o programa mais rápido e libera o terminal
def on_close():
    exit(0)


root = tk.Tk()
# https://stackoverflow.com/questions/4581504/how-to-set-opacity-of-background-colour-of-graph-with-matplotlib
plt.rcParams.update(
    {
        # Não é equivalente ao debaixo
        # 'figure.facecolor': (1.0, 1.0, 1.0, 0.14),
        # 'axes.facecolor': (1.0, 1.0, 1.0, 0.14),
        'figure.facecolor': (0.14, 0.14, 0.14, 1.0),
        'axes.facecolor': (0.14, 0.14, 0.14, 1.0),
    }
)
fig, ax = plt.subplots()

_canvas = FigureCanvasTkAgg(fig, master=root)
_label = tk.Label(text='Matplotlib + Tkinter!')
_label.config(font=('Courier', 32))

_frame = tk.Frame(root)
_label.pack()
_frame.pack()
# canvas.get_tk_widget().pack()

# tk.Button(_frame, text="Plot graph", command=plot_graph).pack(pady=10)

root.protocol('WM_DELETE_WINDOW', on_close)
# root.mainloop()

app = ctk.CTk()
canvas = FigureCanvasTkAgg(fig, master=app)
frame = ctk.CTkFrame(app)
label = ctk.CTkLabel(app, text='Matplotlib + Tkinter modern S2')
label.configure(font=('Helvetica', 32))

ctk.CTkButton(frame, text='Plot graph', command=plot_graph).pack(pady=10)
label.pack()
frame.pack()
canvas.get_tk_widget().pack()

app.protocol('WM_DELETE_WINDOW', on_close)

app.geometry('720x480')
app.title('Some title')
app.mainloop()
