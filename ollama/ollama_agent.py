from ollama import chat, Client
import PARAMETERS

class OllamaAgent:
    def __init__(self, systemMsg: dict, model: str, memory: int):
        self.history = []
        self.systemMsg = systemMsg
        self.model = model
        self.client = Client(host=PARAMETERS.ollama_host)
        self.memory = memory
    
    def query(self, userPrompt: str):
        usrMsg = {'role': 'user', 'content': userPrompt}
        message = [self.systemMsg, usrMsg]
        if len(self.history) != 0:
            if len(self.history) > self.memory: self.history.pop(len(self.history)) # history < memory
            message.append(self.history)

        response = self.client.chat(
            model = self.model,
            messages = message)
        
        return response
    
    