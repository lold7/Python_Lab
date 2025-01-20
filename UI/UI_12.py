from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(bg="lightgray")

def ok():
    print("OK")


def cancel():
    x = b_cancle.cget("text")
    print(x)


b_ok = Button(text="OK" , command=ok).grid(row=1 ,column=0)
b_cancle = Button(text="Cancel" ,command=cancel)
b_cancle.grid(row=1,column=1)


window.mainloop()

