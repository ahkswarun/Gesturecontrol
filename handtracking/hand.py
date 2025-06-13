import cv2
import mediapipe as mp
import time


cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands(False)


while True:
    success,img=cap.read()
    imgRBG=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRBG)
    
    
    cv2.imshow('Camera',img)
    cv2.waitKey(1)
