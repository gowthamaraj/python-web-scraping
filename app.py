import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/LOr%C3%A9al-Paris-Colour-Lipstick-Silverstone/dp/B004BCVFL6/ref=sr_1_12?_encoding=UTF8&c=ts&dchild=1&keywords=Lipsticks&qid=1594664999&refinements=p_72%3A1318476031&rnid=1318475031&sr=8-12&ts_id=1374384031'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(url,headers = headers)

soup = BeautifulSoup(page.content,'html.parser')


price = soup.find(class_="a-color-price").get_text().strip()[2:7]

price = (price).replace(',','')
price = float(price)

print(price)