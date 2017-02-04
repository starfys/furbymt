from bs4 import BeautifulSoup
import urllib3
import random

def inspire():
    
    http = urllib3.PoolManager()

    # Choose a random page number for the file read
    pageNumber = str(random.randint(1,3))
    if (pageNumber == '1'):
        pageNumber = ''

    # Request page content and parse
    quotePage = http.request('GET', 'https://www.brainyquote.com/quotes/authors/k/karl_marx' + pageNumber + '.html')
    inspSoup = BeautifulSoup(quotePage.data, 'html.parser')

    #print inspSoup.prettify()

    # Find all quotes on the page
    quoteList = inspSoup.find_all('a', title="view quote")

    # Remove all occurrences of quote author
    for i in quoteList:
        if(str(i).find('Karl Marx') != -1):
            quoteList.remove(i)

    # Strip the quotes of their headers
    for i in range(len(quoteList)):
        begin = str(quoteList[i]).find('>')
        end = str(quoteList[i]).find('<', begin)
        quoteList[i] = str(quoteList[i])[begin + 1: end]

    return quoteList[random.randint(0,len(quoteList)-1)]
