

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



