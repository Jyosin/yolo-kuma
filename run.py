import torch
import os

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  
# # or yolov5n - yolov5x6, custom

# Images
# img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

img_path = '/home/wang/yolov5/kuma_data'
imgs  = os.listdir(img_path)
for img in imgs:

# # Inference
    data = 'kuma_data/'
    data = data + img

    results = model(data)
    results.show()
    results.save()
    
# results = model('kuma_data/test_6.jpg')
# results.show()
# # Results

 # or .show(), .save(), .crop(), .pandas(), etc.