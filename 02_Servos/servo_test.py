#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

p = GPIO.PWM(25, 50);

print("Initialising...")
p.start(5.5)
time.sleep(2);
print("done")


#for dc in range(0, 11, 1):
#	p.ChangeDutyCycle(dc)
#	print dc
#        time.sleep(1)

while (True):
	dc = input ("Enter a value between 1 and 10 : ")
	if dc == 'end':
		p.stop()
		GPIO.cleanup()
	p.ChangeDutyCycle(dc)

p.stop()
GPIO.cleanup()

#p.start(10)
#print ("MIN waiting 2 sec ...")
#time.sleep(2)

#p.start(99)
#print("MAX done")
#time.sleep(2)

#p.stop()
#GPIO.cleanup()
