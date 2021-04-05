import csv
import os

f = open('/Users/Vladisalv/Desktop/Новая папка/test/analiz_res/canvaz_analiz/1.par')
flag = 1

myData = []

col = []
col.append('name')
for line in f:
    flag = flag + 1
    if flag > 19:
        lst = line.split()
        if len(lst) > 1:
            col.append(lst[0])
myData.append(col)
print(myData)

print("START")
res = []
dir = '/Users/Vladisalv/Desktop/Новая папка/test/analiz_res/canvaz_analiz/'
files = os.listdir(dir)
for file in files:
    f = open(dir + file)
    flag = 1
    img = []
    img.append('canvaz')
    for line in f:
        flag = flag + 1
        if flag > 19:
            lst = line.split()
            if len(lst) > 1:
                img.append(lst[1])
    myData.append(img)

print("END canvaz_analiz")

dir = '/Users/Vladisalv/Desktop/Новая папка/test/analiz_res/cushion_analiz/'
files = os.listdir(dir)
for file in files:
    f = open(dir+file)
    flag = 1
    img = []
    for line in f:
        img.append('cushion')
        for line in f:
            flag = flag + 1
            if flag > 19:
                lst = line.split()
                if len(lst) > 1:
                    img.append(lst[1])
        myData.append(img)
print("END cushion_analiz")




myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete")
