
import sys
import os
from configHelper import getLights

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

    lights = getLights()
    for light in lights:
        if light['alias'] or light[light] == crude_list[0]:
            rgb = None
            if crude_list[2] != None:
                rgb = tuple(crude_list[2])
            action = LightAction(light['alias'], crude_list[1], rgb, crude_list[3])

            payload = {}
            payload["entity_id"] = action.get_light().get_id()
# Gammal kod
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
            #Turn off  = payload:dict = {id}
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