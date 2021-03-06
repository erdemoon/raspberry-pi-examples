import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 23
GPIO.setup(led, GPIO.OUT)

with open("mors2.txt") as my_file:
    mors1 = my_file.read()
mors = json.loads(mors1)


def dot():
    GPIO.output(led, 1)
    time.sleep(0.2)
    GPIO.output(led, 0)
    time.sleep(0.2)


def line():
    GPIO.output(led, 1)
    time.sleep(0.4)
    GPIO.output(led, 0)
    time.sleep(0.2)


input1 = input("Enter a text: ")
print(f"The entered text: {input1}!")
for char in input1:
    for symbol in mors[char.upper()]:
        if symbol == "-":
            line()
        elif symbol == ".":
            dot()
        else:
            time.sleep(0.2)
    time.sleep(0.5)

GPIO.cleanup()
