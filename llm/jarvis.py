
import openai
import json
import os

class Jarvis:
    def __init__(self):
        self.jarvis =  openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.conversation_history = []
        self.conversation_context = []
        
    def fast_response(self, _input: str):
        self.conversation_history.append({"role": "user", "content": _input})
        self.conversation_context.append({"role": "user", "content": _input})
        response = self.jarvis.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": 
                    "You are Jarvis, a home assitant."
                    "Always respond in valid JSON format with two keys: 'message' and 'needs_commands'."
                    "Give short and direct answers, often calling the user sir, always in english."
                    "You can control speakers and lights to the appartment."
                    "Also, return a list of strings 'needs_commands' containing 'light', 'speaker' or None depending on if my lights or speakers should be altered by my input"
                    "Do not return 'light' and/or 'speaker' if you ask if they should be alterd."
                    "Only return 'light' and/or 'speaker' if you or the user states they should be altered without a question"
                    "If the word 'light' or 'speaker' is mentioned in a question, DO NOT return 'light' or 'speaker'"}
            ] + self.conversation_history,
            response_format={"type": "json_object"}
        )
        
        response_dict = response.choices[0].message.content  # Extract the response content
        chat_response = json.loads(response_dict)
        
        self.conversation_history.append({"role": "assistant", "content": chat_response["message"]})
        self.conversation_context.append({"role": "assistant", "content": chat_response["message"]})
        
        if len(self.conversation_history) > 12:
            self.conversation_history = self.conversation_history[-12:]
        if len(self.conversation_context) > 8:
            self.conversation_context = self.conversation_context[-8:]
            
        return chat_response
    
    def lights_response(self):
        response= self.jarvis.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content":
                    "You will only answer in a structured list (not a dictionary) called 'actions' changing the state of lights"
                    "Always respond in valid JSON format"
                    "if asked for 'normal light' turn brightness to 255 and color to (255, 160, 60)"
                    "if an element is not specified, leave as None.  if no light is defined, choose id for everyone" # TODO element = Nnne blir problem. Program kraschar lös på annat vis.
                    "id for window: 'fonster'"
                    "id for entrance: 'hall'"
                    "id for hallway: 'korridor'"
                    "id for bedroom: 'sovrum'"
                    "id for ceiling lamp: 'taklampa'"
                    "id for doughnut lamp: munken"
                    "if for everyone: 'all'"
                    "List format: [id, state ('on'/'off), Tuple (R, G, B), brighness int (0-255)]"}
            ] + self.conversation_context,
            response_format={"type": "json_object"},
            max_tokens=100
        )
        
        response_dict = response.choices[0].message.content  # Extract the response content
        chat_response = json.loads(response_dict)
        
        return chat_response
        
    def speaker_response(self):
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
            ] + self.conversation_context,
            response_format={"type": "json_object"},
            max_tokens=100
        )
        
        response_dict = response.choices[0].message.content  # Extract the response content
        chat_response = json.loads(response_dict)
        return chat_response