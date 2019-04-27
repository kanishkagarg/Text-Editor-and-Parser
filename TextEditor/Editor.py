from tkinter import *

def PrintName():
	print("Hey! My Name is Harsh Vishnoi.")

root = Tk()

menu = Menu(root, bg = "#808080", fg = "#FFFFFF")
root.config(menu=menu)

subMenu1 = Menu(menu)
subMenu2 = Menu(menu)
subMenu3 = Menu(menu)
subMenu4 = Menu(menu)

menu.add_cascade(label =  "File", menu = subMenu1)
menu.add_cascade(label =  "Edit", menu = subMenu2)
menu.add_cascade(label =  "Run", menu = subMenu3)
menu.add_cascade(label =  "Docs", menu = subMenu4)

# ***** File Menu

subMenu1.add_command(label = "New File", command = PrintName)
subMenu1.add_command(label = "Open File", command = PrintName)

subMenu1.add_separator()

subMenu1.add_command(label = "Save", command = PrintName)
subMenu1.add_command(label = "Save as", command = PrintName)

subMenu1.add_separator()

subMenu1.add_command(label = "Close", command = PrintName)
subMenu1.add_command(label = "Quit", command = PrintName)

# ***** Edit Menu

subMenu2.add_command(label = "Cut", command = PrintName)
subMenu2.add_command(label = "Copy", command = PrintName)
subMenu2.add_command(label = "Paste", command = PrintName)

# ***** editor

T = Text(root, height = 51, width = 200, bg = "#3C3636", fg = "#FFFFFF", padx = 10, pady = 10, spacing1 = 5).pack(side = LEFT)

root.mainloop()