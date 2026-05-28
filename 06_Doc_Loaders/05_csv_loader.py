from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='05.1_Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])