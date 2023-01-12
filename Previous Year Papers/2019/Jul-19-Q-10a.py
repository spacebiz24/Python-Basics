# Design and implement a GUI application to find if the input year is a leap year or not.

import tkinter as tk

def leapornot():
    if year.get() % 400 == 0 or year.get() % 4 == 0:
        message.set("Leap Year!")
    else:
        message.set("Not a Leap Year!")

window = tk.Tk()
label = tk.Label(window, text="Enter a year to check if it is leap or not")
label.pack()
year = tk.IntVar()
textbox = tk.Entry(window, textvariable=year)
textbox.pack()
button = tk.Button(window, text="Check", command=leapornot)
button.pack()
message = tk.StringVar()
disp = tk.Label(window, textvariable=message)
disp.pack()
window.mainloop()
