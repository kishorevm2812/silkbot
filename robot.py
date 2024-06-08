import time 
import RPi.GPIO as GPIO                    #Import GPIO library                            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

IN3=16
IN4=18

GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.output(IN3,False)
GPIO.output(IN4,False)
def FORWARD():
    print("FORWARD")
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    time.sleep(9)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)





