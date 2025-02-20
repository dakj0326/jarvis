
import sys
import os
import requests
import json
# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from configHelper import getLights, getDictValues, mergeDicts, getValue, getHAheaders


def main(_input: list):
    
    actions = dereference_input(_input)
    
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

                print(payload)
                print(url)


                # Gammala koden för post men headers hämtas från config.ini
                response = requests.post(url, headers=getHAheaders(), data=json.dumps(payload))


            # Gammala koden för post men headers hämtas från config.ini
            response = requests.post(url, headers=getHAheaders(), data=json.dumps(payload))

            if response.status_code == 200:
                print("Successfully executed: ", action)
            else:
                print("Failed to execute:", action, " :: ", {response.status_code})
                print("Response:", response.text)
            payload.clear()
            break


def dereference_input(_input: list):
    if _input["actions"][0][0].lower() != "all":
        return _input["actions"]
    
    output = []
    lights = getLights()
    for light in lights:
        output.append([light["ha_id"], _input[1], _input[2], _input[3]])
        
    return output