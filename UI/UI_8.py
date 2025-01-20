from tkinter import *

window = Tk()
window.title("Interface")
window.geometry("500x300")
window.config(bg="lightgreen")

b1 = Button(text="one").grid(row=0,column=0,padx=10,pady=10)
b2 = Button(text="two").grid(row=0,column=1,padx=10,pady=10 , sticky=W)
b3 = Button(text="three").grid(row=0,column=2,padx=10,pady=10 , ipadx=50)
b4 = Button(text="four").grid(row=1,column=0,padx=10,pady=10 , sticky=N)
b5 = Button(text="five").grid(row=1,column=1,padx=10,pady=10 ,ipadx=40,ipady=40,columnspan=1)
b6 = Button(text="six").grid(row=1,column=2,padx=10,pady=10 , sticky=NW)

window.mainloop()