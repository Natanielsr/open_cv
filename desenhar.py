import numpy as np
import cv2 as cv

#cria uma imagem preta de 512 x 512
img = np.zeros((512, 512, 3), np.uint8)

#desenha uma linha azul na diagonal na largura de 5px
#1 parametro imagem que vai alterar
#2 parametro ponto 1 da reta
#3 parametro ponto 2 da reta,
#4 parametro cor da reta
#5 largura da reta  
cv.line(img, (0,0), (511,511), (255,0,0), 5)

#desenha um retangulo
cv.rectangle(img, (384,0), (510,128), (0,255,0), 3)

#desenha um circulo
#1 parametro imagem que vai alterar
#2 parametro centro do circulo
#3 parametro raio do circulo
#4 parametro cor do circulo
#5 largura do traço
cv.circle(img, (447,63), 63, (0,0,255), -1)

#desenha uma elipse
cv.ellipse(img, (256, 256), (100,50), 0, 0, 180, 255, -1)

#desenhar um poligono
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

#adiconar texto
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow("Desenhos", img)
cv.waitKey(0)
cv.destroyAllWindows()
