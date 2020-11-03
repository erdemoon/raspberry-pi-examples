import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

out = [2,3,4,14,15,18,17,27]

sleepTime = 0.1

for i in range(8):
	GPIO.setup(out[i], GPIO.OUT)
GPIO.output(15, False)
while 1:
	GPIO.output(27, True)
	time.sleep(sleepTime)
	GPIO.output(17, True)
	GPIO.output(27, False)
	time.sleep(sleepTime)
	GPIO.output(18, True)
	GPIO.output(17, False)
	time.sleep(sleepTime)
	GPIO.output(14,True)
	GPIO.output(18, False)
	time.sleep(sleepTime)
	GPIO.output(4, True)
	GPIO.output(14, False)
	time.sleep(sleepTime)
	GPIO.output(3, True)
	GPIO.output(4, False)
	time.sleep(sleepTime)
	GPIO.output(2, True)
	GPIO.output(3, False)
	time.sleep(sleepTime)
	GPIO.output(14, True)
	GPIO.output(2, False)
	time.sleep(sleepTime)
	GPIO.output(14, False)

GPIO.cleanup()

