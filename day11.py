#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup

def fetch_webpage_title(url):

    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "Title not found"
        return title
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Test the function
url = 'https://example.com'
webpage_title = fetch_webpage_title(url)
print(f"Webpage Title: {webpage_title}")


# In[ ]:




