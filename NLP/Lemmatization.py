import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')


#Input Text
text="The students are studying and playing games."
words=word_tokenize(text)

#Create lemmatizer
lemmatizer=WordNetLemmatizer()
#Perform lemmatization
lemmatized_words=[lemmatizer.lemmatize(word,pos='v') for word in words]

#Display results
print("Original Words::")
print(words)
print("\nAfter Lemmatization::")
print(lemmatized_words)