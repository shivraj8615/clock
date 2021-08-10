import tkinter as ui
import time
window = ui.Tk()
def update_time():
    hour = time.strftime("%I")
    minute = time.strftime("%m")
    second = time.strftime("%s")
    am_or_pm = time.strftime("%p")
    time_text = hour +":"+minute+":"+second+" "+am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000,update_time)


digital_clock_lbl = ui.Label(window,text="00:00:00",font='Helvetica 72 bold')
digital_clock_lbl.pack()
update_time()
window.mainloop()