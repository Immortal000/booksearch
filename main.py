from bs4 import BeautifulSoup
import requests
while True:
    links =[]
    search_query = input()
    website = requests.get('https://www.goodreads.com/search?q='+search_query).text
    soup = BeautifulSoup(website,'lxml')
    for a in soup.find_all('a', href=True):
        links.append(a['href'])
    data_website = requests.get('https://www.goodreads.com'+links[108]).text
    soup = BeautifulSoup(data_website,'lxml')
    book_title = soup.find('h1',{'id':'bookTitle'}).text.strip()
    author = soup.find('div',{'id':'bookAuthors'}).text.strip().split('\n')
    author = ''.join(author)
    try:
        description = soup.find("div", {"class":"readable stacked"}).text
        description = description.split('\n')
    except:
        description = 'None'
    rating = soup.find('span',{'itemprop':'ratingValue'}).text.strip()
    try:
        series = soup.find('a',{'class':'greyText'}).text.strip()
    except:
        series = 'N/A'
    pages = soup.find("span", {"itemprop":"numberOfPages"}).text
    website = requests.get('https://www.bookdepository.com/search?searchTerm='+book_title).text
    soup = BeautifulSoup(website,'lxml')
    b = soup.find('div',{'class':'price-wrap'}).text.strip().split()
    book_price = b[0]
    print(f"Book Title:{book_title}\nBook Series:{series}\nBook Author:{author[2:]}\nBook Rating:{rating}\nLength of the book:{pages}\nBook Price:{book_price}\nDescription:{description[1]}")
