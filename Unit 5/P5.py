# A DNA sequence is a s tring made up of As, Ts, Cs, and Gs. Write a GUI application in which a DNA sequence is entered, and when the Count button is clicked, the number of As, Ts, Cs, and Gs are counted and displayed in the window.

import tkinter as tk


def index():
    count = {}
    for i in seq.get():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    disp.set(str(count))


window = tk.Tk()
label1 = tk.Label(window, text="Enter DNA Sequence")
label1.pack()
seq = tk.StringVar()
disp = tk.StringVar()
textbox = tk.Entry(window, textvariable=seq)
textbox.pack()
button = tk.Button(window, text="Count", command=index)
button.pack()
label = tk.Label(window, textvariable=disp)
label.pack()
window.mainloop()
