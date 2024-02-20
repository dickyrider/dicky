#!/usr/bin/env python
# coding: utf-8

# In[122]:


import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt


# # Question 1 - Extracting Tesla Stock Data Using yfinance

# In[93]:


ticker = "TSLA"
tesla_data = yf.download(ticker, period="1y")
tesla_df = pd.DataFrame(tesla_data)


# In[125]:


tesla_df.head()


# # Question 2 - Extracting Tesla Revenue Data Using Webscraping 

# In[103]:


#can't access 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
requests.get(url)


# # Question 3 - Extracting GameStop Stock Data Using yfinance

# In[104]:


ticker = "GME"
GME_data = yf.download(ticker, period="1y")
gme_df = pd.DataFrame(GME_data)


# In[126]:


gme_df.tail()


# # Question 4 - Extracting GameStop Revenue Data Using Webscraping

# In[107]:


#can't access 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'
requests.get(url)



# # Def for Dashboard

# In[118]:


def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'], color='blue')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(title)
    plt.grid(True)
    plt.show()


# # Question 5 - Tesla Stock and Revenue Dashboard

# In[108]:


tesla_df.reset_index(inplace=True)


# In[123]:


make_graph(tesla_df, 'Tesla Stock Price')


# # Question 6 - GameStop Stock and Revenue Dashboard

# In[113]:


gme_df.reset_index(inplace=True)


# In[124]:


make_graph(gme_df, 'GameStop Stock Price')


# In[ ]:




