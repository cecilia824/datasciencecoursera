import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#這裡需要用到urllib, BeautifulSoup

url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1

print('Retrieving:', url)
for i in range(count):
#repeat的次數 例如四次 0 1 2 3!!!
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href',None)
    print('Retrieving:', link)
    url = link
    
