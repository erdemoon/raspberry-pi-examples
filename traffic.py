import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

for i in range(2):
	GPIO.output(4, True)
	time.sleep(6)
	GPIO.output(17, True)
	time.sleep(3)
	GPIO.output(4, False)
	GPIO.output(17, False)
	GPIO.output(27, True)
	time.sleep(6)
	GPIO.output(27, False)
	GPIO.output(17, True)
	time.sleep(3)
	GPIO.output(17, False)

GPIO.cleanup()
