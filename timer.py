from tkinter import *
from tkinter import messagebox
import time

# creating a window object 
window = Tk()

# setting up width and height of the window
window.geometry("350x150")

# setting up object title
window.title("Timer")

# setting up hours, minutes, seconds    
hr = StringVar()
min = StringVar()
sec = StringVar()

# setting up default values
hr.set("00")
min.set("00")
sec.set("00")

# setting up user inputs for the 3 fields and placements
hrEntry = Entry(window, width=4, font=("Arial",18,""), textvariable=hr)
hrEntry.place(x=80,y=20)

minEntry = Entry(window, width=4, font=("Arial",18,""), textvariable=min)
minEntry.place(x=140,y=20)

secEntry = Entry(window, width=4, font=("Arial",18,""), textvariable=sec)
secEntry.place(x=200,y=20)

# logic for timer
def setTimer():
    try:
        tmp = int(hr.get()) * 3600 + int(min.get()) * 60 + int(sec.get()); 
    except:
        print("Input right value.")

    while tmp >= 0:
        # minutes = tmp // 60, seconds = tmp % 60
        minutes, seconds = divmod(tmp,60)

        hours = 0
        #  hours = minutes // 60, minutes = minutes % 60
        if minutes > 60:
            hours, minutes = divmod(minutes,60)
        
        # storing values
        hr.set("{0:2d}".format(hours))
        min.set("{0:2d}".format(minutes))
        sec.set("{0:2d}".format(seconds))

        window.update()
        time.sleep(1)

        # when time is up
        if (tmp == 0):
            messagebox.showinfo("Countdown Finished","Time's UP!")

        tmp -= 1

button = Button(window, text="Set Timer", bd='7', command=setTimer)
button.place(x=120,y=70)

window.mainloop()