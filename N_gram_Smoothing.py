import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')
text = input("Enter a text corpus: ").lower()
tokens = word_tokenize(text)
tokens = [word for word in tokens if word.isalpha()]
word_count = Counter(tokens)
V = len(word_count)
N = sum(word_count.values())
print("\nWord\t\tCount\tSmoothed Probability")
print("-" * 50)I love Python
I love NLP
Python is easy
for word, count in word_count.items():
    probability = (count + 1) / (N + V)
    print(f"{word:15}{count:5}\t{probability:.4f}")
