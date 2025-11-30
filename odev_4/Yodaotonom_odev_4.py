# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 23:20:16 2025

@author: Ulaş
"""

import cv2
import time

yüz_algilayici = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

kamera = cv2.VideoCapture("yüz_algilama_3.mp4")

merkezler = []

baslangic_zamani = None
saniye = 0


while True:
    ret,frame = kamera.read()
    
    if not ret:
        break
    
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    yüzler = yüz_algilayici.detectMultiScale(gri,scaleFactor =1.1,minNeighbors =5,minSize=(30,30))
    
    if len(yüzler) > 0:
        if baslangic_zamani is None:
            baslangic_zamani = time.time()
            
        saniye = int(time.time() - baslangic_zamani)
    else:
        baslangic_zamani = None
        saniye = 0    
    
    for (x, y, w, h) in yüzler:
        
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 0)
        
        x_merkezi = x + w // 2
        y_merkezi = y + h // 2
        
        merkezler.append((x_merkezi, y_merkezi))
        
        if len(merkezler) > 60:
            merkezler.pop(0)
        
        cv2.putText(frame, f"({x_merkezi},{y_merkezi})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,255,0), 1)
        
        for i in range(1,len(merkezler)):
            cv2.line(frame,merkezler[i-1],merkezler[i], (0,255,0), 2)
        
        
    cv2.putText(frame, f"(Saniye: {saniye})",(frame.shape[1]-150 , 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        
    cv2.imshow("Yüz Algılama", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Yüz Algılama İşleminiz Bitmiştir.")
            break
        
kamera.release()
cv2.destroyAllWindows()
    