import os
from unittest import skip
import cv2
import sys



def plot_bbox():
	# 总的检测根目录
    path_root_labels = '/home/wang/yolov5/VOCData_AB/labels'
    # 总的检测根目录
    path_root_imgs ='/home/wang/yolov5/VOCData_AB/images'

    save_path = '/home/wang/yolov5/VOCData_AB/lable_image'

    type_object = '.txt'


    for ii in os.walk(path_root_imgs):
        for j in ii[2]:
            type = j.split(".")[1]
            if type != 'jpg':
                continue
            path_img = os.path.join(path_root_imgs, j)
            print(path_img)
            label_name = j[:-4]+type_object
            path_label = os.path.join(path_root_labels, label_name)
            # print(path_label)
            f = open(path_label, 'r+', encoding='utf-8')
            if os.path.exists(path_label) == True:

                img = cv2.imread(path_img)
                w = img.shape[1]
                h = img.shape[0]
                new_lines = []
                while True:
                    line = f.readline()
                    if line:
                        img_tmp = img.copy()
                        msg = line.split(" ")
                        # print(x_center,",",y_center,",",width,",",height)
                        x1 = int((float(msg[1]) - float(msg[3]) / 2) * w)  # x_center - width/2
                        y1 = int((float(msg[2]) - float(msg[4]) / 2) * h)  # y_center - height/2
                        x2 = int((float(msg[1]) + float(msg[3]) / 2) * w)  # x_center + width/2
                        y2 = int((float(msg[2]) + float(msg[4]) / 2) * h)  # y_center + height/2
                        print(x1,",",y1,",",x2,",",y2)
                        cv2.rectangle(img_tmp,(x1,y1),(x2,y2),(255,255,255),1)
                    else :
                        break
            cv2.imshow("show", img_tmp)
            cv2.imwrite(os.path.join(save_path,j),img_tmp)
            c = cv2.waitKey(0)


def save_mp4():
    path = "/home/wang/yolov5/runs/detect/exp2"
    files = os.listdir(path)

    file_name = []
    last_name = []

    for file in files :
        if file == '/':
            skip
        file = file.replace('test_','')
        file = file.replace('.jpg','')
        file_name.append(int(file))
        # position = path + '\\' + file
        file_name.sort()

 # 生成图片目录下以图片名字为内容的列表

    # fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G') 用于avi格式的生成

    for i in file_name:
        paths = path  + '/' + 'test_' + str(i) + '.jpg'
        last_name.append(paths)

      # 创建一个写入视频对象




if __name__ == '__main__':
    # plot_bbox()
    save_mp4()


