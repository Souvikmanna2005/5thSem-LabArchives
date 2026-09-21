import spacy 

nlp=spacy.load("en_core_web_sm")
text='The cats were running much faster than the dogs.'

#process the text
doc=nlp(text)
#Extract the base lemma for each word
lemmatized_words=[token.lemma_ for token in doc]
print('Original Text:',text)
print('Lemmatized: '," ".join(lemmatized_words))