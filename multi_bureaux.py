#!/usr/bin/python
#-*-coding:utf-8 -*

from serial import Serial
import subprocess

serial_port = Serial(port='/dev/ttyUSB0', baudrate=9600)

bt = serial_port.readline()
chaine = bt.decode('ascii')

continuer = 1

while continuer:
	bt = serial_port.readline()
	chaine = bt.decode('ascii')
	if chaine[:7] == "bouton1" :
		subprocess.call("xdotool key "+"ctrl+alt+Up", shell=True)
	elif chaine[:7] == "bouton2" :
		subprocess.call("xdotool key "+"ctrl+alt+Left", shell=True)
	elif chaine[:7] == "bouton3" :
		subprocess.call("xdotool key "+"ctrl+alt+Right", shell=True)

