"""
Utilisation des packages :
- requests
- BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
response = requests.get(url)
page = BeautifulSoup(response.content, "html.parser")

def getPageTagsContent(tag, className):
    tagsStringed = []
    tags = page.find_all(tag, className)
    for tag in tags:
        tagsStringed.append(tag.string)
    print("\nContent retreived :\n", tagsStringed, "\n")
    return tagsStringed

getPageTagsContent("a", "gem-c-document-list__item-title")

getPageTagsContent("p", "gem-c-document-list__item-description")

