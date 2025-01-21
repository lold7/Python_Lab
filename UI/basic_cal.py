from tkinter import *

window = Tk()
window.geometry("420x150")
window.resizable(0,0)
window.config(bg="lightgray",pady=10)
window.option_add("*font","tahoma 10")
window.option_add("*Button.width",3)
window.option_add("*Entry.width",10)
window.option_add("*Button.background","gray")
window.option_add("*Label.background","lightgray")



fm1 = Frame(window)
fm1.pack(side=TOP)

fm2 = Frame(window)
fm2.place(x=70,y=60)
fm2.config(bg="lightgray")


lb1 = Label(fm1 , text="Number 1:").pack(side=LEFT)
et1 = Entry(fm1)
et1.pack(side=LEFT)

lb2 = Label(fm1,text="Number 2:").pack(side=LEFT)
et2 = Entry(fm1)
et2.pack(side=LEFT)

lb3 = Label(fm1,text="Result:").pack(side=LEFT)
et3 = Entry(fm1)
et3.bind("<Key>","break")
et3.pack(side=LEFT)


math = ["+","-","*","/","%","//","**"]

def math_button(txt):
    button = Button(fm2,text=txt ,command=lambda:cal(button))
    button.pack(side=LEFT,padx=5)


for i in math:
    math_button(i)

def cal(x):
    try:
        txt = x.cget("text")
        v1 = float(et1.get())
        v2 = float(et2.get())
        result = eval(f"{v1}{txt}{v2}")
        result = int(result) if result % 1 == 0 else result
    except:
        ""
        
    et3.delete(first=0,last=END)
    et3.insert(0,result)



window.mainloop()