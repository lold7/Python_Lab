from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(bg="lightgray")

bt1 = Button(text="one").pack(side = TOP , pady=50)
bt2 = Button(text="two").pack(side=TOP , pady=50)
bt3 = Button(text="three").pack(side=TOP , pady=50)

window.mainloop()