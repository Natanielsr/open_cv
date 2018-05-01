import cv2 as cv

img1 = cv.imread('imagem.jpg')

#retorna o numero de clock-cycles incial
e1 = cv.getTickCount()

#processamento
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)

#retorna o numero de clock-cycles final
e2 = cv.getTickCount()

# encontra o tempo de execução
# getTickFrequency retorna o numero de clock-cycles por segundo


print("Numero de clocks i ",e1)
print("Numero de clocks f ", e2)
print("Clocks por segundo", cv.getTickFrequency())

t = (e2 - e1)/cv.getTickFrequency()

print("Processado em {} segundos".format(t) )