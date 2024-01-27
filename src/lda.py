# -*- coding: utf-8 -*-
from gensim.corpora.dictionary import Dictionary
from gensim import models

document=["The Taj Mahal was designated as a UNESCO World Heritage Site in 1983 for being the jewel of Muslim art in India and one of the universally admired masterpieces of the worlds heritage",
          "It is regarded by many as the best example of Mughal architecture and a symbol of India rich history.",
          "The Taj Mahal attracts 7-8 million visitors a year, and in 2007 it was declared a winner of the New 7 Wonders of the World (2000–2007) initiative."]

tokenized_documents = [doc.split() for doc in document]

# Dictionary: Assigns a unique ID to each word in the corpus, building a vocabulary.
dictionary=Dictionary(tokenized_documents)

# Bag-of-words: Represents each document as a list of (word ID, word frequency) tuples.
corpus=[dictionary.doc2bow(doc) for doc in tokenized_documents]

# Train lda model
lda=models.LdaModel(corpus,3)

for topic in lda.print_topics():
    print(topic)