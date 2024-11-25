import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

print('[INFO] Red led on')
GPIO.output(18,GPIO.HIGH)
time.sleep(1)

print('[INFO] Red led off')
GPIO.output(18, GPIO.LOW)

GPIO.setup(17,GPIO.OUT)

print('[INFO] Yellow led on')
GPIO.output(17,GPIO.HIGH)
time.sleep(1)

print('[INFO] Yellow led off')
GPIO.output(17, GPIO.LOW)

