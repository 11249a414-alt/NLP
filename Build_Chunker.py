import nltk
from nltk.tokenize import word_tokenize
# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Input sentence
sentence = input("Enter a sentence: ")
# Tokenization
tokens = word_tokenize(sentence)
# POS Tagging
tagged_words = nltk.pos_tag(tokens)
# Grammar Rules
grammar = r"""
NP: {<DT>?<JJ>*<NN.*>+}
VP: {<VB.*><DT>?<JJ>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)
print("\nPOS Tagged Sentence")
print(tagged_words)
print("\nChunk Tree")
print(chunk_tree)
# Display graphical parse tree
chunk_tree.draw()