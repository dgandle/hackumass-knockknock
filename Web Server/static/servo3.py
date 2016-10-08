import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

var = True
while(var):
	pwm.ChangeDutyCycle(2.5)
	sleep(2)
	var = False  