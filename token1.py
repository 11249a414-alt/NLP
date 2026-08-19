from nltk.tokenize import sent_tokenize,word_tokenize
input="i'm yamini. studying BE-CSE."
print(sent_tokenize(input))
print(word_tokenize(input))
for i in sent_tokenize (input):
    print(i)
for i in word_tokenize(input):
    print(i)