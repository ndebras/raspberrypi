#!/usr/bin/env python

#import piface.pfio as pfio
import pifacedigitalio as pfio
import time

pfio.init()

while(True):
	print ("================")
	print ("Turn Left")
	print ("Motor 0 => on")
	print ("Motor 1 => off")
	pfio.digital_write(0,1)
	pfio.digital_write(1,0)
	time.sleep (.1)
	
	print ("================")
	print ("Turn Right")
	print ("Motor 0 => off")
	print ("Motor 1 => on")
	pfio.digital_write(0,0)
	pfio.digital_write(1,1)
	time.sleep (.1)
	
	print ("================")
	print ("STOP")
	print ("Motor 0 => off")
	print ("Motor 1 => off")
	pfio.digital_write(0,0)
	pfio.digital_write(1,0)
	time.sleep (3)
