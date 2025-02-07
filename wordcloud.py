#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install wordcloud ')


# In[12]:


import wordcloud


# In[13]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[14]:


text = '''
In this paper, we distinguish between four interconnected notions that recur in the literature on text simplification: clarity, easiness, plainness, and simplicity. While plain language and easy language have both been the subject of standardization efforts, there are few attempts to define text clarity and text simplicity. Indeed, in the definition of plain language, clarity has been favored at the expense of simplicity but is employed as a self-evident notion. Meanwhile, text simplicity suffers from a negative connotation and is more likely to be defined by its antonym, text complexity. In our analysis, we examine the current definitions of plain language and easy language and discuss common definitions of text clarity and text complexity. We propose a model of text simplification that can clarify the transition from specialized texts to plain language texts, and easy language texts. It is our contention that text simplification should be placed in a more general framework of discursive ergonomics.
Keywords: plain language, easy language, clear writing, text clarity, text simplification, discursive ergonomics, discourse and writing, text complexity
Introduction
The movement of opinion known as plain language has gained attention in many countries (Schriver, 2017; Clerc, 2022) and has popularized several notion for identifying what we may call reader-friendly writing. Among these labels, we find four recurring notions: clarity, easiness, plainness, and simplicity. These are semantically close notions that are sometimes employed interchangeably and may generate ambiguity, for example, Naderi et al. (2019) use the phrase plain language to refer to language used for people with disabilities and differentiate it from easy language, which they use for language for people with generic reading difficulties, contrary to Baumert (2016) and Maaß (2020). Moreover, even the current conceptualization of text simplification does not satisfy some specialists (Garbacea et al., 2021).
The goal of this article is to answer these research questions:
How are these notions related and how do they differ?
How can considering these four notions offer a better conceptualization of text simplification?
In fact, much effort has been devoted to developing a standard definition of plain language (Balmford, 2018); similar effort has been made with regard to proposing international standards for easy language (Lindholm and Vanhatalo, 2021). Conversely, there have been few attempts to define text clarity, with the consequence that some confusion persists regarding its meaning (Gracie, 2017). There have been even fewer attempts to define text simplicity, which seems rather defined by its antonym, text complexity. However, text complexity does not have an established definition either (Tolochko and Boomgaarden, 2019).
This paper is structured as follows: First we will discuss the definitions of plain language, easy language, text clarity, and text complexity; then, we will briefly present a modeling of the transition from language for special purposes to plain language and easy language. In this modeling, the tension between complex and simple text is articulated along different aspects of text clarity. Since plain language is an international movement, we will consider the English, French and German languages in our examples
Plain language as clear (and simple) language
In the 2000s, plain language specialists felt the need for a standard definition of this notion. In order to achieve this, the Plain Language Association InterNational formed a working group (James, 2009), which discussed several proposals. Cheek (2010) grouped the existing definitions into three categories. The first category consists of readability tests: These are methods based on objective indicators, such as the number of words per sentence; the second category consists of recommendations on wording to be hosen or avoided, such as word choice, sentence length, and content planning; the third category consists of definitions based on message outcome. The PLAIN working group favored the latter approach (Balmford, 2018). Its definition characterizes plain language as being sufficiently “clear” for a desired effect to occur:1
1) Communication is in plain language if its wording, structure and design are so clear that the intended audience can easily find what they need, understand what they find, and use that information (International Plain Language Federation, 2019)
In the French and German versions of this definition, the wording is slightly different. In German (2), the equivalent of plain language is einfache Sprache “simple language” (Baumert, 2016). Instead, the French label is langage clair “clear language” (Krieg-Planque, 2020). Since a literal translation would create a tautology, the second clear has been deleted (3):
2) Eine Mitteilung ist in einfacher Sprache gehalten, wenn ihre Sprache, ihre Struktur und ihr Design so klar sind, dass die gemeinten Leser*innen relevante Informationen leicht finden, verstehen und anwenden können.
“Communication is considered to be in simple language, if its wording, its structure and its design are so clear that the intended readers can easily find, understand and use the relevant information” (International Plain Language Federation, 2019, translation is ours).
3) Une communication est en langage clair si les mots et les phrases, la structure et la conception permettent au destinataire visé de facilement trouver, comprendre et utiliser l'information dont il a besoin.
“Communication is in clear language if its words and sentences, its structure and design allow the intended recipient to easily find, understand and use the information they need” (International Plain Language Federation, 2019, translation is ours).
Both clarity and simplicity are part of the dictionary meanings of plain (Merriam-Webster, 2022): In fact, they are present in the synonymic pair clear and simple language, which is attested as a paraphrase of plain language (Economic and Social Committee, 1995). However, there has been an evolution over time: according to Ngram Viewer (Michel et al., 2011), the use of this locution peaked in the 1940s and declined from the 1960s onward2. Schriver (2017, p. 345) recalls that initially plain language was indeed described as “simple and direct style,” but this characterization did not incorporate the innovations brought about by information design. Moreover, simplicity has suffered from a negative connotation and has met with opposition (Kimble, 1992b; Coleman, 1998): In fact, this notion is often mentioned in the literature, but one must continually take account of its negative counterpart:
4) Plain language is clear language. It is simple and direct but not simplistic or patronizing (Plainlanguage.gov, 2022).
We can infer that in defining the notion of plainness, clarity has displaced simplicity.
Easy language: when plain is not enough
In the definitions (1–3), the parameter for quantifying clarity is ease. The adjective easy is opposed to difficult and refers to the absence of effort (Merriam-Webster, 2022). Indeed, cognitive psychology has long investigated the relationship between textual comprehension and cognitive effort: The perception of difficulty seems to be related to the relationship between effort and result (Kintsch, 1998, 2018). It is not surprising, then, that ease has become a category of its own: easy language.
The main characteristic of easy language is its target audience, which is people with disabilities. Among the best-known programs is that on easy-to-read information by Inclusion Europe (2009). Inclusion Europe proposes a definition of this type of writing, drafting it in an easy-to-read form. In this definition, a text is easy because it is visually clear and structurally simple:
5) Easy to read is information that is written in a simple way so that people with intellectual disabilities can understand it. It is important to use simple words and sentences. If there are words that are difficult to understand, an explanation is provided. The text needs to be clear to see (…) (Inclusion Europe, 2019).
Here, structural simplicity is used as a proxy for easiness, just as complexity is commonly used as a proxy for difficulty. For example, according to Hansen-Schirra et al. (2020, p. 18) easy language would fit into the extreme end of a difficulty spectrum, with the specialized text at the opposite end. Specialized text and easy language text are contrasted along two parameters: complexity and comprehensibility. The plain language text and the common language text lie between these two opposing poles, along an axis of progressive simplification.
While text simplification for the public has met with opposition, resistance toward simplified forms for people with disabilities goes as far as stigma: For this reason, Maaß (2020) argues for the creation of an intermediate category, Easy Language Plus.
What exactly is text clarity?
Although it is often used as a self-evident notion, the conceptualization of clarity can be problematic (Swiggers, 1987; Meschonnic, 1997; Gracie, 2017). As to professional writing, some authors speak of clear writing (Gunning, 1983; Gottlieb, 1992; Kile, 1992a; Ragins, 2012), others of (text) clarity (Michaelson, 1949; Walton, 1983; De Vries, 2002; Bischof and Eppler, 2011). We will treat these expressions as synonyms.
Among its meanings, the adjective clear is synonymous with transparent, plain, and unmistakable (Merriam-Webster, 2022). Moreover, Emig (1977, p. 126) associates clarity with the avoidance of ambiguity, which she considers a trigger for misunderstanding:
6) Clear writing by definition is writing which signals without ambiguity the nature of conceptual relationships, whether they be coordinate, subordinate, superordinate, causal, or something other.
Coleman (1998, p. 393) contrasts clarity with precision, attributing to the latter the function of avoiding ambiguity:
7) Clarity in fact includes a range of attributes: brief, simple, comprehensible and concise. Precision, on the other hand, refers to an exactness of expression, to an absence of ambiguity, an attempt to reduce contestability.
Beaudet (2001, p. 3) attempts a definition where clarity does not correspond to a set of attributes, but to the aim of the text itself (translation is ours):
8) the clarity of a text produced in the workplace corresponds to its effectiveness and is measured by the materialization, or not, of the action it was intended to provoke.
Among these three definitions, we opt for Beaudet (2001). In fact, Emig's and Coleman's definitions seem problematic to us for two different reasons: On the one hand, as we have argued elsewhere (Vecchiato, forthcoming), a text that is intended to be clear does not necessarily exclude the use of ambiguous expressions—such as a pun—because they can offer an accomplished synthesis of the text's content. Regarding Coleman's definition, on the other hand, we have misgivings about the necessarily “short” nature of a clear text: A text can be reasonably long if more words are needed to adequately explain a concept. Beaudet's definition seems more convincing to us, because the label clear is attributed to a text ex post: In other words, a text is “clear” if it has been understood.
Furthermore (ibid., p. 12), Beaudet emphasizes the dimension of the text's adequacy to the recipient—a dimension we approximate to ergonomics (translation is ours):
9) [C]larity is not a property of thought or language, per se, but the result of the match between the language strategies used and the communication situation.
Beaudet (2001) includes other related concepts in the scope of clarity, such as readability, intelligibility, and coherence. Recently, Labasse (2008) has taken up these concepts in the light of research in cognitive psychology. In his model, clarity or “intelligibility” takes different labels depending on the level of text information processing. At the acquisitive level, that is, the processing of vocabulary and syntax, we will speak of readability; at the logical level, of coherence; and at the figurative level, coinciding with the possibility of constructing a mental image of the text, of representability.
'''


# In[ ]:


single because to make it multiline


# In[15]:


plt.figure(figsize=(10,10))
wordcloud = WordCloud(background_color='beige').generate(text)
plt.imshow(wordcloud) 
plt.axis('off')
plt.show()


# In[19]:


import PIL.Image
import numpy as np


# In[24]:


from PIL import Image
mask = np.array(PIL.Image.open(r'C:\Users\Shreya\Downloads\1234.jpg'))


# In[25]:


mask.shape


# In[26]:


wc = WordCloud(background_color='white', mask=mask)
wc.generate(text)


# In[27]:


plt.imshow(wc)
plt.axis('off')
plt.show()

