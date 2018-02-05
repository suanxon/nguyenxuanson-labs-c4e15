from urllib.request import urlopen
from bs4 import BeautifulSoup

import pyexcel
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section', 'section chart-grid')
div = section.find('div', 'section-content')
ul = div.find('ul')
li_list = ul.find_all('li')

Song_list = []
for lis in li_list:
    names = lis.h3.string
    artists = lis.h4.string
    Names_Artists = {
        'Names': names,
        'Artists': artists
    }
    Song_list.append(Names_Artists)
pyexcel.save_as(records = Song_list, dest_file_name = 'itunes.xlsx')

# Setup cho youtubedl
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}


for song in Song_list:
    dl = YoutubeDL(options)
    dl.download([song['Names']])
