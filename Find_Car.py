import torch
from PIL import Image
import cv2
import numpy as np
# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='Models/Car_detect.pt')

#Converting Pillow image to cv2
def PIL_to_CV2(nparr):
    image= cv2.cvtColor(nparr, cv2.COLOR_RGB2BGR)
    return image.copy()

#Using the car detection model and returning the images of the cars in the pics
def find_car(img):
    # Inference

    #using Model
    results = model(img)

    #Getting the xmin,xmax,ymin,ymax of the cars
    bbox=[]
    for x in results.xyxy[0]:
        bbox.append([int(item) for item in x[:4]])
    #opening image using pillow
    img = Image.open(img)

    #Cropping the cars out of the image and saving them into list
    imges=[]
    for i in bbox:
        img2 = img.crop((i[0],i[1],i[2],i[3]))
        imges.append(np.array(img2))
    #Converting images from pillow object into cv2 model
    for pos,img in enumerate(imges):
        imges[pos]=PIL_to_CV2(img)
    return imges


