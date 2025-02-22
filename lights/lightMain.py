
import sys
import os
import requests
import json
# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from configHelper import getLights, getDictValues, mergeDicts, getValue, getHAheaders

debug = False #Used when payload results is wanted

def main(_input: dict):
    
    actions = dereference_input(_input)
    
    print(actions)
    
    for action in actions:    
        lights = getLights() # Iterera över konfigurerade lampor för att hitta korrekt lampa
        lconf= {}  # Lampans inställningar
        
        for light in lights: #
            values = getDictValues(light)
            if action[0] in values:
                lconf = mergeDicts(light)

                # POST till HA
                payload = {}
                url = getValue('home_assistant_settings', 'url')
                payload['entity_id'] = lconf['ha_id']
                if action[1].lower() == "on": # If state on
                    if lconf['color'] and action[2] != None: payload['rgb_color'] = tuple(action[2]) # Set color if configured
                    if lconf['brightness'] and action[2] != None: payload['brightness'] = action[3] # Set brightness if configured
                    url += lconf['uri_on'] # Append uri
                else: # If state off
                    url += lconf['uri_off']



                # Gammala koden för post men headers hämtas från config.ini
                response = requests.post(url, headers=getHAheaders(), data=json.dumps(payload))

                if debug:
                    print(payload)
                    print(url)
                    
                    if response.status_code == 200:
                        print("Successfully executed: ", action)
                    else:
                        print("Failed to execute:", action, " :: ", {response.status_code})
                        print("Response:", response.text)
                    payload.clear()


def dereference_input(_input: dict):
    """Returns a list of lists with every action"""
    
    print(_input)
    
    if validate_list(_input):
        if _input["actions"][0][0].lower() != "all":
            return _input["actions"]
        
        output = []
        lights = getLights()
        for light in lights:
            output.append([light[1]["ha_id"], _input["actions"][0][1], _input["actions"][0][2], _input["actions"][0][3]])
            
        return output
    else:
        print("System Error: Invalid input\n",
              "    File: lightMain.py\n",
              "    Instance location: dereference_input(_input: dict)\n",
              "    Input: _input = ", _input)

def validate_list(_input: dict):
    """Returns True if the structure of input is correct"""
    if "actions" in _input:
        checklists = []
        lights = getLights()
        actions = _input["actions"]
        
        for i in range(len(_input["actions"])):
            if not isinstance(_input["actions"][i], list):
                return False
            
            checklists.append({"id": False, 
                             "state": False, 
                             "color": False, 
                             "brightness": False})
            # Checks ha_id
            for light in lights:
                if actions[i][0] == light[1]["ha_id"] or actions[i][0] == "all":
                    print(light[1]["ha_id"], actions[i][0])
                    checklists[i]["id"] == True
                    break
            
            # Checks state
            if actions[i][1].lower() == "on" or actions[i][1].lower() == "off":
                checklists[i]["state"] = True
            
            # Checks color
            if isinstance(actions[i][2], list):
                color_state = True
                for color in actions[i][2]:
                    if not (color >= 0 and color <= 255):
                        color_state = False
                
                if color_state:
                    checklists[i]["color"] = True
            if actions[i][2] == None:
                checklists[i]["color"] = True
            
            # Checks brightness
            if isinstance(actions[i][3], int):
                if actions[i][3] >= 0 and actions[i][3] <= 255:
                    checklists[i]["brightness"] = True
            if actions[i][3] == None:
                checklists[i]["brightness"] = True
        
        for checklist in checklists:
            for key, value in checklist.items():
                if not value:
                    print (checklists)
                    return False
        
        return True
    return False