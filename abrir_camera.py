import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
   # Capturar frame por frame
   ret, frame = cap.read()

   # Nossa operação no frame vai aqui
   gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

   #mostra o resultado do frame
   cv.imshow('frame', gray)
   if(cv.waitKey(1) & 0xFF == ord('q')):
      break

#quando tudo estiver feito, entregue a captura
cap.release()
cv.destroyAllWindows()