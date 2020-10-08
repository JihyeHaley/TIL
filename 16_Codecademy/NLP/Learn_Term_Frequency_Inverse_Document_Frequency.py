from preprocessing import preprocess_text
# pip install preprocessing
import pandas as pd

# sample documents
document_1 = "This is a sample sentence!"
document_2 = "This is my second sentence."
document_3 = "Is this my third sentence?"

# corpus of documents
corpus = [document_1, document_2, document_3]

# preprocess documents
processed_corpus = [preprocess_text(doc) for doc in corpus]
print(processed_corpus)