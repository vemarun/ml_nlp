# -*- coding: utf-8 -*-
from nltk import word_tokenize, sent_tokenize,pos_tag

text='Hello! how are you'
print(word_tokenize(text))

word_tokens = word_tokenize(text)
print(pos_tag(word_tokens))

print(sent_tokenize(text))

# Access stopwords for English
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Example text
text = "This is a sample text with some common stopwords."

# Tokenize the text
words = word_tokenize(text)

# Remove stopwords
filtered_words = [word for word in words if word not in stop_words]

print("Original text:", text)
print("Filtered text:", ' '.join(filtered_words))
