from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("better",pos='a'))
print(lemmatizer.lemmatize("happy",pos='a'))