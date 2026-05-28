from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='03.1_books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

for document in docs:
    print(document.metadata)