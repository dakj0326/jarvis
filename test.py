from llm import llmAgent as ai
from llm import systemMsgs
from functions import functions
from llm import systemMsgs
from configHandler import getValue

# Setup response agent
responseAgent = ai.llmAgent(systemMsgs.get_openai_fast_msg(),
                            getValue('llm_settings', 'model'),
                            getValue('llm_settings', 'memory'),
                            getValue('llm_settings', 'source'),
                            True)

# Setup tool calling agent
toolCaller = ai.llmAgent(systemMsgs.get_openai_lights_msg,
                            getValue('llm_settings', 'model'),
                            getValue('llm_settings', 'memory'),
                            getValue('llm_settings', 'source'),
                            True,
                            functions.functions)

while True:
    # User in
    usrInput = input('User: ')
    # chat response
    response = responseAgent.query(usrInput)
    print('Jarvis: ', response)

    # Tool call
    response = toolCaller = toolCaller.query(usrInput)
    print('tool call: ', response)