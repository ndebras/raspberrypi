#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time

GPIO.setmode(GPIO.BCM)
GREEN_LED = 25
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

C = 0
while C<20:
	print "A"
	GPIO.output(GREEN_LED, True)
	GPIO.output(RED_LED, False)
	time.sleep(1)
	print "B"
	GPIO.output(GREEN_LED, False)
	GPIO.output(RED_LED, True)
	time.sleep(1)
	C = C + 1
GPIO.cleanup()
