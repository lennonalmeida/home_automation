import RPi.GPIO as GPIO
import time
gpio = 2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio,GPIO.OUT)

while True:
    print "LED on"
    GPIO.output(gpio,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(gpio,GPIO.LOW)
    time.sleep(1)
