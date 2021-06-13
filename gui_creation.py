import tkinter
from tkinter import *
root=tkinter.Tk()
root.title(" crackz--billing")
root.geometry("500x500")
label=tkinter.Label(root,text="wellcome").pack()
button=Button(root,text="press",bg="blue",fg="black")
button.grid(column=10,row=10)
root.mainloop()
