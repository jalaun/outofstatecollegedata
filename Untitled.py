#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install pandas


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Joshk\Downloads\College_Data.csv')

#uses matplotlib to generate a graph with a figsize of (10,6). A larger figsize would increase the width and height of the graph.
plt.figure(figsize=(10, 6))
#generates a historgram from the outstate column of the inputted data csv. Bins are the bars, more bins represents more bars of data
df['Outstate'].hist(bins=20, edgecolor='black')
plt.title('Distribution of Out-of-State Tuition Costs')
plt.xlabel('Out-of-State Tuition')
plt.ylabel('Number of Universities')
plt.show()


# In[9]:


total_universities = len(df)
print(len(df))


# In[ ]:




