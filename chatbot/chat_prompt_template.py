from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'LBW'})

print(prompt)

#' chatPromptTemplate ' is used to create dynamic templates. It is used for multi-turn conversations(to fit multiple placeholders in messages)