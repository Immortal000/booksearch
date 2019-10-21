from bs4 import BeautifulSoup
import requests
book_title = input()

website = requests.get('https://www.bookdepository.com/search?searchTerm='+book_title).text
soup = BeautifulSoup(website,'lxml')
b = soup.find('div',{'class':'price-wrap'}).text.strip().split()

website = requests.get('https://www.abebooks.com/servlet/SearchResults?cm_sp=SearchFwi-_-SRP-_-Results&isbn=0439023513&kn='+book_title).text
soup = BeautifulSoup(website,'lxml')
price = soup.find('div',{'class':'srp-item-price'}).text.strip()

print(b[0],price)

