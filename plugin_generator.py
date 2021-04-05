import os

print("START")
f = open("canvas1.plugin", 'w')
files = os.listdir('/Users/Vladisalv/PycharmProjects/Scikitlearn/subsetOfKylbergTextureDataset-6classes-40samples/canvas1')
for file in files:
    print(file)
    f.write("LoadImage " + file + '\n')
    f.write("RunAnalysis" + '\n')
    f.write("SaveReport " + os.path.splitext(file)[0] + ".par" + '\n' + '\n')

f = open("cushion1.plugin", 'w')
files = os.listdir('/Users/Vladisalv/PycharmProjects/Scikitlearn/subsetOfKylbergTextureDataset-6classes-40samples/cushion1')
for file in files:
    print(file)
    f.write("LoadImage " + file + '\n')
    f.write("RunAnalysis" + '\n')
    f.write("SaveReport " + os.path.splitext(file)[0] + ".par" + '\n' + '\n')

f = open("linsseeds1.plugin", 'w')
files = os.listdir('/Users/Vladisalv/PycharmProjects/Scikitlearn/subsetOfKylbergTextureDataset-6classes-40samples/linsseeds1')
for file in files:
    print(file)
    f.write("LoadImage " + file + '\n')
    f.write("RunAnalysis" + '\n')
    f.write("SaveReport " + os.path.splitext(file)[0] + ".par" + '\n' + '\n')

f = open("sand1.plugin", 'w')
files = os.listdir('/Users/Vladisalv/PycharmProjects/Scikitlearn/subsetOfKylbergTextureDataset-6classes-40samples/sand1')
for file in files:
    print(file)
    f.write("LoadImage " + file + '\n')
    f.write("RunAnalysis" + '\n')
    f.write("SaveReport " + os.path.splitext(file)[0] + ".par" + '\n' + '\n')

f = open("seat2.plugin", 'w')
files = os.listdir('/Users/Vladisalv/PycharmProjects/Scikitlearn/subsetOfKylbergTextureDataset-6classes-40samples/seat2')
for file in files:
    print(file)
    f.write("LoadImage " + file + '\n')
    f.write("RunAnalysis" + '\n')
    f.write("SaveReport " + os.path.splitext(file)[0] + ".par" + '\n' + '\n')

f = open("stone1.plugin", 'w')
files = os.listdir('/Users/Vladisalv/PycharmProjects/Scikitlearn/subsetOfKylbergTextureDataset-6classes-40samples/stone1')
for file in files:
    print(file)
    f.write("LoadImage " + file + '\n')
    f.write("RunAnalysis" + '\n')
    f.write("SaveReport " + os.path.splitext(file)[0] + ".par" + '\n' + '\n')

print("END")