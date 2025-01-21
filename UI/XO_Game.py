from tkinter import *

window = Tk()
window.geometry("200x200")
window.config(bg="green")
window.title("XO")
window.resizable(0,0)
window.option_add("*Button.background","lightgreen")
window.option_add("*Button.font","times 16 bold")
ref = "O"

def add_button(bt,r,c):
    bt.config(width= 3, command = lambda:click(bt))
    bt.grid(row = r,column=c , padx = 10 , pady = 10)


for i in range(0,3):
    for j in range(0,3):
        add_button(Button() , i , j)

def click(b):
    if b.cget("text") != "":
        return
    
    global ref
    ref = "O" if ref == "X" else "X"
    b.config(text = ref)


window.mainloop()