from ollama import chat, Client
from configHandler import getValue

class OllamaAgent:
    """Instantiable object of ollama model. 
       History is optional """
    def __init__(self, systemMsg: dict, model: str, memory: int, history = None):
        if history == None: # Allow for predefined memory
            self.history = []
        else:
            self.history = history
        
        self.systemMsg = systemMsg
        self.model = model
        self.remote = getValue('ollama_settings', 'remote')
        if self.remote: self.client = Client(host=getValue('ollama_settings', 'host')) # Create client if set to run remote
        self.memory = memory
    
    def query(self, userPrompt: str):
        usrMsg = {'role': 'user', 'content': userPrompt}
        message = [self.systemMsg, usrMsg]
        if len(self.history) != 0: # Append history to msg if it contains any entries
            message.append(self.history)

        if self.remote: # Run if set to remote
            response = self.client.chat(
            model = self.model,
            messages = message,)

            self.addHistory(response['role': 'you', 'content': response['message']['content']])
            return response
        
        else: # Run if set to local
            response = chat(
                model = self.model,
                messages = message)
            
            self.addHistory(response['role': 'you', 'content': response['message']['content']])
            return response
        
    def addHistory(self, msg: dict):    # Add to history while maintinging size
        self.history.append(msg)
        if len(self.history) > self.memory:
            self.history.pop[0]
        

    
