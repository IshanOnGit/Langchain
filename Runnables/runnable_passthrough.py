# RunnablePassthrough in LangChain
# RunnablePassthrough is the simplest runnable that just returns the input as-is, without doing anything to it.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# Generte the joke
joke_generator_chain = RunnableSequence(prompt1, model, parser)

# Parallel processing of the joke
parallelChain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_generator_chain, parallelChain)

result=final_chain.invoke({'topic':'white'})
print['joke' : (result)]
print['explanation': (result)]
