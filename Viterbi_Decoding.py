import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = input("Enter a sentence: ")

# Tokenize the sentence
tokens = word_tokenize(text)

# POS Tagging
tags = pos_tag(tokens)

print("\nPOS Tags using Viterbi Decoding Concept")
print("-" * 45)

for word, tag in tags:
   print(f"{word:<15} {tag}")