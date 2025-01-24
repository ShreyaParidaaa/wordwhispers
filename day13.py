#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install spacy')

import spacy

def pos_tagging(sentence):

    nlp = spacy.load("en_core_web_sm")

    # Process the sentence
    doc = nlp(sentence)

    print("Token\tPOS Tag")
    print("-" * 20)
    for token in doc:
        print(f"{token.text}\t{token.pos_}")

sentence = 'NLP is amazing and fun to learn.'

# Perform POS tagging
pos_tagging(sentence)


# In[ ]:




