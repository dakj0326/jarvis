import sys
import os

# Includes path to parent directiry
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from utils import *
from configHelper import getLights, getDictValues, mergeDicts, getValue

#crude_list = [] # Test
#crude_list = ['fonster', 1, [100, 100, 100], 100]
#print('in: ', crude_list)

def main(crude_list: list):
    lights = getLights() # Iterera över konfigurerade lampor för att hitta korrekt lampa
    lconf= {}  # Lampans inställningar
    for light, i in zip(lights, range(len(lights))): #
        values = getDictValues(light)
        if crude_list[0] in values:
            lconf = mergeDicts(light)

            # POST till HA
            payload = {}
            url = getValue('home_assistant_settings', 'url')
            payload['entity_id'] = lconf['alias']
            if crude_list[1]: # If state on
                if lconf['color']: payload['rbg_color'] = tuple(crude_list[2]) # Set color if configured
                if lconf['brightness']: payload['brightness'] = crude_list[3] # Set brightness if configured
                url += lconf['uri_on'] # Append uri
            else: # If state off
                url += lconf['uri_off']

            #print(payload)
            #print(url)

            # Gammal kod
            response = requests.post(url, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                print("Successfully executed: ", crude_list)
            else:
                print("Failed to execute:", crude_list, " :: ", {response.status_code})
                print("Response:", response.text)
            payload.clear()