from ollama import chat, Client
from os import getenv
from configHandler import getValue, mergeDicts
from json import loads
from dotenv import load_dotenv
import openai

class llmAgent:
    """Instantiable object of llm. """
    def __init__(self, systemMsg: dict, tools = None):
        self.tools = tools
        self.history = []
        self.systemMsg = systemMsg
        self.maxTokens = int(getValue('llm_settings', 'max_tokens'))
        self.model = getValue('llm_settings', 'model')
        self.remote = getValue('ollama_settings', 'remote')
        self.memory = int(getValue('llm_settings', 'memory'))
        self.llm = getValue('llm_settings', 'source')
        
        if self.llm == 'openai':  # Create openai client
            load_dotenv()
            self.client = openai.OpenAI(api_key=getenv('OPENAI_API_KEY'))
        elif self.remote:   # Create ollama client if llm set to ollama & remote
            self.client = Client(host=getValue('ollama_settings', 'host')) # Create client if set to run remote

    
    def query(self, userPrompt: str):
        usrMsg = {'role': 'user', 'content': userPrompt}
        self.addHistory(self.systemMsg)
        self.addHistory(usrMsg) # Append usrMsg to history 

        if self.llm == 'openai': # Run if openai configured
            response = self.client.chat.completions.create(
                model = self.model,
                messages = self.history,
                response_format = {"type": "json_object"},
                tools = self.tools,
                max_tokens = self.maxTokens)
            
            
            if response.choices[0].message.content == None: # Api suger dase
                response.choices[0].message.content = ''

            returnMessage = {'role': response.choices[0].message.role,
                       'content': response.choices[0].message.content}
            
            self.addHistory(returnMessage)
            if self.tools: # Add call to history
                return response.choices[0].message.tool_calls # Return tool call

            try:
                content = loads(response.choices[0].message.content)
                return content['response'] # Return message content response as JSON
            except Exception as e:
                print('Message content not convertable to JSON, returning str: ', e)
            return response.choices[0].message.content # Return message content as str
        
        if self.remote: # Run if ollama set to remote
            response = self.client.chat(
            model = self.model,
            messages = self.history,
            tools = self.tools)

            self.addHistory(response['message'])
            if self.returnCall:
                try:
                    json = loads(response['message']) # Return message content as JSON
                    return json
                except Exception as e:
                    print('llm response not convertable to JSON, returning str: ', e)
            return response['message'] # Return message content as str
        
        else: # Run if ollama set to local
            response = chat(
                model = self.model,
                messages = self.history,
                tools = self.tools)
            
            self.addHistory(response['role': 'you', 'content': response['message']['content']])
            if self.returnCall:
                try:
                    json = loads(response['message']) # Return message content as JSON
                    return json
                except Exception as e:
                    print('llm response not convertable to JSON, returning str: ', e)
            return response['message'] # Return message content as str
        

    def addHistory(self, msg: dict):    # Add to history while maintaining size Måste gö såhär av någon anledning, instanserna delar self.history genom denna funktion, hur vettefan
        self.history.insert(0, msg)
        if len(self.history) > self.memory:
            self.history.pop(-1)