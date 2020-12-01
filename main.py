#Machine Vision and Robotics Course Project
#Fire detection using Image Processing
#import modules
import cv2#Computer vision module for video capture and image processing
import numpy as np#Python numbers module for matrix manipulation
import time#time module to measure time for pauses
import winsound# windows sound module for alarm
v=cv2.VideoCapture(0)#Capture live video using camera 0 (default webcam) and store values in v
time.sleep(2)#pause for 2 seconds
fdc=cv2.CascadeClassifier(r'C:\python\python36\fire_detection.xml')#Load generated cascade classifier into fdc
frequency = 2500#Define alarm frequency as 2500 Hz
duration = 500#Define alarm duration as 500 ms
while(1):#Loop code continously
        d,i=v.read()#Get frame from video capture. If frame is obtained, store TRUE in d and store image matrix in i
        print(i.shape)#Print image dimensions in console
        fire=fdc.detectMultiScale(i,1.3,9)#Use detectMultiScale function to detect objects, passing image,scale factor and minNeighbors as parameters
        print(fire)#Print dimensions of detected object (fire) matrix in console

        if(len(fire)>=1):#If 1 or more objects (fires) are detected
         for x,y,w,h in fire:#Store coordinates of upper-left corner in x and y, and widht and height in w and h
              font=cv2.FONT_HERSHEY_SIMPLEX#Define font
              cv2.putText(i,'FIRE DETECTED',(x-w,y-h),font,0.5,(0,255,255),2,cv2.LINE_AA)#Display "FIRE DETECTED" test
              cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),2)#Display rectangle around fire
              time.sleep(0.2)#Pause of  for 0.2 seconds
              winsound.Beep(frequency, duration)#Sound alarm
        cv2.imshow('image',i)#Display processed image on screen

        if(len(fire)>=1):#If 1 or more objects (fires) are detected
           
           print('FIRE DETECTED')#Print "FIRE DETECTED" to console
        k=cv2.waitKey(5)#If keypress is detected, wait 5 seconds
        if(k==ord('q')):#If detected key is q
                cv2.destroyAllWindows()#Stop all processing
                break#Exit loop
                
