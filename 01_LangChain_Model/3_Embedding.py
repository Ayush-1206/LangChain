#gemini-embedding-001    models/text-embedding-004
 
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions=32)
vector = embeddings.embed_query("Delhi is the capital of India.")

print(str(vector))