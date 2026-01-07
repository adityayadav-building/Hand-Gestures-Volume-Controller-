
import cv2
import mediapipe as mp
import numpy as np
import time
import HandTrack as htm
import math 

import subprocess

def set_volume(percentage):
    # Clamp between 0 and 100
    percentage = max(0, min(100, percentage))
    # Run AppleScript via osascript
    subprocess.run(["osascript", "-e", f"set volume output volume {percentage}"])

def get_volume():
    # Returns the current volume as an integer 0–100
    result = subprocess.check_output(
        ["osascript", "-e", "output volume of (get volume settings)"]
    )
    return int(result.strip())

minVol = 0
maxVol = 100
volBar = 400


detector = htm.handDetector(detectionCon=0.5)



wCam, hCam = 640, 480
pTime=0
cTime=0


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    successs, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
      
      x1 , y1 = lmList[4][1], lmList[4][2]
      x2 , y2 = lmList[8][1], lmList[8][2]
      cx , cy = (x1 + x2)//2 , (y1 + y2)//2



      print(lmList[4], lmList[8])
      cv2.circle(img , (x1 , y1) , 15 , (0,154,0) , cv2.FILLED)
      cv2.circle(img , (x2 , y2) , 15 , (0,154,0) , cv2.FILLED)
      cv2.line(img , (x1 , y1) , (x2 , y2) , (134,0,255) , 3)
      cv2.circle(img , (cx , cy) , 15 , (39,82,155) , cv2.FILLED)

      length = math.hypot(x2 - x1 , y2 - y1)
      print(length)

      vol = np.interp(length , [25 , 200] , [minVol , maxVol])
      volBar = np.interp(length , [25 , 200] , [400 , 150]) 
      print(int(vol))
      set_volume(int(vol))
      v= get_volume()
      cv2.putText( img ,  f'Vol: {int(vol)}' , (40,130) , cv2.FONT_HERSHEY_PLAIN , 2 , (0,0,255) , 3)
      
      # range 25 - 200
        # vol range 0 - 100 

      if length < 25:
        cv2.circle(img , (cx , cy) , 15 , (0,0,200) , cv2.FILLED)




    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.rectangle(img , (50 ,150) , (85, 400) , (0,255,0) , 3)
    cv2.rectangle(img , (50, int(volBar)) , (85, 400) , (0,255,0) , cv2.FILLED)

    

    cv2.putText( img ,  f'FPS: {int(fps)}' , (40,70) , cv2.FONT_HERSHEY_PLAIN , 2 , (223,0,0) , 3)

    cv2.imshow("Image", img)

    cv2.waitKey(1)