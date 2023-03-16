from bs4 import BeautifulSoup
import requests


header = {
    #Сюда помещаем наш user-agent
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.3.949 Yowser/2.5 Safari/537.36'
}
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
spisok = {}
resp = requests.get(url, headers=header).text
soup = BeautifulSoup(resp, "html.parser")
block3 = soup.findAll('tr')
block1 = soup.findAll('td', class_='titleColumn')
block2 = soup.findAll('td', class_='ratingColumn imdbRating')

rating = ''
name = ''
list = []
count = 0
for data in block1:

     if data.find('a'):
        name = data.text
        name = name.replace('\n', '')
        name = name.replace('  ', '')
        list.append(name)



for data1 in block2:

    if data1.find('strong'):
        rating = data1.text
        rating = rating.replace('\n', '')
        rating = rating.replace('  ', '')
        spisok[list[count]] = rating
        if count == 250:
            break
        count += 1

print(spisok)

