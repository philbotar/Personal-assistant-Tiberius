"""
Personal Assitant: Tiberius

Created on Thu Aug 26 16:54:28 2021

@author: philipbotar
"""
import speech_recognition as sr  
import pyttsx3
import datetime



engine = pyttsx3.init()
engine.say('Hello, My name is Tiberius, How can i help you today?')
engine.runAndWait()
engine.stop()


#This function allows tiberius to tell us which day of the week it is and the date
def dateToday():
    dateAndTime = datetime.datetime.now()
    day = int(dateAndTime.strftime("%d"))
    weekday = str(dateAndTime.strftime("%A"))
    month = str(dateAndTime.strftime("%B"))

   #this if loop is checking to see what ordinal on the day should be used, e.g 22nd 
    if day % 10 == 1:
        ordinal = "st"
    elif day % 10 == 2:
        ordinal = "nd"
    elif day % 10 == 3:
        ordinal = "rd"
    else:
        ordinal = "th"

    engine.say("Today is " + weekday + " the " + str(day) + ordinal + " of " + month)
    engine.runAndWait()
    engine.stop()


#now lets implement the speech recognition
# get audio from the microphone                             
#what the following does is use the computers primary microphone as a source and
#then uses googles api to listen and transcribe what the user is saying     
hearing = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = hearing.listen(source)   
try:
    speechInput = hearing.recognize_google(audio,language='en-in')
    print("You said " + hearing.recognize_google(audio,language='en-in'))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

#These if statements will act as a guide for the AI, for what keywords are contained in the speech he will use as an index to return what the user is looking for.
if "date" in speechInput:
    dateToday()



