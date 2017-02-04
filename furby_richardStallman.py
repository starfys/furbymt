import urllib3
from bs4 import BeautifulSoup
import random

# returns a random quote from the legendary stallman (90 quotes)
def stallman():
	http = urllib3.PoolManager()

	# page 1
	rms =  http.request('GET','http://www.azquotes.com/author/13994-Richard_Stallman')
	page = rms.data

	soup = BeautifulSoup(page, "lxml")
	soup = soup.find_all('a', class_='title')

	# define the quotes list
	quotes = []

	for quote in soup:
		soup = quote.text
		quotes.append(soup)

	# page 2
	rms = http.request('GET','http://www.azquotes.com/author/13994-Richard_Stallman?p=2')
	page = rms.data

	soup = BeautifulSoup(page, "lxml")
	soup = soup.find_all('a', class_='title')

	for quote in soup:
		soup = quote.text
		quotes.append(soup)

	# page 3
	rms = http.request('GET','http://www.azquotes.com/author/13994-Richard_Stallman?p=3')
	page = rms.data

	soup = BeautifulSoup(page, "lxml")
	soup = soup.find_all('a', class_='title')

	for quote in soup:
		soup = quote.text
		quotes.append(soup)

	# page 4
	rms = http.request('GET','http://www.azquotes.com/author/13994-Richard_Stallman?p=4')
	page = rms.data

	soup = BeautifulSoup(page, "lxml")
	soup = soup.find_all('a', class_='title')

	for quote in soup:
		soup = quote.text
		quotes.append(soup)

	return(str(random.choice(quotes)))