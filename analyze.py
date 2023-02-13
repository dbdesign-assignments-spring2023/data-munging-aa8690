# Afsana Ahmed, Analyze NASA Global Temperate Index Data

import csv

c = open('data/clean_data.csv','r')

reader = csv.reader(c)

all_data = c.read()
all_data = all_data.split("\n")

for i in range(len(all_data)):
    all_data[i] = all_data[i].split(",")

count = 1
decade_mean = []
temp = []
decades_list = ['1880 - 1889:', '1890 - 1899:', '1900 - 1909:', '1910 - 1919:', '1920 - 1929:', '1930 - 1939:', '1940 - 1949:', '1950 - 1959:', '1960 - 1969:', '1970 - 1979:', '1980 - 1989:', '1990 - 1999:', '2000 - 2009:', '2010 - 2019:','2020 - Present:']

for i in range(1, len(all_data)):
    if count == 10:
        count = 1
        avg_temp = format(((sum(temp)) / 10),'.1f')
        decade_mean.append(avg_temp)
        temp = []

    if all_data[i][13][0] != "*":
        temp.append(float(all_data[i][13])),
    
    count += 1

print("Average Temperature Anomaly in Degrees Farenheit For Each Decade (1880 - Present)")

for v in range(len(decade_mean)):
    print(decades_list[v], decade_mean[v], "degrees Fahrenheit")
