from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# ChatPromptTemplate → helps you define chat-style prompts (system, human, AI)
# MessagesPlaceholder → acts as a slot where past messages can be injected

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'), # system → defines AI personality & rules
    MessagesPlaceholder(variable_name='chat_history'), # MessagesPlaceholder → injects conversation memory
    ('human','{query}') # {query} → latest user question
])

chat_history = [] # You need a container to store previous messages. LLMs don’t remember anything automatically
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines()) # Makes conversation persistent. Even after program restarts, AI can continue the conversation

print(chat_history)

# create prompt
prompt = chat_template.invoke({
    'chat_history':chat_history, 
    'query':'Where is my refund'}) 

print(prompt)