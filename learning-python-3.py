"""
Utilisation de :
- csv
- writer
- writerow
"""

import csv
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
    return tagsStringed

titles = getPageTagsContent("a", "gem-c-document-list__item-title")
descriptions = getPageTagsContent("p", "gem-c-document-list__item-description")

header = ["title", "description"]
with open("titles_and_descriptions.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(header)
    for title, description in zip(titles, descriptions):
        writer.writerow([title, description])
    print("File saved in your local repository")