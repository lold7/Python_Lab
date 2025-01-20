from tkinter import *

window = Tk()
window.geometry("300x300")
window.config(bg="lightgreen")

bOk = Button(text="OK" , command=lambda:click(bOk),bg="lightblue")
bCan = Button(text="Cancel" , command=lambda:click(bCan),bg="lightblue")
bOk.place(x=50,y=50)
bCan.place(x=100,y=100)


def click(x):
    text = x.cget("text")
    print(text)


window.mainloop()