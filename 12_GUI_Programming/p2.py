from tkinter import *

root = Tk() 

root.geometry("800x400")
root.title("My Application")

def display():
    txt = entry.get()
    label.config(text="Hello " + txt)

entry = Entry(root)
entry.pack()

button = Button(root,text="Submit",command=display)
button.pack() 

label = Label(root,text="")
label.pack() 

root.mainloop()