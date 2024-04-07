import numpy as np
import cv2
import time


from pushbullet import Pushbullet
import pygame


#input audio --This part of code was running separately but when merged with other lines of code it does not work properly 
'''

import pyshine as ps

audio,context = ps.audioCapture(mode='send')
ps.showPlot(context,name='pyshine.com')
while True:
	frame = audio.get()
'''	
   

#giving the alert message  {working very well}

API_KEY ="o.2HXZhtk1IqTEKyKPWKRN5sUIDvPA3t9b"
file ="alertmsg.txt"

with open(file, mode='r') as f:
    text = f.read()
    pb =Pushbullet(API_KEY)
    push = pb.push_note('She needs help', text)
    
time.sleep(10)

#playing alert sound {working well}
pygame.mixer.init()
pygame.mixer.music.load('sound1.wav')
pygame.mixer.music.play()

input('enter to exit the sound : ')


#video streaming { working well}
#live video will be coming from phone through the given url
cap=cv2.VideoCapture("http://10.1.3.19:8080/video")


while True :
    _, frame=cap.read()
    

    cv2.imshow('livestream',frame)

    if cv2.waitKey(1)==ord('q'):  #press q to exit the video streaming
        break

cap.release()
cv2.destroyAllWindows
