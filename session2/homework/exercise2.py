from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div',style = 'overflow:hidden;width:100%;border-bottom:solid 1px #cecece;')
table = div.find('table',id = 'tableContent')
tr_list = table.find_all('tr')


financial_list = []
for tr in tr_list:
    td_list = tr.find_all('td')
    for td in td_list:

        title = td_list[0].string
        col2 = td_list[1].string
        col3 = td_list[2].string
        col4 = td_list[3].string
        col5 = td_list[4].string

    table = {
        '5.Quý 3-2017': col5,
        '4.Quý 2-2017': col4,
        '3.Quý 1-2017': col3,
        '2.Quý 4-2016': col2,
        '1.title': title
    }

    financial_list.append(table)

pyexcel.save_as(records=financial_list,dest_file_name='Cafef.xlsx')
