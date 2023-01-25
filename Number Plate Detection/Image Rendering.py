from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import imutils
import cv2

from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil
filename = r'C:\Users\heman\Downloads\abc.mp4'

if os.path.exists('output'):
    shutil.rmtree('output')

os.makedirs('output')

cap = cv2.VideoCapture(filename)
# cap = cv2.VideoCapture(0)
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('window-name',frame)
        cv2.imwrite("./output/frame%d.jpg" % count, frame)
        count = count + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
