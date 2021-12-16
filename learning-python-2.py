# Reading a CSV with DictReader

import csv

with open('presentation.csv') as csv_file:
 reader = csv.DictReader(csv_file, delimiter=";")
 for line in reader:
      print(line["firstname"], " is working as a ", line["job"], " and enjoys ", line["favorite_thing"])