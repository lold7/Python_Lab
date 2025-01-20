from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(bg="lightgray")

bt1 = Button(text="one").pack(side=TOP, fill= X)
bt2 = Button(text="two").pack(side=LEFT , fill=Y)
bt3 = Button(text="three").pack(side=BOTTOM , fill = X)

window.mainloop()