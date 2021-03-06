"""
Utilisation des packages :
- requests
- BeautifulSoup

Exemple d'Extract-transform-load ou datapumping
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

titles = getPageTagsContent("a", "gem-c-document-list__item-title")
descriptions = getPageTagsContent("p", "gem-c-document-list__item-description")

