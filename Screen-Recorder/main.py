from PIL import ImageGrab
import numpy as np
import cv2 as cv
import datetime
from win32api import GetSystemMetrics

#  Getting screen resolution
#  Uncomment for dynamic screen resolution
'''
screenW = GetSystemMetrics(0)
screenH = GetSystemMetrics(1)
'''
screenH = 1080
screenW = 1920
## CAPTURING SCREEN
#  Encoding for video
fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
fielname = f'{time_stamp}.mp4'
cap_video = cv.VideoWriter(fielname, fourcc, 20.0, (screenW, screenH))

##CAPTURING WEBCAM
cap = cv.VideoCapture(0)


while True:
        img = ImageGrab.grab(bbox=(0, 0, screenW, screenH))
        imgToArray = np.array(img)
        img = cv.cvtColor(imgToArray, cv.COLOR_BGR2RGB)
        ret,frame = cap.read()
        frameH,frameW, _ = frame.shape
        img[:frameH,:frameW,:] = frame[:frameH,:frameW,:]


        cv.imshow('Capture', img)
        
        cap_video.write(img,)
        if cv.waitKey(5) == ord('q'):
            break
cap.release()
cv.destroyAllWindows()
