# RunnableParallel lets you run multiple tasks at the same time and get all their results together.
# It’s useful when you want to ask the LLM or tools multiple things at once.


from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence

from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a linkedin post in 50 words about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'LinkedIn' : RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic': 'AI'})
print(result['tweet'])
print(result['LinkedIn'])