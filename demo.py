import pyttsx3
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Docreader")
engine = pyttsx3.init()


label1 = Label(root, text="Enter the message:")
label1.grid(row=0,column=0)
entry1 = Entry(root, width=50)
entry1.grid(row=0,column=1)


def callback():
    textToVoice()

def textToVoice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(entry1.get())
    engine.runAndWait()
button = Button(root, text="Say", command=callback)
button.grid(row=0,column=2)
#entry1.bind('<return>', get())
#root.wm_attributes('=topmost',1)
root.mainloop()
