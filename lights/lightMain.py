
import sys
import os

# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from utils import *
from lightList import *


def main(action_list: list):
    """
    Preforms actions on Light(s).
    
    Parameters:
    action_list : list of Action type objects to preform an action with lights
    """
    payload = {}
    for action in action_list:
        payload["entity_id"] = action.get_light().get_id()
        
        #Turn on
        if action.get_state().lower() == "on":
            #Type of light source
            if "light" in action.get_light().get_id():
                url = f"{URL}/api/services/light/turn_on"
                if action.get_light().get_color_comp():
                    payload["rgb_color"] = action.get_color()
                if action.get_light().get_bright_comp():
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






light1 = entry
action1 = l.LightAction(light1, "on", (255, 255, 200), None)
light2 = munken
action2 = l.LightAction(light2, "off", None, None)

main([action2])


