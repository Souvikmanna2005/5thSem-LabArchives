from collections import Counter

# Training sentences
sentences = [
    "I study NLP",
    "I study python",
    "I like NLP"
]

# Combine all sentences
words = " ".join(sentences).lower().split()

# Count each word
word_counts = Counter(words)

# Total number of words
total_words = len(words)

# Calculate unigram probabilities
unigram_prob = {}

for word, count in word_counts.items():
    unigram_prob[word] = count / total_words

print("\nUnigram Probabilities:")
for word, probability in unigram_prob.items():
    print(word, "=", probability)

# Calculate probability of each sentence
print("\nSentence Probabilities:")

for sentence in sentences:
    sentence_words = sentence.lower().split()
    probability = 1

    for word in sentence_words:
        probability *= unigram_prob[word]

    print(sentence, "=", probability)