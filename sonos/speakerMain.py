
import sys
import os

# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from utils import *
from sonos.speakerList import *
from sonos.speaker import *


def main(crude_list: list):
    
    action_list = dectrypt(crude_list)
    
    
    for action in action_list:
        if action.get_action().lower() == "toggle":
            toggle_speaker(action)
        elif action.get_action().lower() == "shuffle":
            shuffle_speaker(action)
        elif action.get_action().lower() == "volume":
            volume_speaker(action)


def dectrypt(crude_list: list):
    speaker = None
    if crude_list[0].lower() == "sovrum":
        speaker = bedroom
    elif crude_list[0].lower() == "tv_rum":
        speaker = livingroom
    elif crude_list[0].lower() == "sonos_roam":
        speaker = bathroom
    
    if crude_list[1].lower() == "toggle":
        return [SpeakerToggle(speaker, crude_list[2])]
    elif crude_list[1].lower() == "shuffle":
        return [SpeakerShuffle(speaker, crude_list[3])]
    elif crude_list[1].lower() == "volume":
        return [SpeakerVolume(speaker, crude_list[4], crude_list[5], crude_list[6])]
    
    return []

# "List format: [id, action, toggle state ('on'/'off'), shuffle state ('on'/'off'), volume_dynamic, dir, volume]"

def toggle_speaker(action: SpeakerToggle):
    """Toggles a speaker to play or pause"""
    payload = {"entity_id": action.get_speaker().get_id()}
    if action.get_state().lower() == "play":
        url = f"{URL}/api/services/media_player/media_play"
    elif action.get_state().lower() == "pause":
        url = f"{URL}/api/services/media_player/media_pause"
    
    responser(url, payload, action)
        

def shuffle_speaker(action: SpeakerShuffle):
    """Shuffles or unshuffles the playlist"""
    url = f"{URL}/api/services/media_player/shuffle_set"
    payload = {"entity_id": action.get_speaker().get_id(), "shuffle": 'false'}
    if action.get_state().lower() == "on":
        payload["shuffle"] = 'true'

    responser(url, payload, action)


def volume_speaker(action: SpeakerVolume):
    """Changes the volume of a speaker"""
    url = f"{URL}/api/services/media_player/volume_set"
    payload = {"entity_id": action.get_speaker().get_id(), "volume_level": action.get_volume()}
    
    responser(url, payload, action)
    
 
        
def responser(url: str, payload: dict, action):
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print(f"Successfully executed {action} command for {payload['entity_id']}.")
    else:
        print(f"Failed to execute {action} command. Status code: {response.status_code}")
        print("Response:", response.text)

action = SpeakerVolume(bedroom, True, True, 0.1)
main([action])

print(bedroom.get_volume())
