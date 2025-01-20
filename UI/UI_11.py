from tkinter import *

window = Tk()
window.geometry("500x500")
window.option_add("*Button.background","navy")
window.option_add("*Button.foreground","red")


Button(text='one').place(x=100,y=100)
Button(text='two').place(x=300,y=300)

window.mainloop()