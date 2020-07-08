import cv2
import pytesseract as ocr
from PIL import Image


#Consegui ler uns comando básico do tipo "liga" ou "desliga", e "esquerda" ou "direita", mas tá bem ruim e instável

video = cv2.VideoCapture(0)
img_counter = 0
videoNpArr = cv2.imread("test-image.jpg")

while True:


    check, frame = video.read()

    #Tesseract lendo texto, em Português!; 
    #Baixar o trained data em ptbr (https://tesseract-ocr.github.io/tessdoc/Data-Files);
    #Caso não saiba onde, dá um "sudo find / -name "tessdata" (Ubuntu 20.04) para achar a pasta onde tem que instalar a 
    #trained data em ptbr;
    #aí só dar um "sudo cp -r por.traineddata pasta do tessdata" No meu caso foi: 
    #"sudo cp -r por.traineddata /usr/share/tesseract-ocr/4.00/tessdata";

    phrase = ocr.image_to_string(frame, lang='por')

    
    #colocando o que foi lido no video recebido da webcam
    cv2.putText(frame, phrase, (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))

    #criação da janela
    cv2.imshow("Main frame thing", frame)

    #criação da trackbar
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('i'):
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1


video.release()
cv2.destroyAllWindows()