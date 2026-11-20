from tkinter import *
from tkinter import messagebox



root = Tk()
root.geometry("200x200")




def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found!")


button = Button(root, text="Scan for Viruses", command=msg)
button.place(x=40, y=80)

root.mainloop()