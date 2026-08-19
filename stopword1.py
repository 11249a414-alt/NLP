from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
input="hey,i am in dell lab . "
stop_words=set(stopwords.words("english"))
words=word_tokenize(input)
filtered_sentence=[]
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)