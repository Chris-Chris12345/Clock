from tkinter import *
from tkinter.ttk import *
# importing strftime function to
# retrieve system's time
from time import strftime

root = Tk()
root.title("Clock")

def time():
    h = int(strftime("%H")) #Get hour in 24H format
    m = (strftime("%M"))
    s = (strftime("%S"))
    am_pm = "AM" if h < 12 else "PM"

    h = h % 12 #Convert to 12H format (handling midnight as 12)
    final_time = f"{h}:{m}:{s} {am_pm}"
    time_label.config(text=final_time)
    time_label.after(1000,time)


time_label = Label(root,font = ("Times New Roman",40),background="red",foreground="white")
time_label.pack(anchor="center")

time()
root.mainloop()