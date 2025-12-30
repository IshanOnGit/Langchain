from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated  # use typing_extensions.Annotated if on older Python

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

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

print(result)                # should be a dict-like object matching Review
print(result["Summary"])
print(result["Sentiment"])
