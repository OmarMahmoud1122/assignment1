#!/usr/bin/env python
# coding: utf-8

# In[101]:


book1 = open('book1.txt',encoding="utf8")


# In[102]:


book2 = open('book2.txt',encoding="utf8")


# In[103]:


file1 = book1.read().lower().split()


# In[104]:


file2 = book2.read().lower().split()


# In[105]:


words = {'he','she','it','i','we','you','they','am','is','are'}


# In[106]:


intersect = set(file1) & set(file2) 


# In[107]:


print(len(intersect - words))


# In[ ]:




