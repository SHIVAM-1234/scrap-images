from collections import UserList
import requests
from bs4 import BeautifulSoup
import os

url = "https://www7.animeseries.io"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

images = soup.find_all('img')

 for image in img:
     name = image['alt']
     print(image['src'])
     with open(name.replace('','-').replace('/','')+'.jpg','wb') as f:
         im = requests.get(link)
         f.write(im.content)