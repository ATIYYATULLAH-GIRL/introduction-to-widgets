from tkinter import *
from datetime import date

root=Tk()
root.title("Getting Started With Widgets")
root.geometry("500x400")

label1=Label(text="WELCOME TO MY APPLICATION", fg="white", bg="pink", height=1, width=300)
label1.pack()

name_label=Label(text="Full name", bg="purple")
name_label.pack()

name_entry=Entry()
name_entry.pack()

def display():
    name=name_entry.get()
    msg="WELCOME TO THE APPLICATION\n"
    greet="Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,msg)
    text_box.insert(END,date.today())
button=Button(text="CLICK ME", height=1, command=display)
button.pack()

text_box=Text(height=3)
text_box.pack()

root.mainloop()