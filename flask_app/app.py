from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests
prices = []
links = []
app = Flask(__name__)
css = '<link rel="stylesheet" href="styles.css">'
link = '<a href="http://127.0.0.1:5000/">Another Search</a>'
@app.route('/')
def form():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def show():
    search_query = request.form['text']
    website = requests.get('https://www.goodreads.com/search?q='+search_query).text
    soup = BeautifulSoup(website,'lxml')
    for a in soup.find_all('a', href=True):
        links.append(a['href'])
    data_website = requests.get('https://www.goodreads.com'+links[108]).text
    soup = BeautifulSoup(data_website,'lxml')
    book_title = soup.find('h1',{'id':'bookTitle'}).text.strip()
    author = soup.find('div',{'id':'bookAuthors'}).text.strip().split('\n')
    author = ''.join(author)
    author = author[2:]
    try:
        description = soup.find("div", {"class":"readable stacked"}).text
        description = description.split('\n')
    except:
        description = 'None'
    rating = soup.find('span',{'itemprop':'ratingValue'}).text.strip()
    series = soup.find('a',{'class':'greyText'}).text.strip()
    if series.lower() == 'edit details': 
        series = 'N/A'
    pages = soup.find("span", {"itemprop":"numberOfPages"}).text
    image = soup.find('img',{'id':'coverImage'})
    website = requests.get('https://www.bookdepository.com/search?searchTerm='+book_title).text
    soup = BeautifulSoup(website,'lxml')
    b = soup.find('div',{'class':'price-wrap'}).text.strip().split()
    book_depository = b[0]
    website1 = requests.get('https://www.abebooks.com/servlet/SearchResults?cm_sp=SearchFwi-_-SRP-_-Results&isbn=0439023513&kn='+book_title).text
    soup = BeautifulSoup(website1,'lxml')
    try:
        abe_books = soup.find('div',{'class':'srp-item-price'}).text.strip()
    except: 
        abe_books = soup.find('span',{'class':'price-muted'}).text.strip()
    links.clear()
    return render_template('show.html',book_title=book_title,series=series,rating=rating,book_depository=book_depository,abe_books=abe_books,description=description[2],author=author,pages=pages,link=link)
if __name__ == '__main__': 
    app.run(debug=True)
