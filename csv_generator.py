import csv
import os

f = open('/Project/Scikitlearn/res_texture_analysis/canvas1/canvas1-a-p001.par')
flag = 1

myData = []

col = []
col.append('class_name')
col.append('file_name')
for line in f:
    flag = flag + 1
    if flag > 19:
        lst = line.split()
        if len(lst) > 1:
            col.append(lst[0])
myData.append(col)
# print(myData)

print("START")
res = []
main_dir = '/Project/Scikitlearn/res_texture_analysis'
dirs = os.listdir(main_dir)
for dir in dirs:
    files = os.listdir(main_dir + "/" + dir)
    for file in files:
        f = open(main_dir + "/" + dir + "/" + file)
        flag = 1
        img = []
        img.append(dir)
        img.append(file)
        for line in f:
            flag = flag + 1
            if flag > 19:
                lst = line.split()
                if len(lst) > 1:
                    img.append(lst[1])
                    print(lst[1])
        myData.append(img)
print("END")

myFile = open('res.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete")
