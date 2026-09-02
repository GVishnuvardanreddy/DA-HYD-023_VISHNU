import os
import time
import webbrowser
import uuid
import re
import playsound
from gtts import gTTS
import speech_recognition as sr
'''
text='welcome to codegnan,hope yoi are doing well'
#convert
tts=gTTS(text)
#print(tts)
tts.save("audio.mp3")
playsound.playsound("audio.mp3")
'''
#we will use speechRecognition
#we will create a listen function to listen
def listen():
    """function to listen the voice"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("start talking clearly")
        audio = r.listen(source,phrase_time_limit=10)

    data = " " #this will be your statement
    #Exception handling
    try:
        data=r.recognize_google(audio,language='en-US')
        print("you said:" + data)

    except sr.UnknownValueError:
        print("I couldn't hear your voice")

    except sr.RequestError as e:
        print("Request failed")

    return data
    #tts=gTTS(data)
    #tts.save("speech.mp3")
    #playsound.playsound("speech.mp3")
#listen()

#Now we will create a function to respond back

def respond(string):
    """Respond function"""
    print(string)
    tts=gTTS(string)
    tts.save('speech.mp3')
    filename = 'speech%s.mp3'%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#now we will create our assistant function to make
#conversation
def va(data):
    """VirtualAssistant Actions"""
    if "How are you" in data:
        listening=True
        respond("Iam doing gooood,hope you are well")

    elif "yah..! what is in your mind" in data:
        listening=True
        respond("Thinking about today's exam")

    elif "time" in data:
        listening=True
        respond(time.ctime())

    elif "open google" in data.casefold():
        listening = True
        reg_ex = re.search('open google(.*)',data)
        url = "https://www.google.com/"
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        respond("Successfully done")
    elif "open song" in data.casefold():
        listening = True
        reg_ex = re.search('open google(.*)',data)
        url = "https://www.bing.com/videos/riverview/relatedvideo?q=yeshnagula+youtube+song&mid=4ADED89D57EA931E0A334ADED89D57EA931E0A33&churl=&mcid=F38DC8FE3A4B4E5D98C8F7CEEC242D67&FORM=VIRE"
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        respond("Successfully done")
    elif "locate" in data.casefold():
        listening = True
        webbrowser.open('https://www.google.com/maps'+ data.replace("locate",""))
        respond("located")

    elif "stop talikng" in data:
        listening=False
        respond("okay cool")

    try:
        return listening
    except UnboundLocalError:
        print("Time out")

respond("hey ....how are you")
#Greeting from assistent
listening=True
while listening:
    data=listen()
    listening=va(data)
