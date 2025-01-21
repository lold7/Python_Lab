from tkinter import *
from datetime import datetime

window = Tk()
window.geometry("200x60")
window.title("Time")
window.config(bg="lightgray")

lb = Label(font="time 16")
lb.pack(pady=20)

def time_show():
    cur_time = datetime.now()
    format_time = cur_time.strftime("%H:%M:%S")
    lb.config(text=format_time)
    lb.after(1000,time_show)


time_show()

window.mainloop()