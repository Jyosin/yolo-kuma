import cv2
vidcap = cv2.VideoCapture('/home/wang/yolov5/images/one_day/20/91_2020_09_22_20.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite('/home/wang/yolov5/images/one_day/20/%d.jpg'% count,image)
  count += 1