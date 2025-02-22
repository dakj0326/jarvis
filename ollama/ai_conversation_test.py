from ollama_agent import OllamaAgent
from configHelper import getValue
import systemMsgs

# AI instanser
model = getValue('ollama_settings', 'model')
memory = getValue('ollama_settings', 'memory')
agents = [OllamaAgent(systemMsgs.SYSTEM_MSG_GENERAL, model, memory),
          OllamaAgent(systemMsgs.SYSTEM_MSG_GENERAL, model, memory)]

# AI bygga mening med varandra
def sendMsg(msg: str, agent: OllamaAgent):
    return agent.query(msg)['message']['content']

Sentence = "I"
i = False
while True:
    print("Agent",int(i), ": ", Sentence)
    Sentence = sendMsg(Sentence, agents[int(i)])
    i = not i

