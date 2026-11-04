from tkinter import *

root = Tk() 

root.geometry("800x400")
root.title("My Application")

menu_bar = Menu(root) 
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
recent_menu = Menu(file_menu,tearoff=0)
recent_menu.add_command(label="file1.txt")
recent_menu.add_command(label="file2.txt")
recent_menu.add_command(label="file3.txt")
file_menu.add_separator()
file_menu.add_command(label="Exit")

edit_menu = Menu(menu_bar,tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

file_menu.add_cascade(label="Recent",menu=recent_menu)

menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
root.config(menu=menu_bar)
root.mainloop()