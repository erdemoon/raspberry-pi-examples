import RPi.GPIO as GPIO,time,sys

GPIO.setmode(GPIO.BCM)
LED=[21,20,16,19,26,13,6]
GT=0.25
WIN=[]
COUNT=[1]
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for i in range(7):
	GPIO.setup(LED[i], GPIO.OUT)
	GPIO.output(LED[i], False)

while 0:
	if len(WIN)==len(COUNT):
		GT=GT-0.030
		COUNT.append(1)
		time.sleep(0.5)
		GPIO.output(19, False)
		time.sleep(0.5)
		GPIO.output(19,True)
		time.sleep(0.5)
		GPIO.output(19, False)
		for a in range(len(WIN)):
			GPIO.output(LED[a], True)
			time.sleep(.5)
		for x in range(len(WIN)):
			GPIO.output(LED[x], False)

	if len(WIN)==7:
		break
	for i in reversed(range(7)):
		GPIO.output(LED[i], True)

		if i==3:
			if GPIO.input(5)==False:
				WIN.append(1)
				break
		time.sleep(GT)
		GPIO.output(LED[i],False)

	if len(WIN)==len(COUNT):
		continue

	for i in range(1,6):
		GPIO.output(LED[i],True)
		if i==3:
			if GPIO.input(5)==False:
				WIN.append(1)
				break
		time.sleep(GT)
		GPIO.output(LED[i],False)
print("You won!!")
for f in range(10):
	for c in reversed(range(7)):
		GPIO.output(LED[c],True)
		time.sleep(.15)
	for d in range(7):
		GPIO.output(LED[d],True)
		time.sleep(.15)
		GPIO.output(LED[d],False)
	for e in range(6):
		GPIO.output(LED[e],True)
		time.sleep(.15)
		GPIO.output(LED[e],False)
		
