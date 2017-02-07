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
import json

'''____________________________________________________class avance, atribution des actions aux boutons____________________________________________________________'''

class avance:
	def __init__(self):
		interface = Gtk.Builder()
		self.pwd = subprocess.Popen(["pwd"], stdout = subprocess.PIPE, shell = True)
		self.chemin = self.pwd.stdout.read()[:-1]
		interface.add_from_file(self.chemin+'/ClickAvance.glade')
		interface.connect_signals(self)
		self.Process = 0
		self.state = 0
		self.bouton = 0
		self.commande = 0

	def on_mainWindow_destroy(self, widget):
		Gtk.main_quit()
		
	def on_bouton_1_clicked(self, widget):
		if self.bouton == 0 :
			self.bouton +=1
		if self.bouton ==1 :
			fichier_json = open('bouton.json', 'r') #on lis le fichier json
	 
			with fichier_json as fichier:
				data = json.load(fichier)
				bouton1 = data['bouton1'] #on charge le fichier, et recupere l\'objet bouton1
			variable = open('Config.py', 'a') #on ouvre le fichier de config python
			variable.write(bouton1) #on ajoute l\'objet bouton1 au fichier de config
			variable.close()

	def on_bouton_2_clicked(self, widget):
		if self.bouton ==1 and self.commande == 1 :
			self.bouton +=1
			fichier_json = open('bouton.json', 'r')
	 
			with fichier_json as fichier:
				data = json.load(fichier)
				bouton2 = data['bouton2']
			variable = open('Config.py', 'a')
			variable.write('\n'+(bouton2))
			variable.close()

	def on_bouton_3_clicked(self, widget):
		if self.bouton ==2 and self.commande == 2 :
			self.bouton +=1
			fichier_json = open('bouton.json', 'r')
	 
			with fichier_json as fichier:
				data = json.load(fichier)
				bouton3 = data['bouton3']
			variable = open('Config.py', 'a')
			variable.write('\n'+(bouton3))
			variable.close()

	def on_bouton_copier_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				copier = data['copier']
			variable = open('Config.py', 'a')
			variable.write('\n'+(copier))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_coller_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				coller = data['coller']
			variable = open('Config.py', 'a')
			variable.write('\n'+(coller))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_couper_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				couper = data['couper']
			variable = open('Config.py', 'a')
			variable.write('\n'+(couper))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_tout_bureaux_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				toutBureaux = data['toutBureaux']
			variable = open('Config.py', 'a')
			variable.write('\n'+(toutBureaux))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_bureau_prec_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				bureauPrec = data['bureauPrec']
			variable = open('Config.py', 'a')
			variable.write('\n'+(bureauPrec))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_bureau_suiv_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				bureauSuiv = data['bureauSuiv']
			variable = open('Config.py', 'a')
			variable.write('\n'+(bureauSuiv))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_thunderbird_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				thunderbird = data['thunderbird']
			variable = open('Config.py', 'a')
			variable.write('\n'+(thunderbird))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_fb_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				facebook = data['facebook']
			variable = open('Config.py', 'a')
			variable.write('\n'+(facebook))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_twitter_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				twitter = data['twitter']
			variable = open('Config.py', 'a')
			variable.write('\n'+(twitter))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_play_pause_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				playPause = data['playPause']
			variable = open('Config.py', 'a')
			variable.write('\n'+(playPause))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_av_rapide_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				avRapide = data['avRapide']
			variable = open('Config.py', 'a')
			variable.write('\n'+(avRapide))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_ret_rapide_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				retRapide = data['retRapide']
			variable = open('Config.py', 'a')
			variable.write('\n'+(retRapide))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_mute_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				muet = data['muet']
			variable = open('Config.py', 'a')
			variable.write('\n'+(muet))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_aug_volume_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				augVolume = data['augVolume']
			variable = open('Config.py', 'a')
			variable.write('\n'+(augVolume))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_dim_volume_clicked(self, widget):
		self.commande +=1
		if self.bouton != 0 and self.bouton <=3 :
			fichier_json = open('actionCommande.json', 'r')
 
			with fichier_json as fichier:
				data = json.load(fichier)
				dimVolume = data['dimVolume']
			variable = open('Config.py', 'a')
			variable.write('\n'+(dimVolume))
			variable.close()

		if self.bouton == 3 :
			self.bouton +=1

	def on_bouton_Go_clicked(self, widget):
		self.Process = subprocess.Popen(["python", "Config.py"], shell=False)

	def on_STOP_clicked(self, widget):
		self.Process.kill()

if __name__ == "__main__":
	avance()
	Gtk.main()
