#!/usr/bin/env python

import time
import pifacedigitalio as pfio
import os

pfio.init()

print("Ultrasonic Measurement")
do=1
while(do==1):
    do = 0
    
    PFIO_TRIGGER = 2
    PFIO_ECHO = 0
    
    # Set trigger to False (Low)
    pfio.digital_write(PFIO_TRIGGER,0)
    
    # Allow module to settle
    time.sleep(1)
    os.system('clear')
    # Send 10us pulse to trigger
#    pfio.digital_write(PFIO_TRIGGER, 1)
    time.sleep(0.0001)
    pfio.digital_write(PFIO_TRIGGER, 0)
    start = time.time()

    print (pfio.digital_read(PFIO_ECHO))
    
    while pfio.digital_read(PFIO_ECHO)==0:
      pfio.digital_write(4,1)
      pfio.digital_write(4,0)
    print ("START : %.10f" % start)
    
#    while pfio.digital_read(PFIO_ECHO)==0:
    while(True):
        pfio.digital_write(6,1)
        stop = time.time()
	print("STOP : %.10f" % stop)
	print(pfio.digital_read(PFIO_ECHO))
        pfio.digital_write(6,0)
	time.sleep(.3)
    
    # Calculate pulse length
    elapsed = stop-start
    print ( "Elapsed : %.10f" % elapsed)
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000
    
    # That was the distance there and back so halve the value
    distance = distance / 2
    
    print ("Distance : %.1f" % distance)

pfio.deinit()
