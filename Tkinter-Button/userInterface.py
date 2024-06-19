import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from time import sleep

root = tk.Tk(className=' EID Kanban ')
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.configure(bg='black')

bg = PhotoImage(file= 'D:\Program\GitTrain\Tkinter-Button\Image\Train_UI.png')
but_1 = PhotoImage(file='D:\Program\GitTrain\Tkinter-Button\Image\Button-Pull_Send.png')

def but1():
    value_1 = entry_1.get()
    print(value_1)
    stat.configure(text=value_1)
    entry_1.delete(0, END)
        
background = Label(root, image=bg)
background.place(x=-2, y=-2)

stat = Label(root, text="UI TRAIN", anchor="center", bg="white", font=('arial', 15, 'bold'))
stat.place(x=60, y=110)

entry_1 = Entry(root, font=('arial', 15, 'bold'))
entry_1.focus()
entry_1.place(x=60, y=160)

btn = tk.Button(root, bg="black",  bd=0, highlightthickness = 0, image=but_1, command=but1)
btn.place(x=60, y=210)

root.attributes('-fullscreen',True)
root.mainloop()