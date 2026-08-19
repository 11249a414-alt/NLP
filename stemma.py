from nltk.stem import PorterStemmer
ps = PorterStemmer()
example_words = ["study","studies","studying","studied"]
for w in example_words:
    print(ps.stem(w))