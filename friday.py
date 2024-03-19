import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
import random
import sys
import wolframalpha
import datef
import pywhatkit as kit
import pyautogui as pi
pi.FAILSAFE = False
import pyperclip
import pyjokes
import cv2
import psutil
import pyowm
import subprocess
import json
from quotes import Quotes
import math
import time
from GoogleNews import GoogleNews
import ctypes
import sounddevice as sd
import playsound
import glob
import clipboard
import datetime
import pytz
from selenium import webdriver
from PyDictionary import PyDictionary
from selenium.webdriver.chrome.options import Options
import turtle
import fractions

interogative = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which','how':'how', 'when':'when'}

name = "Your name"
gender = "Sir"


engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('api') #your api key
owm = pyowm.OWM('api') # your api key


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #u can change voice id according to your choice
engine.setProperty("rate", 125)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query

def sleeptime():
    
    if os.path.exists("goodnight.txt"):
        starttime=int(datetime.datetime.now().minute)
        f = open("goodnight.txt", "r+")
        endtime = f.readlines()
        sleeptime = starttime - int(endtime[0])
        if sleeptime  < 1:
            speak("You Did not sleep at all om")
        else:    
            speak(f"You slept for {sleeptime} hours")

def wishMe():
    #playsound.playsound('laugh.mp3')
    speak("Welcome back sir!")
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=16 and hour<24:
        speak("Good Evening!")

    else:
        speak("Good night")
    strTime = datetime.datetime.now().strftime("%I:%M:%p").replace(":","").replace("None","")
    speak(f"I am Friday sir, {gender} Now it is {strTime} {weather()}")

def weather():
    city = 'Your city'
    Location = owm.weather_manager().weather_at_place(city)
    weather = Location.weather
    temp = weather.temperature(unit='celsius')
    status = weather.detailed_status
    cleaned_temp_data = (int(temp['temp']))
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<18:
        speak('The temperature today in location is' + (f"{cleaned_temp_data} degree celsius"))
        print('The temperature today in location is' + (f"{cleaned_temp_data} degree celsius"))
    if 'rain' in status or 'thunderstorm' in status or 'drizzle' in status:
        speak('No need to go outside. Sir Because weather is not good')
        print('No need to go outside. Sir Because today weather is not good')
    else:
        speak('Sir today is very pleasent day. You should go outside and enjoy the day')
        print('Sir today is very pleasent day. You should go outside and enjoy the day')
    
def read():
    pi.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    speak(tobespoken)    

def recsound():
    fs=44100
    speak("what should be the length of your sound wave Plz answer in seconds")
    ans=int(takeCommand())
    seconds=ans

    recorded=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
    sd.wait()
    speak("sucessfully recoreded")
    speak("what should i keep the file name")
    filename=takeCommand()
    print(filename+'.mp3',fs,recorded)
    speak("sucessfuly saved")
    try:
        speak("should i show you")
        reply=takeCommand()
        if "yes" in reply:
            os.startfile(filename+".mp3")

    except:
        if "no" in reply:
            speak("okay next command sir")


def jokes():
    my_joke = pyjokes.get_joke('en', category='all')
    print(my_joke)
    speak(my_joke)
    playsound.playsound("laugh.mp3")

def clickedbtn(self):
	global query
	query=takeCommand().lower()


