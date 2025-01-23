#!/usr/bin/env python
# coding: utf-8

# # Day 1

# # Importing the data

# In[ ]:


import pandas as pd 
import numpy as np 


# In[2]:


df = pd.read_csv('bbc_data.csv')


# In[3]:


df


# In[5]:


df['labels'].unique()


# In[6]:


df['labels'].nunique()


# In[7]:


df['data'].nunique()


# In[8]:


df[['data','labels']].drop_duplicates()


# In[9]:


df.isna().sum()


# In[10]:


df['labels'].value_counts()


# In[11]:


l = [1,2.,1,8,9]


# In[12]:


dir(l)


# In[13]:


dir(df)


# # Day 2

# # Preparing the data
# #Converting all the text column to lower case

# In[36]:


df


# In[15]:


df['data'] = df['data'].str.lower()


# In[16]:


df


# # Import spacy for other text cleaning purpose 

# In[17]:


get_ipython().system(' pip install spacy ')


# In[20]:


get_ipython().system(' python -m spacy download en_core_web_sm')


# In[21]:


import spacy
nlp = spacy.load('en_core_web_sm')
print(nlp)


# In[22]:


#Remove punctuations


# In[23]:


df['data'] = df['data'].str.replace(',', ' ')
df['data'] = df['data'].str.replace('.', ' ')
df['data'] = df['data'].str.replace('-', ' ')
df['data'] = df['data'].str.replace('"', ' ')
df['data'] = df['data'].str.replace('  ',' ')


# In[24]:


df


# # Remove stop words

# In[26]:


nlp.Defaults.stop_words


# In[27]:


stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 
              'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but',
               'by', 'can', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing',
               'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn',
               "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his',
               'how', 'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me',
               'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'now', 'o', 'of',
               'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan',
               "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that',
               "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through',
               'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what',
               'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y',
               'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']


# In[28]:


def stop_word_removal(text):
    tokens = text.split(' ')
    words_without_stopwords = [x for x in tokens if x not in stop_words]
    final_sentence = ' '.join(words_without_stopwords)
    return final_sentence


# In[29]:


df


# In[30]:


df['clean_data'] = df['data'].apply(stop_word_removal)


# In[31]:


df


# # Get the vector embeddings

# In[33]:


def get_embeddings(text):
    doc = nlp(text)
    return doc.vector


# In[34]:


df["embeddings"] = df["clean_data"].apply(get_embeddings)


# In[35]:


df


# In[37]:


print(f'{df["clean_data"][0]} \n\n\n {df["embeddings"][0]}')


# In[38]:


df["embeddings"][0].shape


# # Day3

# # Encode the classes

# In[39]:


classes = df['labels'].unique()


# In[40]:


classes


# In[41]:


from sklearn.preprocessing import LabelEncoder


# In[42]:


le = LabelEncoder()
le.fit(classes)


# In[43]:


df['Encoded_labels'] = le.transform(df['labels'])


# In[44]:


df.tail()


# In[45]:


pd.set_option('display.max_colwidth',300)


# In[46]:


df[['Encoded_labels','labels']].drop_duplicates()


# # Get the training data and testing data

# In[47]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


X = np.vstack(df["embeddings"].values)
y = df["Encoded_labels"]


# # Choose any Classifier model

# In[48]:


# Create a model object
model = RandomForestClassifier(random_state=42)


# In[49]:


from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)


# In[50]:


# Print the cross-validation scores
print(scores)
print(f"Mean CV accuracy: {np.mean(scores)}")


# # Choosing a different classifier model

# In[51]:


from sklearn.tree import DecisionTreeClassifier  
model2= DecisionTreeClassifier(criterion='gini', random_state=42)  


# In[52]:


scores = cross_val_score(model2, X, y, cv=5)
print(scores)
print(f"Mean CV accuracy: {np.mean(scores)}")


# In[53]:


from sklearn.neighbors import KNeighborsClassifier
model3 = KNeighborsClassifier(n_neighbors=11,)


# In[54]:


scores = cross_val_score(model3, X, y, cv=5)
print(scores)
print(f"Mean CV accuracy: {np.mean(scores)}")


# In[ ]:




