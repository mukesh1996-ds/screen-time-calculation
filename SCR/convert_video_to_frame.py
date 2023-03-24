import cv2
import imutils
import math 
import matplotlib.pyplot as plt

count = 0
videoFile = r"Data\Video_clip.mp4"
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename =r"D:\My Learning\Major Projects\Deep Larning\screen-time-calculation\DataFrames\frame%d.jpg" % count;count+=1
        cv2.imwrite(filename, frame)
cap.release()
print ("Done!")

