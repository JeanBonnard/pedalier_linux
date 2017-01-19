#!/usr/bin/python 
import pygtk
pygtk.require("2.0")
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject
from serial import Serial
import subprocess
import os
import signal
import time

class HelloWorld:
	def __init__(self):
		interface = Gtk.Builder()
		interface.add_from_file('FootClick.glade')
		interface.connect_signals(self)
		self.Process = 0
		self.state = 0

	def on_mainWindow_destroy(self, widget):
		Gtk.main_quit()
	
	def on_myButton_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/lecture_donnees.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 0

	def on_buttonStop_clicked(self, widget):
		time.sleep(5)
		self.Process.terminate()

if __name__ == "__main__":	
	HelloWorld()
	Gtk.main()
