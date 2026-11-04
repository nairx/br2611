from tkinter import *

root = Tk() 

root.geometry("800x400")
root.title("My Application")

label = Label(root,text="Hello World",font=("Ariel",20))
label.pack()

label1 = Label(root,text="Good Evening")
label1.pack()

def greet():
    print("Greetings!")

button1 = Button(root,text="Click",command=greet)
button1.pack()

root.mainloop()