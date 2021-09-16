#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# In[1]:


#divisible by 7 but not a multuple of 5
df =[]
for x in range (2000,3200):
    if (x%7==0) and (x%5 != 0):
        df.append(str(x))
print(','.join(df))


# In[2]:


#input first name and last name
f_name = input("first name")
l_name =  input ("last name")
print(l_name + ' '+ f_name)


# In[3]:


#volume of sphere
r = float(input("Enter radius"))
volume = 4/3*22/7*(r**3)
print(volume)

