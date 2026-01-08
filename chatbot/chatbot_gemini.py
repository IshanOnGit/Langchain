from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model  = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chat_history = []
# LLMs are stateless. They forget previous messages unless you send them again

#Infinite loop, chatbot keeps running until user inputs(type) exit
while True:
    user_input = input('You: ')     #Takes your message from terminal
    chat_history.append(user_input) #Saves it so AI can remember the conversation
    if user_input == 'exit':
        break   
    result = model.invoke(chat_history) # Sends entire chat history to Gemini. Gemini responds based on previous messages
    chat_history.append(result.content) # Saves AI’s reply for future context
    print("AI: ", result.content)

print(chat_history)