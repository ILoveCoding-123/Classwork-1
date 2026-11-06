from tkinter import *
from datetime import date


root = Tk()
root.title("Getting Started With Widgets")
root.geometry("400x300")



lbl = Label(text="Hey there!", fg="white", bg="#072F5F", height=1, width=300)



money_lbl = Label(text="How much money do you need? ", bg="#3895D3")
money_entry = Entry()


def display():
    money = money_entry.get()


    global message
    message = "Welcome to the application! \nToday's date is: "
    greet = "Here is the amount you need: $" + money + "\n"


    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())


text_box = Text(height = 3)



btn = Button(text="Begin", command=display, height = 1, bg="#1261A0", fg="white")


lbl.pack()
money_lbl.pack()
money_entry.pack()
btn.pack()
text_box.pack()


root.mainloop()