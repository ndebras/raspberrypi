#!/usr/bin/env python

#import piface.pfio as pfio
import pifacedigitalio as pfio
import time

pfio.init()

while(True):
	pfio.digital_write(0,1)
	time.sleep (1)
	pfio.digital_write(0,0)
	time.sleep (1)

