# Write a GUI application with a button labeled "Goodbye." When the button is clicked, the window closes.

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text="Goodbye", command=lambda:window.destroy())
button.pack()
window.mainloop()