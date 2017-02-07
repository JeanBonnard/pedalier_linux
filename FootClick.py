#!/usr/bin/python
#-*-coding:utf-8 -*

'''__________________________________________________import des differentes librairies utile au programme__________________________________________________________'''

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
import Tkinter
import tkMessageBox

'''__________________________________________________class profilaction, atribution des actions aux boutons__________________________________________________________'''


class profilaction:
	def __init__(self):
		interface = Gtk.Builder()
		self.pwd = subprocess.Popen(["pwd"], stdout = subprocess.PIPE, shell = True)
		self.chemin = self.pwd.stdout.read()[:-1]
		interface.add_from_file(self.chemin+'/FootClick.glade')
		interface.connect_signals(self)
		self.Process = 0
		self.state = 0
		
	def on_mainWindow_destroy(self, widget):
		self.Process.kill()
		Gtk.main_quit()
	
	def on_multiBureaux_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "multi_bureaux.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "multi_bureaux.py"], shell=False)
				self.state = 1

	def on_copierColler_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "copier_coller.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "copier_coller.py"], shell=False)
				self.state = 1

	def on_favorite_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "favorite_applis.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "favorite_applis.py"], shell=False)
				self.state = 1

	def on_media_clicked(self, widget):
		if self.state == 0:
			subprocess.Popen(["vlc"])
			self.Process = subprocess.Popen(["python", "/media.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				subprocess.Popen(["vlc"])
				self.Process = subprocess.Popen(["python", "media.py"], shell=False)
				self.state = 1

	def on_son_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "son.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "son.py"], shell=False)
				self.state = 1

	def on_advance_clicked(self, widget):
		if self.state == 0:
			self.Process = subprocess.Popen(["python", "config_av.py"], shell=False)
			self.state = 1
		elif self.state == 1:
			self.Process.kill()
			self.state = 2
			if self.state == 2:
				self.Process = subprocess.Popen(["python", "config_av.py"], shell=False)
				self.state = 1

				nombre_lignes = sum(1 for _ in open('Config.py')) #on compte le nombre de lignes
				if nombre_lignes == 24 :

					with open("Config.py", "r") as config:
						config_str = ''.join(config.readlines()[:-6]) #on supprime les 6 dernieres si le fichier contien 24 lignes

					with open("Config.py", "w") as config:
						config.write(config_str) #on applique

	def on_buttonStop_clicked(self, widget):
		self.Process.kill()
		self.state=0


'''_______________________________________________________________verification de xdotool__________________________________________________________________________'''


sortie = subprocess.Popen(["aptitude show xdotool | grep install"], stdout = subprocess.PIPE, shell = True)
retour = sortie.stdout.read()

if retour[:14] == "État: install" :
	profilaction()
	Gtk.main()
else:
	tkMessageBox.showinfo(title="Warning", message="xdotool doit être installé, Veuillez suivre la procédure d'installation et relancer FootClick")	
	subprocess.call(["gnome-terminal", "-e", "sudo apt install xdotool"])
