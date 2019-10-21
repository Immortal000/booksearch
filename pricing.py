from bs4 import BeautifulSoup
import requests
book_title = input()

website = requests.get('https://www.bookdepository.com/search?searchTerm='+book_title).text
soup = BeautifulSoup(website,'lxml')
b = soup.find('div',{'class':'price-wrap'}).text.strip().split()
book_repository = b[0]

website = requests.get('https://www.abebooks.com/servlet/SearchResults?cm_sp=SearchFwi-_-SRP-_-Results&isbn=0439023513&kn='+book_title).text
soup = BeautifulSoup(website,'lxml')
try:
  abe_books = soup.find('div',{'class':'srp-item-price'}).text.strip()
except: 
  abe_books = soup.find('span',{'class':'price-muted'}).text.strip()

print(book_depository,abe_books)

