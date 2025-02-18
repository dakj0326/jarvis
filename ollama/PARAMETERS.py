# ollama server host address -- Address till ollama som körs på pin
ollama_host='http://192.168.1.101:11434'

# API key -- Verkar inte behövas
API_key = ""

# Which model to use
MODEL = 'qwen:0.5b'

# Memory - max elements in agent conversation history
MEMORY = 100

# System message for model -- system message till modellen som körs på pin
SYSTEM_MSG = {
    'role': 'system',
    'content': 'Build a sentence by appending a single word to the input. English only'
}