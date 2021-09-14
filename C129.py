import  csv
data = []

with open('final.csv','r' )as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)
headers = data[0]
planet_data = data[1:]
for datapoint in planet_data:
    datapoint[0]=datapoint[0].lower()
planet_data.sort(key=lambda planet_data:planet_data[0])
with open('final2.csv','a+')as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)