import nltk 

#Download Required Library
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

#Input textual data
text='The students are learning Natural Language Processing.'

#Tokenization
words=nltk.word_tokenize(text)

#POS tagging
pos_tags=nltk.pos_tag(words)

#Display result
print("Original Text:")
print(text)

print("\nPOS Tagged Text:")
for words,tag in pos_tags:
    print(words,"-->",tag)