import xml.etree.ElementTree as ET
import os
from os import getcwd
import shutil

file_name_1 = "/home/wang/yolov5/VOCData_C/images"
file_name_2 = "/home/wang/yolov5/VOCData_C/Annotations"
file_name_3 = "/home/wang/yolov5/VOCData_C/labels"

image = []
annotation = []

for file in os.listdir(file_name_1):
    if file.endswith(".jpg"):
        num,j = file.split(".")
        image.append(num)

for file in os.listdir(file_name_2):
    if file.endswith("xml"):
        num,j = file.split(".")
        annotation.append(num)

for img in image:
    if img not in annotation:
        os.remove(os.path.join(file_name_1,str(img)+".jpg"))

for xml in annotation:
    if xml not in image:
        os.remove(os.path.join(file_name_2,str(xml)+".xml"))

for file in os.listdir(file_name_3):
    if file.endswith('copy.txt'):
        os.remove(file_name_3 +"/"+ file)