def is_valid_search(phrase):
        if(interogative.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
            return True

def findmeaning():
    speak("Pronouce the word which you want to find out")
    query = takeCommand().lower()
    dictionary=PyDictionary()
    print (dictionary.meaning(query))
    speak (dictionary.meaning(query))

def Synonyms():
    speak("Pronouce the word which you want to find out")
    query = takeCommand().lower()
    dictionary=PyDictionary()
    print (dictionary.synonym(query))
    speak (dictionary.synonym(query))

def Antonym():
    speak("Pronouce the word which you want to find out")
    query = takeCommand().lower()
    dictionary=PyDictionary()
    print (dictionary.antonym(query))
    speak (dictionary.antonym(query))

def translate():
    speak("Pronouce the word which you want to translate it")
    query = takeCommand().lower()
    dictionary=PyDictionary()
    print (dictionary.translate(query,"de"))


def screenshot():
    img = pi.screenshot()
    img.save("Your location address")



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@gmail.com', 'yourpassword')
    server.sendmail('Your gmail', to, content)
    server.close()

def news():
    speak("What kind of news would you like to hear ?")
    type = takeCommand()
    googleNews = GoogleNews()
    googleNews = GoogleNews(lang = 'en-in')
    googleNews.search(type) # will search the kind we want to hear
    googleNews.getpage(5) # page number of news 
    googleNews.result()
    list = googleNews.gettext()
    #print(list)
    if len(list) > 0:
       speak(random.choice(list))
    else:
       speak("No news related to this topic.") 
    
    
def quotes():
    quotes = Quotes()
    persons = quotes.random()
    l=str(persons[1])
    print(l,"\n")
    speak(l)
       

if __name__ == "__main__":
    wishMe()

    while True:
    #if 1:
        query = takeCommand().lower()
        
      

        if 'wikipedia' in query:
            try:
                speak('Searching wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sir I could not recongnise what you said to search on wikipedia plz speak one more chance")    

        if 'search' in query:
            try:
                speak('Searching Query..')
                res = client.query(query)
                results = next(res.results).text
                speak('WOLFRAM-ALPHA says - ')
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry this type of content is not available on wolframalpha")
       
        elif 'translate' in query:
            translate()

        elif "good night" in query:
            strTime = datetime.datetime.now().strftime("%X").replace(":"," ") 
            gtime=strTime.replace(":"," ") 
            speak(f"Good night {name} {gender} it is {gtime} sleep tight..")

        elif "minimise window" in query:
            os.system('''powershell -command "(new-object -com shell.application).minimizeall()"''')

        elif "record my voice" in query:
            recsound()

        elif 'quotes' in query:
            speak('Sir this quotes for you'+f"{quotes()}")

        elif is_valid_search(query):
            speak("Searching Question")
            taburl="http://google.com/?#q="
            question=query
            webbrowser.open(taburl+question)

        elif 'open youtube' in query:
            speak("Opening youtube for you boss")
            chrome_path = 'Your chrome location browser address'
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'ok google' in query:
            speak("Sir, What should i search on google")
            query = takeCommand().lower()
            search = 'https://www.google.com/search?q=' +query
            chrome_path = 'Your chrome location browser address'
            webbrowser.get(chrome_path).open(f"{search}")

        elif 'open notepad' in query:
            speak("Opening notepad boss")
            path = "your notepad address"
            os.startfile(path)

        elif 'open command' in query:
            os.system("start cmd")        

        elif 'play music' in query:
            music_dir = "Your music folder location"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'email' in query:
            try:
                to = "your email address"
                speak("What Should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent sucessfully!")
            except Exception as e:
                print(e)
                speak("Sorry bro. I was not able to send mail because of your fault")

        elif "quit" in query or 'good bye' in query or 'bye' in query or 'exit' in query or 'deactivate' in query:
            speak(f"Thank you {name} for giving your time i had fun serving you,have a good time")
            speak("closing engine")
            speak("closing required applications")
            endTime = int(datetime.datetime.now().hour)
            f = open("goodnight.txt", "w+")
            end = int(datetime.datetime.now().hour)
            f.write(str(end))
            f.close()       
            playsound.playsound("power down.mp3")
            quit()


        #random conservation
            

        elif 'hello' in query or 'wake up jarvis' in query or 'lets do it jarvis' in query:
            stMsgs = ['Tell me work sir!', 'Yes Sir']
            speak(random.choice(stMsgs))

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))    
            
        elif 'where are you right now' in query:
            stMsgs = ['Stuck in a tin box!', 'In a tin box!']
            speak(random.choice(stMsgs))
