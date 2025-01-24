#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install wordcloud')


# In[10]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text, output_filename):
    """
    Generate a word cloud from the given text and save it as an image file.

    Args:
        text (str): Input text to generate the word cloud.
        output_filename (str): Name of the file to save the generated word cloud.
    """
    # Create a WordCloud object with specified dimensions and background color
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Save the generated word cloud to a file
    wordcloud.to_file(output_filename)

    # Display the word cloud using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Input text for the WordCloud
text = 'Technology is so amazing'

# Output filename for the WordCloud image
output_filename = 'wordcloud.png'

# Generate and save the WordCloud
generate_wordcloud(text, output_filename)

print(f"WordCloud saved as {output_filename}")


# In[ ]:




