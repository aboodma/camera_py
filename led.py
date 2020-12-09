import RPi.GPIO as GPIO
from time import sleep
class Led:

    def red_led(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(17,GPIO.HIGH)    
        sleep(5)
        GPIO.output(17,GPIO.LOW)

    def greenLed(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,GPIO.HIGH)    
        sleep(5)
        GPIO.output(26,GPIO.LOW)