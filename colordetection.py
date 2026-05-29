import cv2
from PIL import Image
import numpy as np
def bounds(color):
    c=np.uint8([[color]])
    hsv=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    hue=hsv[0][0][0]
    # wider hue range (±15) to catch more shades
    # lower saturation floor (40) to catch pale/pastel shades
    # lower value floor (40) to catch darker shades
    lowerlimit=np.array([max(hue-15,0), 40, 40],dtype=np.uint8)
    upperlimit=np.array([min(hue+15,179), 255, 255],dtype=np.uint8)
    return lowerlimit,upperlimit


yellow=[0,255,255]
lowlimit,upplimit=bounds(yellow)
web=cv2.VideoCapture(0)
while True:
    ret,frame=web.read()
    hsvframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsvframe,lowlimit,upplimit)
    pilmask=Image.fromarray(mask)
    bbox=pilmask.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    cv2.imshow('COLORDETECTOR',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break



web.release()
cv2.destroyAllWindows()