import cv2
import numpy as np 

image = cv2.imread('yss.png')
dc={'0':(37, 160, 323, 254,),'3':(217, 235, 252, 250),'2':(217, 190, 252, 205),'3':(34, 220, 333, 235)}
#dc={'Store_name':(68, 34, 177, 25),'GSTIN':(72, 82, 169, 19),'Address':(10, 108, 286, 53),'InvoiceNo': (175, 179, 78, 14),'DateTime':(152, 198, 120, 15),'Customer_Dtails':(168, 216, 95, 22),'Item1':(15, 293, 289, 25),'Item2':(13, 318, 292, 22),'Total_Amount':(225, 374, 42, 17) ,'MOP':(217, 410, 61, 17),'Terms_and_conditions':(8, 450, 266, 55)}
bounding_boxes =[]
for j in dc.values():
    bounding_boxes.append(j)

num = 0
for box in bounding_boxes:
    x,y,w,h = box
    ROI = image[y:y+h, x:x+w]
    k=(list(dc.keys())[list(dc.values()).index(box)])
    cv2.imwrite('special/{}.png'.format(k), ROI)
    num += 1
    cv2.imshow('ROI', ROI)
    cv2.waitKey()