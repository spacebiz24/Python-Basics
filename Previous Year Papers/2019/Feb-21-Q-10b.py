# Design and implement a GUI application which accepts the “name” and “time of the day” as input and displays an appropriate greeting message based on the time of the day.

import tkinter as tk

def wish():
    x = ""
    lst = time.get().split(",")
    if int(lst[1]) > 5 and int(lst[1]) < 12:
        x = "Good morning"
    elif int(lst[1]) >= 12 and int(lst[1]) < 16:
        x = "Good Afternoon"
    elif int(lst[1]) >= 16 and int(lst[1]) < 20:
        x = "Good Evening"
    else:
        x = "Good night"
    show.set("{}, {}".format(x, lst[0]))

window = tk.Tk()

label1 = tk.Label(window, text="Enter: {Name,time(24)}")
label1.pack()

time = tk.StringVar()
box = tk.Entry(window, textvariable=time)
box.pack()

calc = tk.Button(window, text="Wish", command=wish)
calc.pack()

show = tk.StringVar()
disp = tk.Label(window, textvariable=show)
disp.pack()

window.mainloop()
