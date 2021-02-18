from bs4 import BeautifulSoup
import requests
import random

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )
    soup = BeautifulSoup(response.content, 'html.parser')
 
    title = soup.find(id="firstHeading")
    print(title.string)

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        if link["href"].find("/wiki/") == -1:
            continue

        linkToScrape = link
        break
    scrapeWikiArticle("https://tr.wikipedia.org/"+ linkToScrape["href"])

scrapeWikiArticle("https://tr.wikipedia.org/wiki/Uzay_arac%C4%B1")