#geographic data
            
        elif 'ip address' in query:
            from requests import get
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            print(ip)

        elif 'location' in query:
            res = requests.get('https://ipinfo.io/')
            data = res.json()

            city = data['city']

            location = data['loc'].split(',')
            latitude = location[0]
            longitude = location[1]
            address=data['country']

            print("Latitude value :", latitude)
            speak("Latitude value is {}".format(latitude))
            print("Longitude value: ", longitude)
            speak("Longitude value is {}".format(longitude))
            print("Captial City : ", city)
            speak("Captial City Name is {}".format(city))
            print("Country :",address)
            speak("Country name is {}".format(address))

        
        elif 'play latest song' in query:
            speak("Sir,Enjoy your song")      
            music_dir = "Folder location" 
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            speak(rd)
            os.startfile(os.path.join(music_dir, rd)) 

        elif 'alarm' in query:
            speak("Sir,which time i set the alarm")
            datef.alarm(query)
            

        elif 'youtube' in query:
            speak("Sir,What Should I search on youtube")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

        elif "shutdown" in query:
            speak("Sir do you really want to shutdown the computer")
            reply = takeCommand().lower()
            if "yes" in reply:
                os.system('shutdown /s /t 1')
            else:
                continue

        elif "restart" in query:
            speak("Sir do you really want to restart the computer")
            reply = takeCommand().lower()
            if "yes" in reply:
                os.system('shutdown /r /t 1')
            else:
                continue

        elif "log out" in query:
            speak("Sir do you really want to log out the computer")
            reply = takeCommand().lower()
            if "yes" in reply:
                os.system('shutdown -1')
            else:
                continue

        elif 'Remeber it' in query:
            speak("What should I write down sir")
            note = takeCommand().lower()
            remember = open("data.txt", 'w')
            remember.write(note)
            remember.close()
            speak("I have noted that" + note)

        elif 'told me' in query:
            remember = open('data.txt', 'r').read()
            speak("You told me to remeber that" + remember)    

        elif 'screenshot' in query:
            screenshot()
            speak("Sir,I have taken screenshot")

        elif 'joke' in query:
            jokes()
           

        elif 'switch window' in query:
            pi.keyDown("alt")
            pi.press("tab")
            pi.keyUp("alt")

        elif 'switch tab' in query:
            pi.keyDown("ctrl")
            pi.press("tab")
            pi.keyUp("alt")
                                    
        elif 'FOlder name' in query:
            os.startfile("location of the folderr") #any folder you want to open

        elif 'password' in query:
            speak("Ok master")	    
            speak("Here is Your Saved Connected Wifi Password")
            Collect_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            Collect_profiles = [i.split(":")[1][1:-1] for i in Collect_data if "All User Profile" in i]
            for i in Collect_profiles:
                results=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    print("Wifi name: {:<20}|  Password: {:<}".format(i, results[0]))
                    speak("Wifi name: {:<20}|  Password: {:<}".format(i, results[0]))
                except:
                    print("Wifi name: {:<20}|  Password:  {:<}".format(i, ""))
                    speak("Wifi name: {:<20}|  Password:  {:<}".format(i, ""))   

        elif "lock" in query:
            speak('Ok Sir! your pc is being locked')       
            for value in ['pc', 'system', 'windows']:
                ctypes.windll.user32.LockWorkStation()

        elif "sleep mode" in query:
            speak('Ok sir! your pc is being sleeped')
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    

        elif "task view" in query:
            pi.keyDown("win")
            pi.press("tab")
            pi.keyUp("win")

        elif "close current window" in query:
            pi.keyDown("alt")
            pi.press("f4")
            pi.keyUp("alt")

        elif "show start menu" in query:
            pi.press("win")

        
        elif "where is" in query:    
            query = query.split(" ")
            location = query[2]
            speak("Just A Second Sir, I will show you where " + location + " is.")

            URL = "https://www.google.com/maps/place/" + location + "/&amp;"
            webbrowser.open(URL, new=2)
            
        elif "read" in query:
            try:
                read()
            except:
                speak("no text selected plz select a text")

        elif "type" in query:
            speak(f"okay i am listening speak{name} {gender}")
            pi.typewrite(takeCommand())

        elif "select all" in query:
            pi.hotkey('ctrl','a')

        elif "open a new tab" in query:
            pi.hotkey('ctrl','n')

        elif "open a new incognito tab" in query:
            pi.hotkey('ctrl','shift','n')

        elif "copy" in query:
            pi.hotkey('ctrl','c')
            speak('text copied to clipboard')

        elif "paste" in query:
            pi.hotkey('ctrl','v')

        elif "undo" in query:
            pi.hotkey('ctrl','z')

        elif "redo" in query:
            pi.hotkey('ctrl','y')

        elif "save" in query:
            pi.hotkey('ctrl','s')

        elif "back" in query:
            pi.hotkey('browserback')

        elif "go up" in query:
            pi.hotkey('pageup') 

        elif "go to top" in query:
            pi.hotkey('home')
 
        elif "beatbox" in query or "Beatbox" in query:
            beatboxes=['beatbox (1).wav','beatbox (3).wav','beatbox (4).wav','beatbox (5).wav','beatbox (6).wav','beatbox (7).wav' ]
            playsound.playsound(random.choice(beatboxes))

        elif "date" in query:
            date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
            speak(f"Today is {date} ")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")    
            speak(f"the time is {strTime}")    
       
        elif 'meaning of' in query:
            findmeaning()
        