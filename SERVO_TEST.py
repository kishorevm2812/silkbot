import time 
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def servo1(i):
    servoPIN = 12
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)
    p.start(0)
    p.ChangeDutyCycle(i)
    time.sleep(1)

servo1(2)
time.sleep(3)
servo1(6)
time.sleep(3)
servo1(10)
time.sleep(3)
servo1(6)
time.sleep(3)
