from ollama_agent import OllamaAgent
import PARAMETERS

# AI instanser
agents = [OllamaAgent(PARAMETERS.SYSTEM_MSG, PARAMETERS.MODEL, PARAMETERS.MEMORY),
          OllamaAgent(PARAMETERS.SYSTEM_MSG, PARAMETERS.MODEL, PARAMETERS.MEMORY)]

# AI bygga mening med varandra
def sendMsg(msg: str, agent: OllamaAgent):
    return agent.query(msg)['message']['content']

Sentence = "I"
i = False
while True:
    print("Agent",int(i), ": ", Sentence)
    Sentence = sendMsg(Sentence, agents[int(i)])
    i = not i

