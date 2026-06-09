from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain.tools import tool
import requests
from dotenv import load_dotenv  
load_dotenv()

#Tool Creation
@tool
def multiply(a: int, b:int) -> int:
    """Given 2 numbers this tool multiplies that"""
    return a * b


#Tool binding
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm_with_tool = llm.bind_tools([multiply])


query = HumanMessage('can you multiply 3 with 1000')
messages = [query]

#Tool Calling
result = llm_with_tool.invoke(messages)
messages.append(result)

toolCall = result.tool_calls[0]
toolResult = multiply.invoke(toolCall)
messages.append(toolResult)

print(llm.invoke(messages).content)
