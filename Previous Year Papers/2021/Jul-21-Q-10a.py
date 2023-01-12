# With the help of widget GUI elements, design a window as follows:

import tkinter as tk

window = tk.Tk()

but1 = tk.Button(window, text="Button1")
but1.config(fg="red")
but1.pack()
but2 = tk.Button(window, text="Button2")
but2.config(fg="green")
but2.pack()
but3 = tk.Button(window, text="Button3")
but3.config(fg="purple")
but3.pack(side="left")
but4 = tk.Button(window, text="Button4")
but4.config(fg="yellow")
but4.pack(side="left")

window.mainloop()
