import csv 
data1 = []
data2 = []
with open ('dataset_1.csv','r')as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data1.append(row)
with open ('dataset_2.csv','r')as f:
    csvReader1 = csv.reader(f)
    for row in csvReader1:
        data2.append(row)
header1 = data1[0]
planet1 = data1[1:]
header2 = data2[0]
planet2 = data2[1:]
headers = header1+header2
planetData = []
for index,row in enumerate(planet1):
    planetData.append(planet1[index]+planet2[index])
with open('finalData.csv','a+')as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)
