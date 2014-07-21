
# coding: utf-8

# In[4]:

import urllib2

search_url = 'http://fishbase.se/search.php'
search_page = urllib2.urlopen(search_url)

print search_page.read(200)

soup = BeautifulSoup(search_page)


# In[14]:

import urllib2
from bs4 import BeautifulSoup
opener = urllib2.build_opener()
url = ('http://wired.com')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl)

print soup.title.text

for link in soup.find_all('a'):
    print(link.get('href'))


# In[ ]:



