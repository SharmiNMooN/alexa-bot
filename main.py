import speech_recognition as sr
import pyttsx3
import datetime

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

    try:
        with sr.Microphone() as source:
            print("Say something! I'm listening...")
            audio = listener.listen(source)
            print("Voice Listening Done")
            command = listener.recognize_google(audio)
            command = command.lower()
            if "alexa" in command:
                print(command)
            
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    return command
    
def run_command():
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)
        print(time)
    
run_command()

