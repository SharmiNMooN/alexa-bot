import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Say something! I'm listening...")
        audio = listener.listen(source)
        print("Voice Listening Done")
        text = listener.recognize_google(audio)
        print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    