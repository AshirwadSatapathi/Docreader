import pyttsx3
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Docreader")
engine = pyttsx3.init()


label1 = Label(root, text="Enter the message:")
label1.grid(row=0,column=0)
label2 = Label(root, text="Select Gender: ")
label2.grid(row=1,column=0)
entry1 = Entry(root, width=50)
entry1.grid(row=0,column=1)


def callback():
    textToVoice()

def textToVoice():
    i=int(selected.get())
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[i].id)
    engine.say(entry1.get())
    engine.runAndWait()
button = Button(root, text="Say", command=callback)
button.grid(row=4,column=1)

selected = IntVar()
rad1 = Radiobutton(root,text='Male', value=1, variable=selected)
rad2 = Radiobutton(root,text='Female', value=0, variable=selected)
#rad3 = Radiobutton(root,text='Third', value=3, variable=selected)
def clicked():
   print(selected.get())
rad1.grid(column=1, row=1)
rad2.grid(column=1, row=2)

#entry1.bind('<return>', get())
#root.wm_attributes('=topmost',1)
root.mainloop()
