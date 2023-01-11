# Write a GUI application with a button labeled "Goodbye." When the button is clicked, the window closes.

import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Goodbye", command=lambda: window.destroy())
button.pack()
window.mainloop()
