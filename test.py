from tools.tools import getTools
from llm.llmAgent import llmAgent
from llm import systemMsgs
import json


# Setup response agent
tools = getTools()
talkAgent = llmAgent(systemMsgs.get_openai_fast_msg(), False)
toolAgent = llmAgent(systemMsgs.get_openai_lights_msg(), True, tools)

def parseFunc(funcList):
    for name, args in enumerate(funcList):
        print(f'tool {name}: {args} ')


while True:
    # User in
    usrInput = input('User: ')
    # chat response
    chatResponse = talkAgent.query(usrInput)
    toolResponse = toolAgent.query(usrInput)
    print('Jarvis: ', chatResponse)
    print(f'Tool: {toolResponse}')
    if toolResponse != None:
        parseFunc(toolResponse)


