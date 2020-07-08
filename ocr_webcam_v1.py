import cv2
import pytesseract as ocr
from PIL import Image


#Tesseract reading in Portuguese!; 
    #Download portuguese or others trained data(https://tesseract-ocr.github.io/tessdoc/Data-Files);
    #to install, first do "sudo find / -name 'tessdata'" (Ubuntu 20.04) to find the right folder
    #do "sudo cp -r por.traineddata tessdata_folder", In my case it was: 
    #"sudo cp -r por.traineddata /usr/share/tesseract-ocr/4.00/tessdata";

#It can read some simple handmade texts shown in the webcam, stills kinda unstable

video = cv2.VideoCapture(0)
img_counter = 0
videoNpArr = cv2.imread("test-image.jpg")

while True:


    check, frame = video.read()

    

    phrase = ocr.image_to_string(frame, lang='por')

    
    #Put the text read on the webcam 
    cv2.putText(frame, phrase, (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))

    #Windows creation
    cv2.imshow("Main frame thing", frame)

    #Trackbar creation
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('i'):
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1


video.release()
cv2.destroyAllWindows()
