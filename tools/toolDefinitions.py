from configHandler import getLightNames
from tools.setLights import setLights

# Dict of all available functions
functions = {
    'setLights': setLights
}

def getTools():
    return [{
        "type": "function",
        "function": {
            "name": "setLights",
            "description": "Sets the properties of lights. The available IDS are: " + getLightNames(),
            "parameters": {
                "type": "object",
                    "properties": {
                    "id": {
                        "type": "string",
                        "description": "The id of the light to be altered."
                    },
                    "state": {
                        "type": "boolean",
                        "description": "The on/off state of the light"
                    },
                    "color": {
                        "type": "array",
                        "description": "The RGB color value of the light represented as the aray [R, G, B], each element is an integer and have a range of 0-255",
                        "items": {
                            "type": "number"
                        }
                    },
                    "brightness": {
                        "type": "number",
                        "description": "The brightness of the light, takes a value in the range 0-255"
                    },
                },
                "required": ["id", "state", "color", "brightness"]
            }
        }
    }]