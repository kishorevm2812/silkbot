import RPi.GPIO as gpio
import time
import RPi.GPIO as GPIO                    #Import GPIO library                            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

IN1=21
IN2=20

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)

GPIO.output(IN1,False)
GPIO.output(IN2,False)
DT =23#27
SCK=24 #17
relay1=25
relay2=2
HIGH=1
LOW=0
sample=0
val=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(SCK, gpio.OUT)
gpio.setup(relay1, gpio.OUT)
gpio.setup(relay2, gpio.OUT)
gpio.setup(relay1, False)
gpio.setup(relay2, False)
def readCount():
  i=0
  Count=0
 # print Count
 # time.sleep(0.001)
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)
  while gpio.input(DT) == 1:
      i=0
  for i in range(24):
        gpio.output(SCK,1)
        Count=Count<<1
        gpio.output(SCK,0)
        time.sleep(0.001)
        if gpio.input(DT) == 0: #0
            Count=Count+1
            #print Count
        
  gpio.output(SCK,1)
  Count=Count^0x800000
  time.sleep(0.001)
  gpio.output(SCK,0)
  return Count  

print(" test")
sample= readCount()
print(sample)
flag=0
count= readCount()
print(count)
cnt=0
w=0
def load():
#while True:
    print('start measure')
    #time.sleep(4)
    count= readCount()

    w=0

    w=abs((count-sample)/470)
##    w=w*2.095
##    w=w-3
#     if w < 7:
#       w=0
    w=round(w)
    print (w,"g")
    time.sleep(0.5)
    if w>2:
        print('female')
        gpio.setup(relay2, True)
        time.sleep(4)
        gpio.setup(relay2, False)
        time.sleep(2)
        GPIO.output(IN1,True)
        GPIO.output(IN2,False)
        gpio.setup(relay1, True)
        time.sleep(4)
        gpio.setup(relay1, False)        
    if w<= 2 and w>0:
        print('male')
        gpio.setup(relay2, True)
        time.sleep(4)
        gpio.setup(relay2, False)    
        GPIO.output(IN1,True)
        GPIO.output(IN2,False)