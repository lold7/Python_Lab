from tkinter import *
import random

window = Tk()
window.geometry("300x300")
window.config(bg="lightblue")

window.option_add("*Button.background","lightgreen")
window.option_add("*Button.foreground","red")

def rand():
    r = random.randint(1,100)
    if r > 50:
        bnext.config(state=NORMAL)
    else:
        bnext.config(state=DISABLED)


bnext = Button(text="Next",state=DISABLED)
ran = Button(text="Random",command=rand)
ran.grid(row=1,column=0,padx=5)
bnext.grid(row=1,column=1,padx=5)

window.mainloop()