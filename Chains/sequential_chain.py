from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Summarize the following text in 5 bullet points:\n\n{text}",
    input_variables=["text"],
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

# Adapter: take the string output and convert it into {"text": ...}
to_text_input = RunnableLambda(lambda s: {"text": s})

chain = (
    prompt1
    | model
    | parser           # -> string (the detailed report)
    | to_text_input    # -> {"text": "..."}
    | prompt2
    | model
    | parser           # -> string (5-point summary)
)

result = chain.invoke({"topic": "AI education in India"})
print(result)
