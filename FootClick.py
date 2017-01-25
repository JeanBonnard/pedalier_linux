#!/usr/bin/python
#-*-coding:utf-8 -*
<<<<<<< HEAD

'''__________________________________________________import des differentes librairies utile au programme__________________________________________________________'''

=======
 
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
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
<<<<<<< HEAD
import Tkinter
import tkMessageBox

'''__________________________________________________class HelloWorld, atribution des actions aux boutons__________________________________________________________'''
=======
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477

class HelloWorld:
	def __init__(self):
		interface = Gtk.Builder()
<<<<<<< HEAD
		self.pwd = subprocess.Popen(["pwd"], stdout = subprocess.PIPE, shell = True)
		self.chemin = self.pwd.stdout.read()[:-1]
		interface.add_from_file(self.chemin+'/FootClick.glade')
		interface.connect_signals(self)
		self.Process = 0
		self.state = 0
		
=======
		interface.add_from_file('/home/jean/Arduino/projet_pedalier/FootClick.glade')
		interface.connect_signals(self)
		self.Process = 0
		self.state = 0

>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
	def on_mainWindow_destroy(self, widget):
		Gtk.main_quit()
	
	def on_multiBureaux_clicked(self, widget):
		if self.state == 0:
<<<<<<< HEAD
			self.Process = subprocess.Popen(["python", "multi_bureaux.py"], shell=False)
=======
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/multi_bureaux.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
<<<<<<< HEAD
				self.Process = subprocess.Popen(["python", "multi_bureaux.py"], shell=False)
=======
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/multi_bureaux.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
				self.state = 1

	def on_copierColler_clicked(self, widget):
		if self.state == 0:
<<<<<<< HEAD
			self.Process = subprocess.Popen(["python", "copier_coller.py"], shell=False)
=======
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/copier_coller.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
<<<<<<< HEAD
				self.Process = subprocess.Popen(["python", "copier_coller.py"], shell=False)
=======
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/copier_coller.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
				self.state = 1

	def on_favorite_clicked(self, widget):
		if self.state == 0:
<<<<<<< HEAD
			self.Process = subprocess.Popen(["python", "favorite_applis.py"], shell=False)
=======
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/favorite_applis.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
<<<<<<< HEAD
				self.Process = subprocess.Popen(["python", "favorite_applis.py"], shell=False)
=======
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/favorite_applis.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
				self.state = 1

	def on_media_clicked(self, widget):
		if self.state == 0:
			subprocess.Popen(["vlc"])
<<<<<<< HEAD
			self.Process = subprocess.Popen(["python", "/media.py"], shell=False)
=======
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/media.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				subprocess.Popen(["vlc"])
<<<<<<< HEAD
				self.Process = subprocess.Popen(["python", "media.py"], shell=False)
=======
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/media.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
				self.state = 1

	def on_son_clicked(self, widget):
		if self.state == 0:
<<<<<<< HEAD
			self.Process = subprocess.Popen(["python", "son.py"], shell=False)
=======
			self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/son.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
<<<<<<< HEAD
				self.Process = subprocess.Popen(["python", "son.py"], shell=False)
=======
				self.Process = subprocess.Popen(["python", "/home/jean/Arduino/projet_pedalier/son.py"], shell=False)
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
				self.state = 1

	def on_buttonStop_clicked(self, widget):
		self.Process.kill()
		self.state=0

<<<<<<< HEAD
'''_______________________________________________________________verification de xdotool__________________________________________________________________________'''


sortie = subprocess.Popen(["aptitude show xdotool | grep install"], stdout = subprocess.PIPE, shell = True)
retour = sortie.stdout.read()

if retour[:14] == "État: install" :
	HelloWorld()
	Gtk.main()
else:
	tkMessageBox.showinfo(title="Warning", message="xdotool doit être installé, Veuillez suivre la procédure d'installation et relancer FootClick")	
	subprocess.call(["gnome-terminal", "-e", "sudo apt install xdotool"])
=======
if __name__ == "__main__":	
	HelloWorld()
	Gtk.main()
>>>>>>> 9a7a21579e6b34b401eebfe3f6234ed6f6f85477
