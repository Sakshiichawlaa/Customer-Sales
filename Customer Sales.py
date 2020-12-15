#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.__version__
#enable IPython to display matplotlib graphs.
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


sales=pd.read_csv('http://pbpython.com/extras/sample-salesv2.csv', parse_dates=['date'])
sales.head()


# In[3]:


sales.describe()


# In[4]:


#We can tell that customers on average purchases 10.3 items per transaction
#The average cost of the transaction was $579.84
#It is also easy to see the min and max so you understand the range of the data


# In[5]:


#If we want we can look at a single column as well:

sales['unit price'].describe()


# In[6]:


#I can see that my average price is $56.18 but it ranges from $10.06 to $99.97.

#I am showing the output of dtypes so that you can see that the date column is a datetime field.


# In[7]:


sales.dtypes


# In[8]:


#First remove some columns to make additional analysis easier.

customers = sales[['name','ext price','date']]
customers.head()


# In[9]:


#This representation has multiple lines for each customer. 
#In order to understand purchasing patterns, let’s group all the customers by name.
#We can also look at the number of entries per customer to get an idea for the distribution.
customer_group = customers.groupby('name')
customer_group.size()


# In[ ]:


my_plot = sales_totals.plot(kind='bar')


# In[13]:


#Unfortunately this chart is a little ugly. With a few tweaks we can make it a little more impactful. Let’s try:

#sorting the data in descending order
#removing the legend
#adding a title
#labeling the axes
my_plot = sales_totals.plot(kind='bar',legend=None,title="Total Sales by Customer")
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales ($)")


# In[14]:


#This actually tells us a little about our biggest customers and how much difference there is between their sales 
#and our smallest customers.

#Now, let’s try to see how the sales break down by category.

customers = sales[['name','category','ext price','date']]
customers.head()


# In[15]:


#We can use groupby to organize the data by category and name.
category_group=customers.groupby(['name','category']).sum()
category_group.head()


# In[16]:


#The category representation looks good but we need to break it apart to graph it as a stacked bar graph. 
#unstack can do this for us.

category_group.unstack().head()


# In[17]:


my_plot = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer")
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales")


# In[18]:


#In order to clean this up a little bit, we can specify the figure size and customize the legend.

my_plot = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer",figsize=(9, 7))
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales")
my_plot.legend(["Total","Belts","Shirts","Shoes"], loc=9,ncol=4)


# In[19]:


#Now that we know who the biggest customers are and how they purchase products, we might want to look at purchase patterns 
#in more detail.

#Let’s take another look at the data and try to see how large the individual purchases are. 
#A histogram allows us to group purchases together so we can see how big the customer transactions are.


# In[20]:


purchase_patterns = sales[['ext price','date']]
purchase_patterns.head()


# In[26]:


#We can create a histogram with 20 bins to show the distribution of purchasing patterns.

purchase_plot = purchase_patterns['ext price'].hist(bins=20)
purchase_plot.set_title("Purchase Patterns")
purchase_plot.set_xlabel("Order Amount($)")
purchase_plot.set_ylabel("Number of orders")


# In[27]:


#In looking at purchase patterns over time, we can see that most of our transactions are less than $500 and only a very few 
#are about $1500.

#Another interesting way to look at the data would be by sales over time. A chart might help us understand, 
#“Do we have certain months where we are busier than others?”

#Let’s get the data down to order size and date.

purchase_patterns = sales[['ext price','date']]
purchase_patterns.head()


# In[28]:


#If we want to analyze the data by date, we need to set the date column as the index using set_index .

purchase_patterns = purchase_patterns.set_index('date')
purchase_patterns.head()


# In[29]:


#One of the really cool things that pandas allows us to do is resample the data. 
#If we want to look at the data by month, we can easily resample and sum it all up. 
#You’ll notice I’m using ‘M’ as the period for resampling which means the data should be resampled on a month boundary.

purchase_patterns.resample('M',how=sum)


# In[30]:


purchase_plot = purchase_patterns.resample('M',how=sum).plot(title="Total Sales by Month",legend=None)


# In[37]:


#end


# In[ ]:




