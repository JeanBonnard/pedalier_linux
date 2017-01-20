#!/usr/bin/python
#-*-coding:utf-8 -*
 
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
		interface.add_from_file('/home/jean/Arduino/projet_pedalier/FootClick.glade')
		interface.connect_signals(self)
		self.Process = 0
		self.state = 0

	def on_mainWindow_destroy(self, widget):
		Gtk.main_quit()
	
	def on_multiBureaux_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/multi_bureaux.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/multi_bureaux.py"], shell=False)
				self.state = 1

	def on_copierColler_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/copier_coller.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/copier_coller.py"], shell=False)
				self.state = 1

	def on_favorite_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/favorite_applis.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/favorite_applis.py"], shell=False)
				self.state = 1

	def on_media_clicked(self, widget):
		if self.state == 0:
			subprocess.Popen(["vlc"])
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/media.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				subprocess.Popen(["vlc"])
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/media.py"], shell=False)
				self.state = 1

	def on_son_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/son.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/son.py"], shell=False)
				self.state = 1

	def on_buttonStop_clicked(self, widget):
		self.Process.kill()
		self.state=0

if __name__ == "__main__":	
	HelloWorld()
	Gtk.main()
