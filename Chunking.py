import nltk
from nltk.tokenize import word_tokenize
# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Read input
sentence = input("Enter a sentence: ")
# Tokenization
tokens = word_tokenize(sentence)
# POS Tagging
tagged = nltk.pos_tag(tokens)
# Grammar for Noun Phrase
grammar = r"""
NP: {<DT>?<JJ>*<NN.*>+}
"""
# Chunk Parser
chunk_parser = nltk.RegexpParser(grammar)
# Parse the tagged sentence
chunk_tree = chunk_parser.parse(tagged)
print("\nPOS Tagged Sentence")
print(tagged)
print("\nChunk Tree")
print(chunk_tree)
# Display graphical tree
chunk_tree.draw()