import speech_recognition as sr
import pyttsx3
from ConversationalShell import ConversationalShell

class VoiceBridge:
    def __init__(self):
        self.shell = ConversationalShell()
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

    def listen_and_respond(self):
        with sr.Microphone() as source:
            print("[VoiceBridge] Listening...")
            audio = self.recognizer.listen(source)
        try:
            user_input = self.recognizer.recognize_google(audio)
            print("You:", user_input)
            response = self.shell.receive_message(user_input)
            print("Builder:", response)
            self.speaker.say(response)
            self.speaker.runAndWait()
        except Exception as e:
            print("[VoiceBridge ERROR]", str(e))