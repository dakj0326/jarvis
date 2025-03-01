from ollama import chat, Client
from os import getenv
from configHandler import getValue
from json import loads
from dotenv import load_dotenv
import openai

class llmAgent:
    """Instantiable object of llm. """
    def __init__(self, systemMsg: dict, model: str, memory: int, llm: str, returnJson = False, tools = None, history = [], maxTokens = None):
        if maxTokens == None: # Use other than configured max tokens?
            self.maxTokens = int(getValue('llm_settings', 'max_tokens'))
        else:
            self.maxTokens = maxTokens

        self.history = history  # Predefined history?
        self.tools = tools  # Tools?
        self.returnJson = returnJson # Return message as JSON object?
        self.systemMsg = systemMsg
        self.model = model
        self.remote = getValue('ollama_settings', 'remote')
        self.memory = int(memory)
        self.llm = llm

        if self.llm == 'openai':  # Create openai client
            load_dotenv()
            self.client = openai.OpenAI(api_key=getenv('OPENAI_API_KEY'))
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
                model = self.model,
                messages = message,
                response_format={"type": "json_object"},
                max_tokens = self.maxTokens,
                tools = self.tools)

            self.addHistory(response.choices[0].message)

            if self.returnJson:
                try:
                    return loads(response.choices[0].message.content) # Return message content as JSON
                except Exception as e:
                    print('llm response not convertable to JSON, returning str: ', e)
            return response.choices[0].message.content # Return message content as str
        
        if self.remote: # Run if ollama set to remote
            response = self.client.chat(
            model = self.model,
            messages = message,
            tools = self.tools)

            self.addHistory(response['role': 'you', 'content': response['message']['content']])
            if self.returnJson:
                try:
                    json = loads(response['message']['content']) # Return message content as JSON
                    return json
                except Exception as e:
                    print('llm response not convertable to JSON, returning str: ', e)
            return response['message']['content'] # Return message content as str
        
        else: # Run if ollama set to local
            response = chat(
                model = self.model,
                messages = message,
                tools = self.tools)
            
            self.addHistory(response['role': 'you', 'content': response['message']['content']])
            if self.returnJson:
                try:
                    json = loads(response['message']['content']) # Return message content as JSON
                    return json
                except Exception as e:
                    print('llm response not convertable to JSON, returning str: ', e)
            return response['message']['content'] # Return message content as str
        
    def addHistory(self, msg: dict):    # Add to history while maintaining size
        self.history.append(msg)
        if len(self.history) > self.memory:
            self.history.pop[0]