from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict       
from dotenv import load_dotenv  
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#Schemas
class Review(TypedDict):
    summary: str
    sentiment: str

#Output Parser
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great but the software feels bloated. there are too many pre-installed apps that I can't remove. Also the UI looks outdated as compared to other brands. Hoping for a software update to fix these issues.
""")

print(result)
print(result['sentiment']) 