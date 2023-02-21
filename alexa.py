
import speech_recognition as sr 
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
engine.say("hey i am alex what can i do for you")

def talk(text):
  engine.say(text)
  engine.runAndWait()

def alexa_command():
 try:
      with sr.Microphone() as source:
       print("listener----")
       voice=listener.listen(source) 
       command=listener.recognize_google(voice)
       command=command.lower()
      if "alexa" in command:
            command=command.replace("alexa","")
            talk(command)
            print(command)
 except:
    pass
 return command 
         
def run_alexa():

    command=alexa_command()
    if "play" in command:
      song=command.replace("play"," ")
      talk("playing" +song)
      pywhatkit.playonyt(song)
    elif "time" in command:
      time=datetime.datetime.now().strftime("%H:%M")
      print(time)
      talk("current time is "+time)
    elif "actor" in command:
      person=command.replace("actor"," ")
      info=wikipedia.summary(person,2)
      print(info)
      talk(info)
    elif "joke" in command:
       talk(pyjokes.get_joke())
      

run_alexa()
