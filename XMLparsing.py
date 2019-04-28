import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

location = input('Enter location: ')
print('Retrieving ',location)

html = urllib.request.urlopen(location).read()
print('Retrieved ', len(html),'characters')

tree = ET.fromstring(html)
#轉化data這string為樹狀圖
lst = tree.findall('.//comment')
#找出來變成comment小樹的list
#為什麼這邊用.//?????
sum = 0
for item in lst: #item是剛剛lst內每個以comment為母體的小樹
    #item.find('count').text 從每個小樹裡面找出count的值
    sum = sum + int(item.find('count').text)

print('Count:', len(lst))
print('Sum:',sum)
