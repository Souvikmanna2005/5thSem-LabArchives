# Tokenization Using NLTK in Python

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text="Natural Language Processing Is a Branch of Artificial Intelligence"

tokens=word_tokenize(text)

print('Original Text:')
print(text)

print("\nTokens:")
print(tokens)