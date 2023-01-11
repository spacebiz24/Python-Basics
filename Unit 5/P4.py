# Write a GUI application with a single button. Initially the button is labeled 0, but each time it is clicked, the value on the button increases by 1.

import tkinter as tk

def increment():
    x.set(x.get() + 1)

window = tk.Tk()
x = tk.IntVar()
x.set(0)
button = tk.Button(window, textvariable=x, command=increment)
button.pack()
window.mainloop()
