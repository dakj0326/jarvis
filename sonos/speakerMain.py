
import sys
import os

# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from utils import *
from speakerList import *
from speaker import *


def main(action_list: list):
    for action in action_list:
        if action.get_action().lower() == "toggle":
            toggle_speaker(action)


def toggle_speaker(action: SpeakerToggle):
    """Toggles a speaker to play or pause"""
    payload = {"entity_id": action.get_speaker().get_id()}
    if action.get_state().lower() == "play":
        url = f"{URL}/api/services/media_player/media_play"
    elif action.get_state().lower() == "pause":
        url = f"{URL}/api/services/media_player/media_pause"
    
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print(f"Successfully executed {action} command for {payload['entity_id']}.")
    else:
        print(f"Failed to execute {action} command. Status code: {response.status_code}")
        print("Response:", response.text)


action = SpeakerToggle(bedroom, "play")
main([action])
