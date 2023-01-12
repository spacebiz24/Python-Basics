# Write a Python program that creates a GUI with a textbox, Ok button and Quit button. On clicking Ok, the text entered in textbox is to be printed in Python shell; on clicking Quit, the program should terminate.

import tkinter as tk

def printshell():
    print(text.get())

window = tk.Tk()
text = tk.StringVar()
textbox = tk.Entry(window, textvariable=text)
textbox.pack()
quit = tk.Button(window, text="Quit", command=lambda: window.destroy())
quit.pack()
ok = tk.Button(window, text="OK", command=printshell)
ok.pack()
window.mainloop()
