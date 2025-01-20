from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(bg="lightgray")

fm1 = Frame(window , bg="pink")
fm2 = Frame(window , bg="pink")
fm1.pack(side= LEFT)
fm2.pack(side= LEFT , padx = 20)

Button(fm1,text="one").pack(side=TOP)
Button(fm1,text="two").pack(side=TOP)
Button(fm1,text="three").pack(side=TOP)

Button(fm2,text="first").grid(row=0,column=0)
Button(fm2,text="second").grid(row=0,column=1)
Button(fm2,text="third").grid(row=1,column=0)
Button(fm2,text="fourth").grid(row=1,column=1)

window.mainloop()