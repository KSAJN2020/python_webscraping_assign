##Adding Comment directly in Web git
from bs4 import BeautifulSoup
import requests
import csv
fv
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Book Title', 'Prize', 'Stock Info'])
l
source = requests.get('http://books.toscrape.com/').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

section = soup.find('section')
#print(section)
for li_tag in section.find_all('li'):
    #print(li_tag.h3.a)
    #get title
    try:
        title = (li_tag.h3.a)['title']
        print(title)

        #get prize
        prd_price = li_tag.find('div', class_='product_price')
        price = (prd_price.p.text)[1:]
        print(price)

        #stock Information
        stock_info = (prd_price.find('p', class_='instock availability').text).strip('\n" "')
        print(type(stock_info))
        print(stock_info)
    except:
        title = None
        price = None
        stock_info = None

    csv_writer.writerow([title, price, stock_info])
csv_file.close()
