from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(bg="lightgray")

bt1 = Button(text="one").pack(anchor= NW , expand=YES)
bt2 = Button(text="two").pack(anchor=NE , expand= YES)
bt3 = Button(text="three").pack(anchor= E , expand=YES)

window.mainloop()