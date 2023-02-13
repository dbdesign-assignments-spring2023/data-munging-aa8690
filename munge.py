# Afsana Ahmed, Munge NASA Index Data

resultdata = []

o = open('data/nasa_index.txt','r')
data = o.read()
data = data.split("\n")

for element in data:
    if element == '':
        data.remove(element)

data = data[5:156]
months = 'Year   Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec    J-D D-N    DJF  MAM  JJA  SON  Year'

for element in data:
    if element == months:
        data.remove(element)

data.insert(0,months)

c = open('data/clean_data.csv','w')

for i in range(len(data)):
    data[i] = data[i].split()

for i in range(1,len(data)):
    for j in range(1,len(data[i])-1):
        element = data[i][j]

        if element[0] != "*":
            element = int(element)
            data[i][j] = (element / 100) * 1.8
            data[i][j] = (format(data[i][j],'.1f'))

    # write each piece of data to the list and include line breaks

for i in data:
  resultdata.append(','.join(i))

resultdata = '\n'.join(resultdata)

c.write(resultdata)
# print(resultdata)

c.close()