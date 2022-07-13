import os
from os import listdir
import cv2
import os
import pytesseract
import json
import numpy as np

#pytesseract.pytesseract.tesseract_cmd = '/Users/kishanmishra/Desktop/OCRbilling_system/pytesseract/pytesseract/pytesseract.py'


def transfer(imagename,text):
    name=imagename[:len(imagename)-5]+".txt"
    with open("./Extracted_texts/{}".format(name), "w") as f:
            f.write(text)
    f.close()



# Preprocessing  ---------------------------------------------------------

def get_grayscale(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    return cv2.medianBlur(img,5)

def thresholding(img):
    return cv2.threshold(img,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[0]


res=dict()

folder_dir = './special'
i=0
for images in os.listdir(folder_dir):
 
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):

        #text=pytesseract.image_to_string(k)
        text=str(i)
        imname=images[:len(images)-4]
        res[imname]=text
        print(imname)
        i+=1


        #transfer(images,text)
json_object = json.dumps(res, indent = 4)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)