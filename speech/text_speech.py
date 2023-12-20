# pyttsx3
import pyttsx3
txt_sp=pyttsx3.init()
txt=input("enter the text to convert....\n")
txt_sp.say(txt)
txt_sp.runAndWait()