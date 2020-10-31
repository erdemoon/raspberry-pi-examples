import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

print ("Please enter a number")

MATRIX = [ [1,2,3],
	   [4,5,6],
	   [7,8,9],
	   ['*',0,'#'] ]

ROW = [7,11,13,15]
COL = [12,16,18]


for j in range(3):
	GPIO.setup(COL[j], GPIO.OUT)
	GPIO.output(COL[j], 1)

for i in range(4):
	GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
	while(True):
		for j in range(3):
			GPIO.output(COL[j],0)
			for i in range(4):
				if GPIO.input(ROW[i]) == 0:
					print (MATRIX[i][j])
					time.sleep(0.5)
					if type(MATRIX[i][j]) == int:
						for x in range(MATRIX[i][j]):
							GPIO.output(4, True)
							time.sleep(0.5)
							GPIO.output(4, False)
							time.sleep(0.5)
					else:
						print ("PLease enter a number.")
					while (GPIO.input(ROW[i]) == 0):
						pass
			GPIO.output(COL[j],1)

except KeyboardInterrupt:
	GPIO.cleanup()



