
import openai
import json
import os

class Jarvis:
    def __init__(self):
        self.jarvis =  openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.conversation_history = []
        
    def fast_response(self, _input: str):
        self.conversation_history.append({"role": "user", "content": _input})
        
        response = self.jarvis.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": 
                    "You are Jarvis, a home assitant."
                    "Always respond in valid JSON format with two keys: 'message' and 'needs_commands'."
                    "Give short and direct answers, often calling the user sir, always in english."
                    "You can control speakers and lights in the appartment."
                    "Also, return a list of strings 'needs_commands' containing 'light', 'speaker' or None depending on if my lights or speakers should be altered by my input"},
                {"role": "user", "content": _input}
            ],
            response_format={"type": "json_object"}
        )
        
        response_dict = response.choices[0].message.content  # Extract the response content
        chat_response = json.loads(response_dict)
        
        if len(self.conversation_history) > 20:
            self.conversation_history = self.conversation_history[-10:]
            
        return chat_response
    
    def lights_response(self, _input: str):
        response= self.jarvis.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": 
                    "You will only answer in a structured list called 'actions' changing the state of lights"
                    "Always respond in valid JSON format"
                    "if an element is not specified, leave as None.  if no light is defined, choose id for everyone"
                    "id for window: 'fonster'"
                    "id for entrance: 'hall'"
                    "id for hallway: 'korridor'"
                    "id for bedroom: 'sovrum'"
                    "id for ceiling lamp: 'taklampa'"
                    "id for doughnut lamp: munken"
                    "if for everyone: 'all'"
                    "List format: [id, state ('on'/'off), Tuple (R, G, B), brighness (0-100)]"},
                {"role": "user", "content": _input}
            ],
            response_format={"type": "json_object"},
            max_tokens=100
        )
        
        response_dict = response.choices[0].message.content  # Extract the response content
        chat_response = json.loads(response_dict)
        
        return chat_response
        
    def speaker_response(self, _input: str):
        response= self.jarvis.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": 
                    "You will only answer in a structured list called 'actions' changing the state of speakers"
                    "Always respond in valid JSON format"
                    "if an element is not specified, leave as None. if no speaker is defined, choose id for everyone"
                    "id for tv speakers and livingroom speakers: 'tv_rum'"
                    "id for bedroom: 'sovrum'"
                    "id for bathroom: 'sonos_roam'"
                    "id for everyone: 'all'"
                    "action for play or pause: 'toggle'"
                    "action for volume: 'volume'"
                    "action for shuffle: 'shuffle'"
                    "if no specific wanted volume float is asked:  bool volume_dynamic = True else False"
                    "bool dir = True when wanting to increase volume else False"
                    "if no specific volume float is asked: 'a little' -> volume = 0.1, alot -> volume = 0.25"
                    "List format: [id, action, toggle state ('play'/'pause'), shuffle state ('on'/'off'), volume_dynamic, dir, volume]"},
                {"role": "user", "content": _input}
            ],
            response_format={"type": "json_object"},
            max_tokens=100
        )
        
        response_dict = response.choices[0].message.content  # Extract the response content
        chat_response = json.loads(response_dict)
        return chat_response