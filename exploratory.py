#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:/Users/DELL/Downloads/supermarket_sales - Sheet1.csv")
data.head()


# In[3]:


data.isnull().sum()


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


#checking number of rows and columns
print("Dataset contains {} row and {} colums".format(data.shape[0],data.shape[1]))


# In[7]:


#the countplot is used to represent the count of observation present in the categorical variable
plt.figure(figsize=(14,6))
plt.style.use('fivethirtyeight')
ax=sns.countplot('Gender',data=data,palette='copper')
ax.set_xlabel(xlabel="Gender",fontsize=18)
ax.set_ylabel(ylabel="Gender count",fontsize=18)
ax.set_title(label="Gender count in supermarket",fontsize=20)
plt.show()


# In[8]:


#groupby is used for grouping the data according to the categories 
data.groupby(['Gender']).agg({'Total':'sum'})


# In[9]:


#grammers of graphics
plt.style.use('ggplot')
plt.figure(figsize=(14,6))
ax=sns.countplot(x='Customer type',data=data,palette="rocket_r")
ax.set_title("type ofcustomers",fontsize=25)
ax.set_xlabel("Customer type",fontsize=16)
ax.set_ylabel("customer count",fontsize=16)


# In[10]:


data.groupby(['Customer type']).agg({'Total':'sum'})


# In[11]:


plt.figure(figsize=(14,6))
plt.style.use('classic')
ax=sns.countplot(x="Customer type",hue="Branch",data=data,palette="rocket_r")
ax.set_title(label="Customer type in different branch",fontsize=2
ax.set_xlabel(xlabel="Branches",fontsize=16)
ax.set_ylabel(ylabel="Customer count",fontsize=16)


# In[12]:


plt.figure(figsize=(14,6))
ax=sns.countplot(x="Payment",data=data,palette="tab20")
ax.set_title(label="Payment methods of customers",fontsize=25)
ax.set_xlabel(xlabel="Payment method",fontsize=16)
ax.set_ylabel(ylabel="Customer Count",fontsize=16)


# In[13]:


plt.figure(figsize=(14,6))
plt.style.use('classic')
ax=sns.countplot(x="Payment",hue="Branch",data=data,palette="tab20")
ax.set_title(label="Payment distribution in all branches",fontsize=25)
ax.set_xlabel(xlabel="Payment method",fontsize=16)
ax.set_ylabel(ylabel="People count",fontsize=16)


# In[14]:


#this plot represents the minimum maximum median first and third quartile in the dataset
plt.figure(figsize=(14,6))
ax=sns.boxplot(x="Branch",y="Rating",data=data,palette="RdYlBu")
ax.set_title("Rating distribution between branches",fontsize=25)
ax.set_xlabel(xlabel="Branches,fontsize=16")
ax.set_ylabel(ylabel="Rating distribution",fontsize=16)


# In[15]:


#a lineplot is a graph that shows frequency of data along a number line
data["Time"]=pd.to_datetime(data["Time"])
data["Hour"]=(data["Time"]).dt.hour
plt.figure(figsize=(14,6))
plt.style.use('classic')
SalesTime=sns.lineplot(x="Hour",y="Quantity",data=data).set_title("product sales per Hour")


# In[16]:



plt.figure(figsize=(14,6))
plt.style.use('classic')
rating_vs_sales=sns.lineplot(x="Total",y="Rating",data=data)


# In[17]:


#here we can se that the average sales of different lines of products
plt.figure(figsize=(14,6))
plt.style.use('classic')
ax=sns.boxenplot(x="Quantity",y="Product line",data=data,)
ax.set_title(label="Average sales of different lines of products",fontsize=25)
ax.set_xlabel(xlabel="Quantity Sales",fontsize=16)
ax.set_ylabel(ylabel="Product Line",fontsize=16)


# In[18]:


#here we can see the top sold products 
plt.figure(figsize=(14,6))
ax=sns.countplot(y='Product line',data=data, order=data['Product line'].value_counts().index)
ax.set_title(label="Sales count of products",fontsize=25)
ax.set_xlabel(xlabel="Sales count",fontsize=16)
ax.set_ylabel(ylabel="Product Line",fontsize=16)


# In[19]:


plt.figure(figsize=(14,6))
plt.style.use('classic')
ax=sns.boxenplot(y="Product line",x="Total",data=data)
ax.set_title(label="Total sales of product",fontsize=25)
ax.set_xlabel(xlabel="Total Sales",fontsize=16)
ax.set_ylabel(ylabel="Product Line",fontsize=16)


# In[20]:


plt.figure(figsize=(14,6))
plt.style.use('classic')
ax=sns.boxenplot(y="Product line",x="Rating",data=data)
ax.set_title(label="Average rating of product line",fontsize=25)
ax.set_xlabel("Rating",fontsize=16)
ax.set_ylabel("Product Line",fontsize=16)


# In[21]:



plt.style.use('classic')
plt.figure(figsize=(14,6))
ax=sns.stripplot(y="Product line", x="Total",hue="Gender",data=data)
ax.set_title(label="product sales on the basic of gender")
ax.set_xlabel(xlabel="Total sales of products")
ax.set_ylabel(ylabel="Product Line")


# In[23]:


plt.figure(figsize=(14,6))
plt.style.use('classic')
ax=sns.relplot(y="Product line",x="gross income",data=data
ax.set_title(label="Products and Gross income")
ax.set_xlabel(xlabel="Total gross income")
ax.set_ylabel(ylabel="Product line")


# In[25]:


data=np.random.randint(low=1,high=100,size=(10,10))
print("The data to be plotted:\n")
print(data)
hm=sns.heatmap(data=data)
plt.show()


# In[26]:


data=np.random.randint(low=1,high=100,size=(10,10))
vmin=30
vmax=70
hm=sns.heatmap(data=data,vmin=vmin,vmax=vmax)
plt.show()


# In[29]:


data=np.random.randint(low=1,high=100,size=(10,10))
cmap='tab20'
hm=sns.heatmap(data=data,cmap=cmap)
plt.show()


# In[30]:


data=np.random.randint(low=1,high=100,size=(10,10))
cmap='tab20'
center=0
hm=sns.heatmap(data=data,cmap=cmap,center=center)
plt.show()


# In[31]:


data=np.random.randint(low=1,high=100,size=(10,10))
annot=True
hm=sns.heatmap(data=data,annot=annot)
plt.show()


# In[32]:


data=np.random.randint(low=1,high=100,size=(10,10))
linewidths=2
linecolor="yellow"
hm=sns.heatmap(data=data,linewidths=linewidths,linecolor=linecolor)
plt.show()


# In[33]:


data=np.random.randint(low=1,high=100,size=(10,10))
cbar=False
hm=sns.heatmap(data=data,cbar=cbar)
plt.show()


# In[34]:


data=np.random.randint(low=1,high=100,size=(10,10))
xticklabels=False
yticklabels=False
hm=sns.heatmap(data=data,xticklabels=xticklabels,yticklabels=yticklabels)
plt.show()


# In[ ]:




