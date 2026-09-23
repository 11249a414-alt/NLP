import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Read input
sentence = input("Enter a sentence: ")

# Tokenization
tokens = word_tokenize(sentence)

# POS Tagging
tagged_words = pos_tag(tokens)

# Display output
print("\nPart-of-Speech Tagged Sentence")
print("-" * 40)
for word, tag in tagged_words:
  print(f"{word:<15} {tag}")