
import sys
import os

# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from jarvis_dir import jarvis as j
from lights import lightMain
from sonos import speakerMain

jarvis = j.Jarvis()

while True:
    _input = input("You: ")
    
    if _input.lower() == "exit":
        break
    
    chat_response = jarvis.fast_response(_input)
    print("Jarvis: ", chat_response["message"])
    
    light_response = []
    speaker_response = []
    
    for action in chat_response["needs_commands"]:
        if action.lower() == "light":
            light_response = jarvis.lights_response(_input)
        elif action.lower() == "speaker":
            speaker_response = jarvis.speaker_response(_input)
    
    print("\n\n", speaker_response, "\n", light_response)
    
    if len(light_response) != 0:
        lightMain.main(light_response)
        
    if len(speaker_response) != 0:
        speakerMain.main(speaker_response)
        