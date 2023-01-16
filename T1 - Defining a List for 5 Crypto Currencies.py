#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# TASK 1 - Defining a Python List That Contains 5 Crypto Currencies
crypto_list = ['BTC', 'XRP', 'LTC', 'ADA', 'ETH' ]
crypto_list


# In[3]:


# Confirming the Data Type
type(crypto_list)


# In[4]:


# Creating A One Dimensional Pandas Series
crypto_series = pd.Series(data = crypto_list)
crypto_series


# In[5]:


# Confirming the Pandas Series Data Type
type(crypto_series)


# In[6]:


# Defining Another Pandas Series with Crypto Prices
crypto_prices_series = pd.Series(data = [2000, 500, 2000, 20, 50])
crypto_prices_series

