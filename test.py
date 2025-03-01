from llm import llmAgent as ai
from llm import systemMsgs
from tools import lightMain
from llm import systemMsgs
from configHandler import getValue

# Setup response agent
responseAgent = ai.llmAgent(systemMsgs.get_openai_fast_msg(),
                            getValue('llm_settings', 'model'),
                            getValue('llm_settings', 'memory'),
                            getValue('llm_settings', 'source'),
                            True)

while True:
    # User in
    usrInput = input('User: ')
    # chat response
    response = responseAgent.query(usrInput)
    print('Jarvis: ', response)