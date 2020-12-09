
import cv2
import requests
from time import sleep
import RPi.GPIO as GPIO


url = 'https://emostaxi.com'
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()

while True:
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                     0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:

            x = requests.get(url, params = {"data": data})
            res = x.text
            if (res == "1"):
                GPIO.output(17,GPIO.HIGH)    
                sleep(5)
                GPIO.output(17,GPIO.LOW)
            else:
                 GPIO.output(26,GPIO.HIGH)    
                 sleep(5)
                 GPIO.output(26,GPIO.LOW)
            
    # display the image preview
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()
