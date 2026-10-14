import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4') 
 
def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    
    return synonyms, antonyms

syns, ants = get_synonyms_antonyms("happy")
print("Synonyms:", syns)
print("Antonyms:", ants)
