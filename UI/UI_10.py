from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(bg="lightblue")

fm = Frame(window)
fm.place(x=250,y=250)
fm.config(bg="pink")

Button(fm,text="ONE",bg="red",fg="green").grid(column=1,row=1)

window.mainloop()