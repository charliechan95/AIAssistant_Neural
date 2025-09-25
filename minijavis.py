import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia 
import webbrowser



listener = sr.Recognizer()




#def talk(text):
   # machine.say(text)
#machine.runAndWait()

def input_instruction():

    global instruction
    r = sr.Recognizer()




    try:
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 0.7
            audio = r.listen(source)

            query = r.recognize_google(audio)
            query = query.lower()
            if "Jarvis" in query:
                query = query.replace('Jarvis', ' ')
            print(query)

    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query
      
def talk(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1.0)

   # for index, voice in enumerate(voices):
      #  print(f"Voice {index}:")
       # print(f" - ID: {voice.id}")
      #  print(f" - Name: {voice.name}")
     #   print(f" - Languages: {voice.languages}")
     #  print(f" - Gender: {voice.gender}")
     #   print(f" - Age: {voice.age}")
     #  print()
    
    engine.say(audio)
    engine.runAndWait()


def hello():
    talk("Hello, I am your virtual assistant, how can I help you?")

def tellday():
    day = datetime.datetime.today().weekday()
    Day_Dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    if day in Day_Dict.keys():
        day_of_the_week = Day_Dict[day]
        print(day_of_the_week)
        talk("The day is " + day_of_the_week)


def telltime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    talk("The time is sir" + hour + "Hours and" + min + "Minutes")

def play_Jarvis():
    hello() 
    
    while True:
    
        instruction = input_instruction()
        print(instruction)

    

        if "play" in instruction:
            song = instruction.replace('play', "")
            talk("playing" + song)
            pywhatkit.playonyt(song)
            continue
        elif "what day it is" in instruction:
            talk(tellday())
            continue
        elif "what time is it now" in instruction:
            talk(telltime())
            continue


       
        

        elif 'how are you' in instruction:
            talk('i am fine, how about you')
            continue
        elif 'what is your name' in instruction:
            talk('i am Javis, nice to meet you!')
            continue
        elif 'who is' in instruction:
            person = instruction.replace('who is', "")
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
            continue
        elif 'bye' in instruction:
            talk('bye bye, have a nice day!')
            exit()

        else:
            talk('please repeat that again')
            talk('I did not understand, please say that again')
        



play_Jarvis()
