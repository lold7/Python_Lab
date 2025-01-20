from tkinter import *

window = Tk()
window.title("Tk interface")
window.geometry("250x100")
window.minsize(200,80)
window.resizable(0,0)

label = Label(text = "Enter your data")
entry = Entry()
button = Button(text= "OK")

label.pack()
entry.pack()
button.pack()

window.mainloop()