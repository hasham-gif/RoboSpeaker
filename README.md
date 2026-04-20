# RoboSpeaker

A simple text-to-speech program for Windows that mimics Mac's `say` command.

## Features

- Type any text → Computer speaks it out loud
- Type `q` → Exits with "bye bye friend"
- Works completely offline

## Installation
pip install pywin32

## Usage
python test2.py

## Code

from win32com.client import Dispatch

speaker = Dispatch("SAPI.SpVoice")

while True:
    text = input("Enter text to speak (q to quit): ")
    if text == "q":
        speaker.Speak("bye bye friend")
        break
    speaker.Speak(text)

## Mac Version Code

import os

while True:
    x = input("Enter what you want to speak: ")
    if x == "q":
        os.system("say 'bye bye friend'")
        break
    os.system(f"say {x}")
    
## Files

- `test2.py` - Windows version
- `chatRobo.py` - Mac version

## Author

M. Hashaam - First Python Project
