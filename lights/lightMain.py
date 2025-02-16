
import sys
import os

# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from utils import *
from lights.lightList import *
from lights.light import *


def main(crude_list: list):
    """
    Preforms actions on Light(s).
    
    Parameters:
    action_list : list of Action type objects to preform an action with lights
    """
    action_list = decrypt(crude_list)
    
    payload = {}
    for action in action_list:
        payload["entity_id"] = action.get_light().get_id()
        
        #Turn on
        if action.get_state().lower() == "on":
            #Type of light source
            if "light" in action.get_light().get_id():
                url = f"{URL}/api/services/light/turn_on"
                if action.get_light().get_color_comp() and action.get_color() != None:
                    payload["rgb_color"] = action.get_color()
                if action.get_light().get_bright_comp() and action.get_brightness() != None:
                    payload["brightness"] = action.get_brightness()
            elif "switch" in action.get_light().get_id():
                url = f"{URL}/api/services/switch/turn_on"
        #Turn off    
        else:
            if "light" in action.get_light().get_id():
                url = f"{URL}/api/services/light/turn_off"
            elif "switch" in action.get_light().get_id():
                url = f"{URL}/api/services/switch/turn_off"
                
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            print(f"Successfully executed {action} command for {payload['entity_id']}.")
        else:
            print(f"Failed to execute {action} command. Status code: {response.status_code}")
            print("Response:", response.text)
            
        payload.clear()


def decrypt(crude_dict: list):
    _light = None
    
    crude_list = crude_dict["actions"][0]
    
    if crude_list[0].lower() == "fonster":
        _light = window
    elif crude_list[0].lower() == "hall":
        _light = entry
    elif crude_list[0].lower() == "korridor":
        _light = hallway
    elif crude_list[0].lower() == "sovrum":
        _light = bedroom
    elif crude_list[0].lower() == "taklampa":
        _light = livingroom
    elif crude_list[0].lower() == "munken":
        _light = munken
        
    print("\n\n", type(crude_list[2]), "\n\n")

    rgb = None
    if crude_list[2] != None:
        rgb = tuple(crude_list[2])
    
    if _light != None:
        return [LightAction(_light, crude_list[1], rgb, crude_list[3])] 
    
    return []
