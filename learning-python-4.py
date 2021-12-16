""" 
Récupération des données du csv input avec DictReader
Injection de ces données dans un fichier output
"""

import csv

def listInputColumnData(columnHeader):
    listOfDataRetreived = []
    with open("input.csv") as input:
        reader = csv.DictReader(input, delimiter=",")
        for line in reader:
            listOfDataRetreived.append(line[columnHeader])
        return listOfDataRetreived

header = ["nom", "salaire"]
with open("output.csv", "w") as output:
    writer = csv.writer(output, delimiter=",")
    writer.writerow(header)
    names = listInputColumnData("nom")
    hours = listInputColumnData("heures_travaillees")
    for name, hour in zip(names, hours):
        hour = int(hour) * 15
        writer.writerow([name, hour])
    print("File saved")