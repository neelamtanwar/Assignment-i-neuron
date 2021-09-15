#!/usr/bin/env python
# coding: utf-8

# In[5]:


#printing the pattern
rows = 5
for i in range(0,rows):
    for j in range(0,i+1):
        print('*', end =' ')
    print("\r")
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print('*', end = ' ')
    print("\r")
    


# In[9]:


#Reverse a word
word = input("insert a word")
for char in range(len(word)-1,-1,-1):
    print(word[char],end=" ")


# In[ ]:




