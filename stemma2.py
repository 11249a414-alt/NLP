from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
new_text = "Is this very important to study while you are studying"
words = word_tokenize (new_text)
for w in words:
     print(ps.stem (w))