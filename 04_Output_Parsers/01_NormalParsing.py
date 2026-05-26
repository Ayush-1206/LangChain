from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

chat = ChatHuggingFace(llm=llm)

template1 = ChatPromptTemplate.from_template(
    "Write a detailed report on {topic}"
)

template2 = ChatPromptTemplate.from_template(
    "Write a 5 line summary of the following text:\n{text}"
)

prompt1 = template1.invoke({"topic": "Climate Change"})
result = chat.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
result2 = chat.invoke(prompt2)

print(result2.content)