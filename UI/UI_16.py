from tkinter import *

window = Tk()
window.geometry("200x200")
window.config(bg="lightgray")

def text_change(*arg):
    sv2.set(sv1.get())


sv1 = StringVar()
sv1.trace_add("write",text_change)
ent1 = Entry(window,textvariable=sv1)
ent1.pack(pady=20)

sv2 = StringVar()
ent2 = Entry(window,textvariable=sv2,state=DISABLED)
ent2.pack(pady=10)

window.mainloop()