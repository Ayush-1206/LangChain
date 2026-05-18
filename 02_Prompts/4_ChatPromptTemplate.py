from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a {domain} expert.'),
    ('human', 'Explain in simple terms, what is {topic}?'),
])

prompt = chat_template.invoke({"domain": "Cricket", "topic": "LBW rule"})
print(prompt)