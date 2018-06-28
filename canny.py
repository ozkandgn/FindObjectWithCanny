import cv2
import numpy as np
from matplotlib import pyplot as plt

class Img(object):
    def __init__(self):
        self.name=0
        
    def Draw(self,canny,first):
        minX=255
        minY=255
        maxX=0
        maxY=0
        for i in range(len(canny)):
            for j in range(len(canny[i])):
                if canny[i][j] == 255:
                    if minY > j:
                        minY=j
                    elif maxY < j:
                        maxY=j
                    if minX > i:
                        minX=i
                    elif maxX < i:
                        maxX=i
        cv2.rectangle(first, (minY, minX), (maxY, maxX), (255,0,0), 2)
        cv2.imshow("image-"+str(self.name),first)
        #self.name+=1
        cv2.imshow("canny-"+str(self.name),canny)
        #self.name+=1
        
    def Image(self,frame):    
        frame = cv2.resize(frame,(300,240), interpolation = cv2.INTER_CUBIC)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = cv2.Canny(image,350,620)
        self.Draw(image,frame)
        
    def Video(self):
        cam = cv2.VideoCapture('videos/video2.mp4')
        while True:
            try:
                ret,frame=cam.read()
                self.Image(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except:
                break
Img().Video()
