import pywhatkit
import pyttsx3
import speech_recognition as sr
import time
import webbrowser
# def face():
def hello():
    s=pyttsx3.init()
    s.setProperty("rate",150)
    s.say("Hello Amigo, I am V, I am a voice Assistant")
    s.say("How May i help You")
    print("Hello,How May i help You")
    s.runAndWait()
def about():
        s=pyttsx3.init()
        s.setProperty("rate",150)
        s.say("I am just a voice assistant who wants to help you with your tasks, My name is based on character from Cyberpunk 2077")
        s.runAndWait()
def search():
        s=pyttsx3.init()
        s.setProperty("rate",150)
        p=sr.Recognizer()
        p1=sr.Microphone()
        while(1):
            with p1 as source1:
                s.say("Give a keyword to search")
                s.runAndWait()
                # p.pause_threshold = 0.5
                audio1=p.listen(source1)
                try:   
                    time.sleep(3)
                    print("Recognizing")
                    search=p.recognize_google(audio1,language='en-in')
                    print("the command is printed=",search)
                    if('exit search' or 'quit search' in search):
                        print("Stopping Search")
                        break
                    else:
                        s.say("Searching")
                        s.runAndWait()
                        pywhatkit.search(search)
                        time.sleep(15) 
                except:
                    s.say("Would you repeat the word to search again sir")
                    s.runAndWait() 
                    print("Repeat the word again")
def p(speech):
        print("the command is printed=",speech)
s=pyttsx3.init()
s.setProperty("rate",150)
hello()
r=sr.Recognizer()
t=sr.Microphone()
while(1):
    print("The list of options available are:\n1)search\n2)image recognition")
    time.sleep(5)
    with t as source:
        print('Listening')
        s.say("Give a command")
        s.runAndWait()
        # r.pause_threshold = 0.7
        audio=r.listen(source)
        try:
            time.sleep(3)
            print("Recognizing")
            speech=r.recognize_google(audio,language='en-in')
            p(speech)
            if('search' in speech):
                search()
            elif('tell me about yourself' or 'about yourself' in speech):
                about()
            elif('exit voice support' or 'quit voice support' in speech):
                        s.say("Exiting")
                        s.runAndWait()
                        webbrowser.open("http://localhost:8501/")
                        break
            # elif('scan my face' in speech):
            #     face()
        except Exception as e:
            print(e)
            s.say("Say that again sir")
            s.runAndWait()


