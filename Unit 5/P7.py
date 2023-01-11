# When a value is entered in the text field and the Convert button is clicked, the value s hould be converted from Fahrenheit to Celsius and displayed in the window, as s hown in the image below.

import tkinter as tk


def F2C():
    temp = (temp_f.get() - 32) * 5 / 9
    temp_c.set(temp)


window = tk.Tk()
label = tk.Label(window, text="Temperature in Fahrenheit")
label.pack()
temp_f = tk.DoubleVar()
temp_c = tk.DoubleVar()
textbox = tk.Entry(window, textvariable=temp_f)
textbox.pack()
printc = tk.Label(window, textvariable=temp_c)
printc.pack()
convert = tk.Button(window, text = "Convert", command = F2C)
convert.pack()
quit = tk.Button(window, text = "Quit", command = lambda: window.destroy())
quit.pack()
window.mainloop()
