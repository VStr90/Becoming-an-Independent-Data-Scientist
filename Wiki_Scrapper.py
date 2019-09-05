import requests
from bs4 import BeautifulSoup

def wiki_scrape(url):

    req = requests.get(url)

    soup = BeautifulSoup(req.text,'lxml')
    contents = soup.find('div',class_='mw-parser-output').find_all('p')

    # title of the article
    title = soup.find('table',class_ = 'infobox vcard').find('caption').text
    print('=========================')
    print('--------WIKI TITLE-------')
    print('=========================')
    print(title)

    print('=========================')
    print('--------REFERENCES-------')
    print('=========================')

    # print(contents)
    references = soup.find('div',class_='mw-references-wrap mw-references-columns')

    for ref in references.find_all('a',class_='external text'):
        print(ref['href'])



wiki_scrape('https://en.wikipedia.org/wiki/Davide_Calabria')
