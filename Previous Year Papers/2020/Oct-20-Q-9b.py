# Design and implement a GUI application to accept a string of numbers and displays the sorted list on click of the button named "sort".

import tkinter as tk

def sort():
    list = string.get().split(sep=",")
    for i in range(len(list) - 1):
        if list[i + 1] < list[i]:
            list[i + 1], list[i] = list[i], list[i + 1]
    slist.set(list)

window = tk.Tk()
label = tk.Label(window, text="Enter numbers seperated by commas to sort")
label.pack()
string = tk.StringVar()
textbox = tk.Entry(window, textvariable=string)
textbox.pack()
button = tk.Button(window, text="Sort", command=sort)
button.pack()
slist = tk.StringVar()
message = tk.Label(window, text="Sorted List:")
message.pack()
disp = tk.Label(window, textvariable=slist)
disp.pack()
window.mainloop()
