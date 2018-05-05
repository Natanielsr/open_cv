import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

cap = cv.VideoCapture(0)

def inicia():

   while(True):
      loop()
      if(cv.waitKey(1) & 0xFF == ord('q')):
         break

   #quando tudo estiver feito, entregue a captura
   cap.release()
   cv.destroyAllWindows()

def loop():
   # Capturar frame por frame
   ret, frame = cap.read()

   # Nossa operação no frame vai aqui
   gray = detectar_rosto(frame)

   #mostra o resultado do frame
   cv.imshow('frame', frame)
   cv.imshow('gray', gray)

def detectar_rosto(frame):
   gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

   faces = face_cascade.detectMultiScale(gray, 1.3, 5)

   for (x, y, w, h) in faces:
      cv.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = frame[y:y+h, x:x+w]
      detectar_olhos(roi_gray, roi_color)   

   return gray
   
def detectar_olhos(roi_gray, roi_color):
   eyes = eye_cascade.detectMultiScale(roi_gray)
   if(len(eyes) == 0):
      print('Olhos fechados', cv.getTickCount())

   for (ex, ey, ew, eh) in eyes:
      cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0),2)

inicia()