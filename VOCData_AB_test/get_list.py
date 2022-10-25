from importlib.resources import path
from re import L
# from turtle import position
import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as plt


path = "/home/wang/yolov5/VOCData_AB/labels"
files = os.listdir(path)

lable = []

file_name = []


for file in files :
    file = file.replace('test_','')
    file = file.replace('.txt','')
    
    file_name.append(int(file))
    # position = path + '\\' + file
    file_name.sort()

for i in file_name:
    position = path + '/' + 'test_' + str(i) + '.txt'
    with open (position,"r") as f :
        for line in f.readlines():
            data = line.split()
            lable.append(data)

lable_float = []
x_center = []
y_center = []

for j in lable :
    list_float = []
    for k in j:
        list_float.append(float(k))
    lable_float.append(list_float)
    x_center.append(list_float[1])
    y_center.append(list_float[2])

plt.plot(x_center,"red")
plt.plot(y_center,"blue")

plt.show()



# print (x_center)