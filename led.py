import RPi.GPIO as GPIO
from time import sleep
class Led:


 def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(26,GPIO.OUT)

def redLed():
    GPIO.output(17,GPIO.HIGH)    
    sleep(5)
    GPIO.output(17,GPIO.LOW)

def greenLed():
    GPIO.output(26,GPIO.HIGH)    
    sleep(5)
    GPIO.output(26,GPIO.LOW)