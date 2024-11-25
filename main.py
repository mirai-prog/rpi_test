import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


print('[INFO] Red led on')
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
print('[INFO] Red led off')
GPIO.output(17, GPIO.LOW)

#------
GPIO.setup(27,GPIO.OUT)
print('[INFO] Yellow led on')
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
print('[INFO] Yellow led off')
GPIO.output(27, GPIO.LOW)

#--------
GPIO.setup(22,GPIO.OUT)
print('[INFO] Yellow led on')
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
print('[INFO] Yellow led off')
GPIO.output(22, GPIO.LOW)

