#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install splinter
#!pip install webdriver_manager
#!pip install pymongo


# In[2]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', executable_path, headless=False)

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[5]:


html = browser.html
soup = bs(html, 'html.parser')


# In[6]:


print(soup.prettify())


# In[9]:


news = soup.find("li", class_="slide")
news_title = news.find("div",class_="content_title").text
news_p = news.find("div", class_="article_teaser_body").text


# In[10]:


print(news_title)
print(news_p)


# In[11]:


#JPL Mars Space Images Scrape
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[12]:


html = browser.html
soup = bs(html, 'html.parser')


# In[13]:


print(soup.prettify())


# In[14]:


image = soup.find('div', class_='carousel_container')
f_image = image.a['data-fancybox-href']
base_url = "https://www.jpl.nasa.gov"
featured_image_url = base_url + f_image


# In[15]:



print(featured_image_url)


# In[16]:


#Mars Facts
url = 'https://space-facts.com/mars/'
browser.visit(url)


# In[17]:


html = browser.html
soup = bs(html, 'html.parser')


# In[18]:



print(soup.prettify())


# In[19]:


mars = pd.read_html(url)


# In[20]:



mars


# In[21]:



mars_data = mars[0]
mars_data


# In[ ]:




