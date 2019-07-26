#led.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4,True) #1 or high
time.sleep(1)
GPIO.output(4, False) #0 or low
