import tkinter as tk
import time

'''A script to remind me to walk a bit every hour '''

def countdown():
    t = 3600
    while t > 0:
        t -= 1
        time.sleep(1)
    alert()
    
def alert():
    window = tk.Tk()
    remember = tk.Label(text="Estira las patas")
    remember.pack()
    window.mainloop()
    countdown()
    
countdown()
