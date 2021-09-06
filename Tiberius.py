"""
Personal Assitant: Tiberius

Created on Thu Aug 26 16:54:28 2021

@author: philipbotar
"""
import speech_recognition as sr
import pyttsx3
import datetime
import sys
import os
import cryptocompare
import inflect


engine = pyttsx3.init()
engine.say('Hello, My name is Tiberius, How can i help you today?')
engine.runAndWait()
engine.stop()

inf = inflect.engine()

#this function determines which ordinal to use when presented with the day
def ordinal(day):
    if day % 10 == 1:
        ordinal = "st"
    elif day % 10 == 2:
        ordinal = "nd"
    elif day % 10 == 3:
        ordinal = "rd"
    else:
        ordinal = "th"

    return(ordinal)

def dateToday():
    dateAndTime = datetime.datetime.now()
    day = int(dateAndTime.strftime("%d"))
    weekday = str(dateAndTime.strftime("%A"))
    month = str(dateAndTime.strftime("%B"))

    engine.say("Today is " + weekday + " the " + str(day) + ordinal(day) + " of " + month)
    engine.runAndWait()
    engine.stop()

def dateTomorrow():
    dateAndTime = datetime.date.today() + datetime.timedelta(days=1)
    day = int(dateAndTime.strftime("%d"))
    weekday = str(dateAndTime.strftime("%A"))
    month = str(dateAndTime.strftime("%B"))

    engine.say("Tomorrow is " + weekday + " the " + str(day) + ordinal(day) + " of " + month)
    engine.runAndWait()
    engine.stop()

#this function writes the speechinput from the user
def writeNote(secondarySpeechInput):
    newNote = secondarySpeechInput
    with open('notes.txt', 'a') as notes:
        notes.write(newNote)
        notes.write("\n")


def readNote():
    with open('notes.txt', 'r') as notes:
        engine.say(notes.read())
        engine.runAndWait()
        engine.stop()

def deleteNote():
    os.remove("notes.txt")

#we use listenTo whenever we need a break in the speech and need a seperate input
def listenTo():
    hearing = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = hearing.listen(source)
    try:
        secondarySpeechInput = hearing.recognize_google(audio,language='en-in')
        print("You said " + hearing.recognize_google(audio,language='en-in'))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    return(secondarySpeechInput)

def btc():
    value = cryptocompare.get_avg('BTC', currency='USD', exchange='Kraken')
    price = int(value['PRICE'])
    price = str(price)
    price = inf.number_to_words(price)
    engine.say('Bitcoins current price is' + price + 'U S D')
    engine.runAndWait()
    engine.stop()

def eth():
    value = cryptocompare.get_avg('ETH', currency='USD', exchange='Kraken')
    price = int(value['PRICE'])
    price = str(price)
    price = inf.number_to_words(price)
    engine.say('Ethereums current price is' + price + 'U S D')
    engine.runAndWait()
    engine.stop()
                #return bitcoin price
            #elif symbol = ethereum:
                #return ethereum price
            #elif symbol = ripple:
                #return ripple price

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
if ("date" and "tomorrow") in speechInput:
    dateTomorrow()
    sys.exit()

if "date" in speechInput:
    dateToday()
    sys.exit()

if ("note" and "write") in speechInput or ("note" and "right") in speechInput:
    engine.say('What would you like me to write?')
    engine.runAndWait()
    engine.stop()
    secondarySpeechInput = listenTo()
    writeNote(secondarySpeechInput)
    sys.exit()

if ("note" and "read") in speechInput or ("notes" and "read") in speechInput:
    readNote()
    sys.exit()

if("note" and "delete") in speechInput or ("notes" and "delete") in speechInput:
    engine.say('Are you sure you want to delete your notes? This is irreversible')
    engine.runAndWait()
    engine.stop()
    secondarySpeechInput = listenTo()
    if "yes" in secondarySpeechInput:
        deleteNote()
    else:
        sys.exit()
    sys.exit()

if("price" and "Bitcoin") in speechInput:
    btc()
    sys.exit()

if("price" and "ethereum") in speechInput:
    eth()
#if("price" and "ripple") in speechInput:
