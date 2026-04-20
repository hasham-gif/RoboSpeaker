from win32com.client import Dispatch

speaker = Dispatch("SAPI.SpVoice")

print("Welcome to chatRobo 1.0. Created by M.Hashaam")

while True:
    x = input("Enter What you want to speak : ")
    
    if x == "q":
        speaker.Speak("bye bye friend")
        break
    
    speaker.Speak(x)