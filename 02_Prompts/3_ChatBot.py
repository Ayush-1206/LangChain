from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("Enter your prompt (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("AI: " + result.content)

print("\nChat History:", chat_history)