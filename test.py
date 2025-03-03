from tools.tools import getTools
from llm.llmAgent import llmAgent
from llm import systemMsgs
from configHandler import getValue


# Setup response agent
tools = getTools()
talkAgent = llmAgent(systemMsgs.get_openai_fast_msg())
toolAgent = llmAgent(systemMsgs.get_openai_lights_msg(), tools)

while True:
    # User in
    usrInput = input('User: ')
    # chat response
    chatResponse = talkAgent.query(usrInput)
    toolResponse = toolAgent.query(usrInput)
    print('Jarvis: ', chatResponse)
    #print('Tool:', toolResponse[0].function)


    def callFunc(funcList):
        for f in funcList:
            
            f.name
            f.arguments

