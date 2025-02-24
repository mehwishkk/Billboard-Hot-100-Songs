import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL= f'https://www.billboard.com/charts/hot-100/{date}/'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response=requests.get(URL, headers=header)
website_html=response.text

soup=BeautifulSoup(website_html,'html.parser')
#print('@@',soup)

all_songs=soup.select("li ul li h3")

song_names = [song.getText().strip() for song in all_songs]
for n in song_names:
    print(n)
