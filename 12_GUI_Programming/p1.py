from tkinter import *

root = Tk() 

root.geometry("800x400")
root.title("My Application")

label = Label(root,text="Hello World, How are you")
label.grid(row=1,column=0)
# label.place(x=0,y=0)
# label.place(relx=0.1,rely=0.1)
# label.pack()

label1 = Label(root,text="Good Evening")
label1.grid(row=2,column=0)
# label1.place(relx=0.2,rely=0.2)
# # label1.pack(pady=50)

def greet():
    print("Greetings!")

button1 = Button(root,text="Click",command=greet)
button1.grid(row=3,column=0)
# # button1.pack()

root.mainloop()