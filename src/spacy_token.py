# -*- coding: utf-8 -*-

import spacy

# https://spacy.io/models fiirst install model using python -m spacy download en_core_web_sm

nlp=spacy.load('en_core_web_sm')

doc1=nlp("Get up early and start your work !")

for token in doc1:
    print([(token.text,token.idx,token.tag_)])