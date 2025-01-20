from tkinter import *

window = Tk()
window.geometry("200x160")
window.config(bg="green")

bt1 = Button(text="one").place(x=10,y=20,width=40,height=30)
bt2 = Button(text="two").place(x=10,y=60,width=80)
bt3 = Button(text="three").place(x=10,y=100,height=40)

'''
bt1.place(x=10,y=20,width=40,height=30)
bt2.place(x=10,y=60,width=80)
bt3.place(x=10,y=100,height=40)
'''
window.mainloop()