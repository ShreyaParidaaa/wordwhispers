#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def clean_text(text):

    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    return cleaned_text

input_text = 'Hello, World! Welcome to NLP 101.'
cleaned_output = clean_text(input_text)
print(f"Original: {input_text}")
print(f"Cleaned: {cleaned_output}")


# In[ ]:




