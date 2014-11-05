#!/usr/bin/python
import os,time,re,sys;

#Rotating the display
normal = 'xrandr --output LVDS1 --rotate normal'
left = 'xrandr --output LVDS1 --rotate left'
right = 'xrandr --output LVDS1 --rotate right'

#Reading data from accelerometer (x-axis)
def readAccelerometer():
	f = open('/sys/devices/platform/hdaps/position','r')
	return int(re.search('[-]*[0-9]+', f.readline()).group(0))

while True:
	time.sleep(0.1)
	data = abs(readAccelerometer())
	if (data < 400):
		os.system(left)
	elif (data > 590):
		os.system(right)
	else:
		os.system(normal)