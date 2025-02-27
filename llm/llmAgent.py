from ollama import chat, Client
from configHandler import getValue
import openai
import os
from json import loads

class llmAgent:
    """Instantiable object of ollama model. 
       History is optional """
    def __init__(self, systemMsg: dict, model: str, memory: int, llm: str, history = None, returnJson = False, maxTokens = None):
        self.history = history if history != None else self.history = [] # Predefined memory?
        self.returnJson = True if returnJson else self.returnJson = False # Return message as JSON object?
        self.maxTokens = maxTokens if maxTokens != None else self.maxTokens = 500 # Max tokens, for openai
        self.systemMsg = systemMsg
        self.model = model
        self.remote = getValue('ollama_settings', 'remote')
        self.memory = memory
        self.llm = llm

        if self.llm == openai:  # Create openai client
            self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        elif self.remote:   # Create ollama client if llm set to ollama & remote
            self.client = Client(host=getValue('ollama_settings', 'host')) # Create client if set to run remote

    
    def query(self, userPrompt: str):
        usrMsg = {'role': 'user', 'content': userPrompt}
        message = [self.systemMsg, usrMsg]
        if len(self.history) != 0: # Append history to msg if it contains any entries
            message.append(self.history)
        
        self.addHistory(usrMsg) # Append usrMsg to history

        if self.llm == 'openai': # Run if openai configured
            response = self.client.chat.completions.create(
                model = 'self.model',
                messages = message,
                response_format={"type": "json_object"},
                max_tokens = self.maxTokens)
            
            self.addHistory(response['role': 'you', 'content': response['message']['content']])

            if self.returnJson:
                return loads(response.choices[0].message.content) # Return message content as JSON
            return response.choices[0].message.content # Return message content as str
        
        if self.remote: # Run if ollama set to remote
            response = self.client.chat(
            model = self.model,
            messages = message)

            self.addHistory(response['role': 'you', 'content': response['message']['content']])
            return response
        
        else: # Run if ollama set to local
            response = chat(
                model = self.model,
                messages = message)
            
            self.addHistory(response['role': 'you', 'content': response['message']['content']])
            return response
        
    def addHistory(self, msg: dict):    # Add to history while maintinging size
        self.history.append(msg)
        if len(self.history) > self.memory:
            self.history.pop[0]
        

    
