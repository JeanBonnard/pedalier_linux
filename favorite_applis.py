#!/usr/bin/python
#-*-coding:utf-8 -*

from serial import Serial
import subprocess
import time

serial_port = Serial(port='/dev/ttyUSB0', baudrate=9600)

bt = serial_port.readline()
chaine = bt.decode('ascii')

continuer = 1

while continuer:
	bt = serial_port.readline()
	chaine = bt.decode('ascii')
	if chaine[:7] == "bouton1" :
		subprocess.Popen(["thunderbird"])
	elif chaine[:7] == "bouton2" :
		subprocess.Popen(["firefox"])
		time.sleep(2)
		subprocess.call("xdotool key "+"ctrl+l", shell = True)
		subprocess.call("xdotool type "+"www.facebook.fr", shell = True)
		subprocess.call("xdotool key "+"Return", shell = True)
	elif chaine[:7] == "bouton3" :
		subprocess.Popen(["firefox"])
		time.sleep(2)
		subprocess.call("xdotool key "+"ctrl+l", shell = True)
		subprocess.call("xdotool type "+"www.twitter.fr", shell = True)
		subprocess.call("xdotool key "+"Return", shell = True)

