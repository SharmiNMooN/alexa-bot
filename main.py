import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))
    

listener = sr.Recognizer()
alexa = pyttsx3.init()
voice = alexa.getProperty('voices')
alexa.setProperty('voice', voice[1].id)

change_voice(alexa, "en_US", "VoiceGenderFemale")

def speak(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():

    command = ""
    try:
        with sr.Microphone() as source:
            print("Say something! I'm listening...")
            audio = listener.listen(source)
            print("Voice Listening Done")
            command = listener.recognize_google(audio)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
            
    except:
        pass
    return command
    
def run_command():
    command = take_command()
    print(command)
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)
        print(time)
    

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)
    elif "tell me" in command:
        wiki = command.replace("tell me", "")
        info = wikipedia.summary(wiki, 1)
        print(info)
        speak("according to wikipedia " + info)
    elif "joke" in command:
        speak(pyjokes.get_joke())
        
    elif "date" in command:
        speak("Sry vaiya....I am engagaged in another realationship")
    else:
        speak("I don't understand, But I can search it for you")
        pywhatkit.search(command)
        while True:
            speak("Do you want to search for more?")
            command = take_command()
            if "yes" in command:
                run_command()
                break
            elif "no" in command:
                break

run_command()