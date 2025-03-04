from tools.toolDefinitions import getTools, functions
from llm.llmAgent import llmAgent
from llm import systemMsgs
from json import loads

def parseToolCalls(funcs):
    for call in funcs:
        try:
            func = functions[call.function.name]
            args = loads(call.function.arguments)
            func(**args)
        except Exception as e:
            print(f'Error calling function: {e}')


# Setup response agent
talkAgent = llmAgent(systemMsgs.get_openai_fast_msg(), False)
toolAgent = llmAgent(systemMsgs.get_openai_lights_msg(), True, getTools())

while True:
    usrInput = input('User: ')

    chatResponse = talkAgent.query(usrInput) # chat response
    print('Jarvis: ', chatResponse)
    
    toolResponse = toolAgent.query(usrInput)
    if toolResponse != None:
        parseToolCalls(toolResponse)