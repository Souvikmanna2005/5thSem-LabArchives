import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')

#input text
text='The students are studying and playing games'
#tokenization
words=word_tokenize(text)
#create stemmer
stemmer=PorterStemmer()
#perform stemming
stemmed_words=[stemmer.stem(word) for word in words]
#display results
print('Original word:')
print(words)
print('\nAfter Stemming:')
print(stemmed_words)