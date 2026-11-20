from tkinter import *
from tkinter import messagebox




window = Tk()
window.title("Event Handler")
window.geometry("100x100")


def handle_keypress(event):
    print(event.char)



window.bind("<Key>", handle_keypress)


def handle_click(event):
    print("\nThe button was clicked!")


def msg():
    messagebox.showwarning("Alert", "The button was not supposed to be clicked!")


button = Button(text="Click Me!", command=msg)
button.pack()


button2 = Button(window, text="Scan for Viruses", command=msg)
button2.pack()


button.bind("<Button-1>", handle_click)

button2.bind("<Button-2>", handle_click)

window.mainloop()