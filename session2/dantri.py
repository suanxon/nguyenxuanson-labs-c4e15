url = "http://dantri.com.vn/"
ouput_file= "news.xlsx"
#1 download website
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
#1.1 mo ket noi toi website
connect = urlopen(url)
#1.2 doc du lieu
data = connect.read()
# 1.3 decode
html_content = data.decode('utf-8') # utf-8: unicode
#gop lai:
html_content = urlopen("http://dantri.com.vn/").read().decode('utf-8')
#luu ra 1 file pohng truong hop mat mang
html_file = open("dantri.html", "w")
html_file.write(html_content)
html_file.close()
#2 Extract ROI ( trich xuat vung quan tam)

#3 Extract News ( trich thong tin can thiet)

#Create a soup
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify)  # lam dep
ul = soup.find('ul', "ul1 ulnew") # class la dac biet, neu id thi viet id =""
# print(ul.prettify)
li_list = ul.find_all('li')
# for li in li_list:
#     print(li.prettify())
#     print("*" * 20)

li =li_list[0]
# h4 = li.find('h4')
# # print(h4)
# a = h4.find('a')
new_list= []
for li in li_list:
    a = li.h4.a # di tat
    href = url + a['href']
    #dung stri o title:
    title = a.string
    news = {
        'Title': title,
        'Link': href
    }
    new_list.append(news)
    # print(href)
    # print(title)
print(new_list)

pyexcel.save_as(records = new_list, dest_file_name= 'dantri.xlsx')
