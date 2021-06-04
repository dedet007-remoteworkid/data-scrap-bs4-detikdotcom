import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/terpopuler'
rs = requests.get(url, params={'tag_from': 'framebar'})

sp = BeautifulSoup(rs.text, 'html.parser')

pop_area = sp.find(attrs={'class': 'grid-row list-content'})

judul = pop_area.findAll(attrs={'class': 'media__title'})
foto = pop_area.findAll(attrs={'class': 'media__image'})

#for j in judul:
#    print(j.text)

#print(foto)

for f in foto:
    #print(f.text)
    #print(f.find('a'))
    #print(f.find('a').find('img'))
    print(f.find('a').find('img')['title'])

# print(judul)
