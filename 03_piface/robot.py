#!/usr/bin/env python

import time, threading
import pifacedigitalio as pfio
import curses

class Robot():
    def __init__(self,pfio):
        pfio.init()
        self.pfio = pfio
    
    def initialize(self):
        pass
    
    def stopWheels(self):
        pfio.digital_write(0,0)
        pfio.digital_write(1,0)
        
    def moveForward(self):
        pfio.digital_write(0,1)
        pfio.digital_write(1,1)
        
    def moveBackward(self):
        pass    #TODO : I need a H-bridge to make that work
    
    def turnLeft(self):
        self.pfio.digital_write(0,1)
        self.pfio.digital_write(1,0)
        
    def turnRight(self):
        pfio.digital_write(0,0)
        pfio.digital_write(1,1)
        
    def __destroy(self):
        time.sleep(1);
        self.pfio.deinit();
        self.__destroy();

robot = Robot(pfio);

#CURSES
stdscr = curses.initscr()

curses.noecho()
curses.cbreak();
previousMotorState = "STOP"
motorState = "STOP"

while True:
    stdscr.nodelay(0)
    char = stdscr.getch()
    
    if char == -1 :
        stdscr.addstr(1,1,"NO KEY")
        robot.stopWheels
        motoState = "STOP"
        
    if char == 113: 
        break  # q
    elif char == ord("d"): 
        stdscr.addstr(1,1,"RIGHT")
        motorState = "RIGHT"
        if previousMotorState != motorState:    
            previousMotorState = motorState
            robot.turnRight()
        time.sleep(.1)
    elif char == ord("a"): 
        stdscr.addstr(1,1,"LEFT")
        motorState = "LEFT"
        if previousMotorState != motorState:    
            previousMotorState = motorState
            robot.turnLeft()
        time.sleep(.1)
    elif char == ord("w"): 
        stdscr.addstr(1,1,"UP")
        motorState = "UP"
        if previousMotorState != motorState:    
            previousMotorState = motorState
            robot.moveForward()
        time.sleep(.1)
    elif char == ord("s"): 
        stdscr.addstr(1,1,"DOWN")
        motorState = "DOWN"
        robot.stopWheels()
    else: 
        robot.stopWheels()
        
    if previousMotorState != motorState:
        
        previousMotorState = motorState
      
    
curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
pfio.deinit()