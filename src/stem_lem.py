# -*- coding: utf-8 -*-

from nltk.stem import SnowballStemmer

snowball=SnowballStemmer("english")

print(snowball.stem("running"))
print(snowball.stem("cats"))
print(snowball.stem("completion"))
print(snowball.stem("mice"))

# Lemmatization

from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

print(lemmatizer.lemmatize("completion"))
print(lemmatizer.lemmatize("mice"))