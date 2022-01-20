import time
from datetime import datetime
import speech_recognition as sr
import pyautogui
from playsound import playsound
from fifteen_api import FifteenAPI



#listen to voice
#check for [Aico] <-
#check for command after Aico
#check what command
#activate command

def speak(voiceInput: str):
    print(voiceInput)
    #aicoVoice.save_to_file(setVoice, voiceInput, "AicoOutput.wav")
    #playsound("AicoOuput.wav")


def command_google(google: str):
    speak("googling. " + google)
    pyautogui.keyDown("alt")
    pyautogui.press("space")
    pyautogui.keyUp("alt")
    time.sleep(1)
    pyautogui.typewrite("www.google.com")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite(google)
    time.sleep(1)
    pyautogui.press("enter")


def command_time(time: str):
    current_time = datetime.now()
    print(current_time)


class Command:
    def __init__(self, command_input: [str], callback):
        self.command_input = command_input
        self.callback = callback

    def match(self, user_input: str):
        for command in self.command_input:

            if user_input.startswith(command):
                self.callback(user_input[len(command):])
                return True

        return False


def command_recognition(command: str):
#   storing versions the speech recognition sees as Aico


    aico = ["ico", "aiko", "aico", "eyeko"]
    command_list = [
        Command(command_input=["please google", "google"], callback=command_google),
        Command(command_input=["what time is it", "what is the time", "what is the date"], callback=command_time),
        ]
    command_input = command.lower().split(" ")
    print(command_input)

#   check where Aico is in the string
    for pos, com in enumerate(command_input):
        if com in aico:

            print("command recognized")
#           check for what command is being called
            for command_class in command_list:

                user_input = " ".join(command_input[pos+1:])
                if result := command_class.match(user_input):
                    print("command found")
                    break




setVoice = "Rise Kujikawa"
startupLine = "testing voice"
aicoVoice = FifteenAPI()
speak(startupLine)

r = sr.Recognizer()
mic = sr.Microphone()


while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        CommandActivation = r.recognize_google(audio)
        print(CommandActivation)
        command_recognition(CommandActivation)

    except sr.UnknownValueError:
        pass