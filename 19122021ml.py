#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("Uber Drives 2016.csv")


# In[4]:


type(df)


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.dtypes


# In[8]:


temp = pd.DataFrame({"A":["1","2","3"],"B":[11,12,13],"C": ["12-06-2012","13-06-2015","15-06-2017"]})


# In[9]:


temp.dtypes


# In[10]:


temp["C"]= pd.to_datetime(temp["C"])


# In[11]:


temp.dtypes


# Important:::::

# In[12]:


pd.to_datetime(["2016-sep-11","abc"], errors="coerce")


# In[13]:


temp["A"] = pd.to_numeric(temp["A"])


# In[15]:


temp.dtypes


# In[16]:


df.describe()


# In[17]:


df.describe(include = "all")


# In[18]:


df["START*"].value_counts().head()


# In[19]:


df["START*"].value_counts()


# In[20]:


df


# # Selecting

# In[26]:


df.iloc[0:5,0:4]


# In[21]:


bastard = df.iloc[:,:-1]
bastard


# In[22]:


print(df.shape)
print(bastard.shape)


# In[23]:


df.loc[:,"START*"]


# In[24]:


df.loc[:,["START*","STOP*"]]


# In[25]:


df[["START*","STOP*"]]


# In[26]:


df.loc[:,["START*","STOP*"]]
bas = df.loc[:,"START*"]


# In[27]:


tard = df.loc[:,["START*"]]


# In[28]:


type(bas)


# In[29]:


type(tard)


# In[30]:


df.keys()


# In[31]:


df


# # Assignment 1

# In[32]:


df.loc[0:4,["START_DATE*","MILES*"]]


# In[33]:


df[["MILES*"]]>10


# In[34]:


df2 = df.loc[df["MILES*"]>10, : ]
df2 


# In[36]:


df2 = df.loc[df["STOP*"]=="New York", : ]
df2 


# In[37]:


df3 = df.loc[df["START*"].isin(["New York", "Jamaica"]), ["START*","MILES*"]].shape
df3


# In[38]:


df4 = df.loc[df["START*"].isin(["Carry", "Jamaica"]), ["START*","MILES*"]].shape
df4


# In[39]:


df5 = df.loc[(df["MILES*"]>10) & (df["START*"].isin(["New York","Morrisville"]))]
df5


# In[40]:


df6 = df5.reset_index()
#df5
df6

#if you only take out df5 it will show as before i.e., no ordered index value
#if you only take out df6 it will show a new dataframe which has 2 index column 
#one  with the original index value with column name as index and 
#second is order index which is the leftmost


# In[41]:


#df5.reset_index(inplace =  True)
df5.reset_index(inplace = True ,drop = True)
df5

# original dataframe df5 is changed


# # Sorting

# In[43]:


df


# In[47]:


df.sort_values(by = ["MILES*"],ascending=False).head(-1)


# In[51]:


df.sort_values(by=["MILES*"],ascending = True).tail(5)

