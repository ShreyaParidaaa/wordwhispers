#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install nltk')


# In[2]:


import pandas as pd 
import numpy as np 


# In[4]:


df = pd.read_csv('sentiment_analysis.csv')


# In[5]:


df


# In[6]:


df['sentiment'].unique()


# In[7]:


df['sentiment'].value_counts()


# In[8]:


df = df[['text','sentiment']]


# In[9]:


df


# # using Vader and SIA

# In[13]:


nltk.download('vader_lexicon')


# In[14]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


# # Understanding SIA

# In[15]:


sentence = "This movie was amazing, but the acting was a bit disappointing."
sentiment_scores = sia.polarity_scores(sentence)
print(sentiment_scores) 


# In[16]:


def analyze_sentiment_nltk(review):
    score = sia.polarity_scores(review)
    final_score = score['compound']
    if final_score > 0.4:
        return 'positive'
    elif final_score >= -0.3 and final_score <= 0.4:
        return 'neutral'
    else :
        return 'negative'


# In[17]:


df['predicted_sentiment_nltk'] = df['text'].apply(analyze_sentiment_nltk)


# In[18]:


df


# In[19]:


df['prediction_correctness_nltk'] = np.where(df['sentiment']==df['predicted_sentiment_nltk'],1,0)


# In[20]:


df


# In[21]:


df['prediction_correctness_nltk'].value_counts()


# # Using textblob

# In[22]:


get_ipython().system(' pip install textblob')


# In[23]:


from textblob import TextBlob


# In[24]:


def analyze_sentiment_textblob(review):
    blob = TextBlob(review)
    if blob.sentiment.polarity >= 0.4:
        return 'positive'
    elif blob.sentiment.polarity >= -0.3 and blob.sentiment.polarity <= 0.4:
        return 'neutral'
    else : 
        return 'negative'


# In[32]:


analyze_sentiment_textblob('She is very pretty')


# In[33]:


analyze_sentiment_textblob('He uses bad words')


# In[34]:


analyze_sentiment_textblob('Him and her are made for eachother')


# In[36]:


analyze_sentiment_textblob('He uses good words')


# In[27]:


df['predicted_sentiment_textblob'] = df['text'].apply(analyze_sentiment_textblob)


# In[28]:


df['prediction_correctness_textblob'] = np.where(df['sentiment']==df['predicted_sentiment_textblob'],1,0)


# In[29]:


df


# In[30]:


df['prediction_correctness_textblob'].value_counts()


# In[ ]:




