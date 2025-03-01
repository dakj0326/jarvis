# GPT tool calling
tools = [{
    "type": "function",
    "function": {
        "name": "setLights",
        "description": "Sets the properties of lights.",
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
                    "type": "Tuple(int, int, int)",
                    "description": "The RGB color value of the light represented as the tuple (R, G, B), each integer have a range of 0-255"
                },
                "brightness": {
                    "type": "int",
                    "description": "The brightness of the light, takes a value in the range 0-255"
                }
            },
            "required": [
                "id"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]