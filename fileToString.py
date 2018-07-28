import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
b=input("enter the file name :")
file = open(b,"r")
a = file.read()
print(a)
def message():
    message = a
    return message
def speak(a):
    engine.say(a)
    engine.runAndWait()
    engine.stop()
def flow():
    a=message()
    speak(a)
flow()
