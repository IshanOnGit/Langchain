# NEED OF STRUCTURED OUTPUT
# Raw LLM outputs are hard to parse, unreliable, dangerous in production
# LangChain creates a new model wrapper
# Adds: instructions, output parsing, validation
# model.invoke() → free text
# structured_model.invoke() → validated structure

# This code enforces structured output from a Gemini LLM using a TypedDict schema, ensuring predictable, validated responses suitable for production use.


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated  # use typing_extensions.Annotated if on older Python

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Schema
class Review(TypedDict):
    Summary: Annotated[str, "Give a brief summary of the review"]
    Sentiment: Annotated[str, "Give sentiment of the review (pos/neg/neutral)"]

# Wrap the model with structured output
structured_model = model.with_structured_output(Review)

# Now invoke the *structured* model ❌model.inovke❌  ✅structured_model.invoke✅
result = structured_model.invoke(
    """The hardware is great but the software feels bloated. There are too many 
    pre-installed apps that I can't remove. Also, the UI looks outdated compared 
    to other brands. Hoping for a software update to fix this."""
)

# INTERNALLY 
# LangChain injects schema instructions
# Gemini generates output
# LangChain parses it
# If output doesn’t match schema → retry or error

print(result)    
#Now you can: store it in DB, send to frontend, run logic on it, chain it to another agent            # should be a dict-like object matching Review
print(result["Summary"])
print(result["Sentiment"])

# Where this is used in real applications ?
# This pattern is used for:
# sentiment analysis
# classification
# entity extraction
# form filling
# API generation
# decision-making agents
# Basically: anywhere reliability matters