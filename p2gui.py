#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtCore 
from PySide import QtGui 


import interface_prospero
import re
import datetime


class client(object):
	def __init__(self,h = '127.0.0.1',p = '4000'):
		self.c = interface_prospero.ConnecteurPII() 
		self.c.set(h,p)
		self.teste_connect()

	def teste_connect(self):
		teste = self.c.connect()
		if (teste):
			self.Etat = True
		else :
			self.Etat = False

	def disconnect(self):
		self.c.disconnect()


	def recup_cols(self):
		var = "$col[0:]"
		cols = self.c.eval_variable(var)
		self.cols = re.split(", ",cols) 
		return var
	
	def recup_ents(self):
		var = "$ent[0:1000]"
		ents = self.c.eval_variable(var)
		self.ents = re.split(", ",ents)
		return var

	def recup_efs(self):
		var = "$ef[0:]"
		efs = self.c.eval_variable(var)
		self.efs = re.split(", ",efs) 
		return var
	
	def recup_texts(self):
		txts = self.c.eval_variable("$txt[0:]")
		self.txts = re.split(", ",txts)

	def eval_var(self,var):
		self.eval_var_result = self.c.eval_variable(var)
		return re.split(", ",self.eval_var_result) 
	# jp : pour retrouver la sémantique d'un élément : (getsem 'nucléaire' $ent )
	def eval_get_sem(self,exp,type):
		exp = exp.encode('utf-8')
		self.eval_var_result = self.c.eval_fonc("getsem:" + exp + ":" + type)
		return self.eval_var_result  

class Principal(QtGui.QMainWindow):
	def __init__(self):
		super(Principal, self).__init__()
		self.initUI()
		

	def initUI(self):


		# create the menu bar
		#menubar = self.menuBar()
#		ParamMenu = menubar.addMenu('&Parameter')
# parametrage du Gui : langue etc
#		ConstelMenu = menubar.addMenu('&Constellation')
#		HelpMenu = menubar.addMenu('&Help')

		# create the status bar
		self.status = self.statusBar()
		self.status.showMessage(u"Ready")
	
		# create the toolbar
		toolbar = self.addToolBar("toolbar")	
		toolbar.setIconSize(QtCore.QSize(16, 16))
		toolbar.setMovable( 0 )

		#Saction = QtGui.QAction(QtGui.QIcon('Prospero-II.png'), 'Server', self)
		#toolbar.addAction(Saction)

		list1 = QtGui.QComboBox()
		list1.addItem(u"Reference corpus")
#		list1.addItem(u"auteur : AFP")
		toolbar.addWidget(list1)

		spacer1 = QtGui.QLabel()
		spacer1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		toolbar.addWidget(spacer1)
		
		etat1 = QtGui.QLabel()
#		etat1.setText("234 textes 5,44 pages volume 234")
		toolbar.addWidget(etat1)
		
		spacer2 = QtGui.QLabel()
		spacer2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		toolbar.addWidget(spacer2)

		etat2 = QtGui.QLabel()
#		etat2.setText("/Users/gspr/corpus/Alarm and Controversies/AaC.prc")
		toolbar.addWidget(etat2)


		#quart SE

		SET11 =  QtGui.QLabel()
#		Prop1Image = QtGui.QPixmap("prop1.png")
#		SET11.setPixmap(Prop1Image)
		SET12 =  QtGui.QLabel()
#		Prop2Image = QtGui.QPixmap("prop2.png")
#		SET12.setPixmap(Prop2Image)
		SET13 =  QtGui.QLabel()
#		Prop3Image = QtGui.QPixmap("prop3.png")
#		SET13.setPixmap(Prop3Image)
		SET14 =  QtGui.QLabel()
#		Prop4Image = QtGui.QPixmap("prop4.png")
#		SET14.setPixmap(Prop4Image)
		SET15 =  QtGui.QLabel()
#		Prop5Image = QtGui.QPixmap("prop5.png")
#		SET15.setPixmap(Prop5Image)

		SET1 = QtGui.QTabWidget()
#		SET1.addTab(SET11,u"Propriétés saillantes")
#		SET1.addTab(SET12,u"Apports et reprises")
#		SET1.addTab(SET13,u"Eléments du texte")
#		SET1.addTab(SET14,u"Textes proches")
#		SET1.addTab(SET15,u"Textes identiques")


		T2 =  QtGui.QLabel()
#		CTXImage = QtGui.QPixmap("CTX.png")
#		T2.setPixmap(CTXImage)

		T3 =  QtGui.QLabel()
#		TextImage = QtGui.QPixmap("Text.png")
#		T3.setPixmap(TextImage)


		SubWdwSE = QtGui.QTabWidget()
#		SubWdwSE.addTab(SET1,"Prop")
#		SubWdwSE.addTab(T2,"CTX")
#		SubWdwSE.addTab(T3,"Text")


		#quart SO

		self.SOT1 = QtGui.QListWidget()

		#SOT2 =  QtGui.QLabel()
#		NetworkImage = QtGui.QPixmap("network.png")
#		SOT2.setPixmap(NetworkImage)

		SOT3 =  QtGui.QLabel()
#		EnglImage = QtGui.QPixmap("engl.png")
#		SOT3.setPixmap(EnglImage)

		#jp réseau
		self.SOT2 =  QtGui.QListWidget()
		#


		SubWdwSO = QtGui.QTabWidget()
		SubWdwSO.addTab(self.SOT1,"Texts")
		#jp réseau
		SubWdwSO.addTab(self.SOT2,"Networks")
#		SubWdwSO.addTab(SOT2,"Network")
#		SubWdwSO.addTab(SOT3,"Expressions englobantes")


		#quart NE

#parametrer le serveur
		Param_Server = QtGui.QWidget()
		Param_Server_V = QtGui.QVBoxLayout()
#Ici on lancera le serveur avec le PRC ciblé
		Param_Server_I = QtGui.QLabel()
		Param_Server_I.setPixmap(QtGui.QPixmap('Prospero-II.png'))
		Param_Server_V.addWidget(Param_Server_I)
#configurer les parametres de connexion au serveur
		Param_Server_F = QtGui.QFormLayout()
		self.Param_Server_val_host = QtGui.QLineEdit()
		Param_Server_F.addRow("&host",self.Param_Server_val_host)
		self.Param_Server_val_host.setText('127.0.0.1')
		self.Param_Server_val_port = QtGui.QLineEdit()
		Param_Server_F.addRow("&port",self.Param_Server_val_port)
		self.Param_Server_val_port.setText('4000')
		Param_Server_V.addLayout(Param_Server_F)
#a terme la connection locale lancera le serveur local
		self.Param_Server_B = QtGui.QPushButton('Connect to server')
		self.Param_Server_B.clicked.connect(self.connect_server)
		Param_Server_F.addWidget(self.Param_Server_B)
		Param_Server.setLayout(Param_Server_V)

#onglet de gestion du PRC a ajouter
		NET1 = QtGui.QTextEdit()
#l'historique des actions
		self.History =  QtGui.QTextEdit()

#evaluer directement les variables du serveur
		server_vars = QtGui.QWidget()
		server_vars_Vbox =  QtGui.QVBoxLayout() 
		server_vars.setLayout(server_vars_Vbox)

		server_vars_Hbox = QtGui.QHBoxLayout()
		server_vars_champL = QtGui.QFormLayout()
		self.server_vars_champ = QtGui.QLineEdit()
		self.server_vars_champ.returnPressed.connect(self.server_vars_Evalue)
		server_vars_champL.addRow("&var",self.server_vars_champ)
		server_vars_Hbox.addLayout(server_vars_champL)
		server_vars_button_eval = QtGui.QPushButton('Eval')
		server_vars_Hbox.addWidget(server_vars_button_eval)
		server_vars_button_eval.clicked.connect(self.server_vars_Evalue)
		server_vars_button_clear = QtGui.QPushButton('Clear')
		server_vars_Hbox.addWidget(server_vars_button_clear)
		server_vars_button_clear.clicked.connect(self.server_vars_Clear)
		server_vars_Vbox.addLayout(server_vars_Hbox)

		self.server_vars_result = QtGui.QTextEdit(readOnly = True) 
		server_vars_Vbox.addWidget(self.server_vars_result)

		T4 =  QtGui.QLabel()
#		viewImage = QtGui.QPixmap("viewer.png")
#		T4.setPixmap(viewImage)

#mise en place des onglets
		SubWdwNE = QtGui.QTabWidget()
		SubWdwNE.addTab(Param_Server,"Server parameters")
#		SubWdwNE.addTab(T4,"Viewer")
#		SubWdwNE.addTab(NET1,"Marlowe")
		SubWdwNE.addTab(self.History,"History")
		SubWdwNE.addTab(server_vars,"Server vars")

		#quart NO

		SubWdwNO =  QtGui.QTabWidget()

		#NOT1 =  QtGui.QLabel()
		#NOImage = QtGui.QPixmap("NO.png")
		#NOT1.setPixmap(NOImage)

		NOT1 = QtGui.QWidget()
#une box verticale
		NOT1V = QtGui.QVBoxLayout()
		NOT1.setLayout(NOT1V)

	#une ligne horizontale qui contient les commandes au dessus-de la liste 
		NOT1VHC = QtGui.QHBoxLayout()
		NOT1V.addLayout(NOT1VHC)
	#une liste deroulante pour choisir le contenu de la liste
		self.NOT1select = QtGui.QComboBox()
		self.NOT1select.addItem(u"collections")
		self.NOT1select.addItem(u"entities")
		self.NOT1select.addItem(u"fictions")
		NOT1VHC.addWidget(self.NOT1select)
		self.connect(self.NOT1select,QtCore.SIGNAL("currentIndexChanged(const QString)"), self.select_liste)
	# les commandes
		#NOT1Commands = QtGui.QMenu()
		#NOT1Commands.setTitle("titre")
		#NOT1Commands.addMenu('&Research')
		#NOT1Commands.addMenu('&T')
		#NOT1Commands.addMenu('&V')
		#NOT1VHC.addWidget(NOT1Commands)

	#une box horizontale pour liste, score et deploiement
		NOT1VH = QtGui.QHBoxLayout()
		NOT1V.addLayout(NOT1VH) 
	#la liste
		self.NOT12 = QtGui.QListWidget()
		
		
		NOT1VH.addWidget(self.NOT12)
		
		# try un listview multi colonnes
		self.NOT122 = QtGui.QListView()
		
		NOT1VH.addWidget(self.NOT122)
	#jp signal associé
		self.NOT12.itemActivated.connect(self.item_activated)
		
	#le deploiement
		self.NOT12_D = QtGui.QListWidget()
		NOT1VH.addWidget(self.NOT12_D)



		NOT2 =  QtGui.QLabel()
#		FrmlImage = QtGui.QPixmap("formul.png")
#		NOT2.setPixmap(FrmlImage)

		NOT3 =  QtGui.QLabel()
#		ExploImage = QtGui.QPixmap("explo.png")
#		NOT3.setPixmap(ExploImage)

		SubWdwNO.addTab(NOT1,"Lists")
#		SubWdwNO.addTab(NOT2,"Formulae")
#		SubWdwNO.addTab(NOT3,"Explorer")

		#la MdiArea 
		Area = QtGui.QMdiArea()
		sw1 = Area.addSubWindow(SubWdwSE, flags = QtCore.Qt.FramelessWindowHint)
		sw2 = Area.addSubWindow(SubWdwSO, flags = QtCore.Qt.FramelessWindowHint)
		sw3 = Area.addSubWindow(SubWdwNE , flags = QtCore.Qt.FramelessWindowHint)
		sw4 = Area.addSubWindow(SubWdwNO , flags = QtCore.Qt.FramelessWindowHint)
	

		Area.tileSubWindows()

		self.setCentralWidget(Area)
				
		self.setWindowTitle(u'Prospéro II 25/10/2014')    
		self.showMaximized() 
	#jp
	def get_type(self):
		print self.NOT1select.currentText()
		if self.NOT1select.currentText()=="entities" : return '$ent'
		if self.NOT1select.currentText()=="collections" : return '$col'
		if self.NOT1select.currentText()=="fictions" : return '$ef'
		return ''
	def item_activated(self):

		type = self.get_type()

		if not type : return
		print "type :" + type
		exp = self.NOT12.currentItem().text()
		print "exp  " +  exp
		semantique = self.client.eval_get_sem(exp, type)
		print  "----> " , semantique 
		self.update_networks ( exp, semantique)
		
		
	def update_networks (self, exp,semantique):
		"""
			$ent10 --> $ent10.res[0:200]
			$col1	---> $col1.res[0:200]
		"""
		self.SOT2.clear()
		
		res_semantique = semantique + ".res[0:200]"
		content = self.client.eval_var(res_semantique)
		self.SOT2.addItems(content)
		
		
	def activity(self,message):
		self.status.showMessage(message)
		self.History.append("%s: %s" % (datetime.datetime.now(),message))

	def recup_liste_textes(self):
		self.activity(u"Waiting for text list"   )
		self.client.recup_texts()
		self.activity(u"Displaying text list (%d items)" %len(self.client.txts)  )
		self.SOT1.clear()
		listeTextes = self.client.txts
		self.SOT1.addItems(listeTextes)

	def select_liste(self,typ):
		if (typ == ""):
			content = []
		elif (typ == "collections"):
			self.activity(u"Waiting for  %s list" % (typ)) 
			var = self.client.recup_cols()
			content = self.client.cols
		elif (typ == "entities"):
			self.activity(u"Waiting for  %s list" % (typ)) 
			var = self.client.recup_ents()
			content = self.client.ents
		elif (typ == "fictions"):
			self.activity(u"Waiting for  %s list" % (typ)) 
			var = self.client.recup_efs()
			content = self.client.efs
			
		if len(content):
			self.activity(u"Displaying %s list (%d items)" % (typ,len(content)))
		else :
			self.activity(u"Displaying no list" )
		self.change_liste(content)

	def change_liste(self,content):
		self.NOT12.clear()
		self.NOT12.addItems(content)
		
	def server_vars_Evalue(self):
		var = self.server_vars_champ.text()
		self.server_vars_champ.clear()
		self.client.eval_var(var)
		self.server_vars_result.setColor("red")
		self.server_vars_result.append("%s" % var)
		self.server_vars_result.setColor("black")
		self.server_vars_result.append(self.client.eval_var_result)

	def server_vars_Clear(self):
		self.server_vars_result.clear()
	
	def connect_server(self):
		self.activity("Connecting to server")
		self.client=client(self.Param_Server_val_host.text(),self.Param_Server_val_port.text())
		self.client.teste_connect()
		if (self.client.Etat):
			self.select_liste(self.NOT1select.currentText())
			self.recup_liste_textes()
			self.Param_Server_B.clicked.connect(self.disconnect_server)
			self.Param_Server_B.setText("Disconnect")
	
	def disconnect_server(self):
		self.activity("Disconnecting")
		self.client.disconnect()
		self.Param_Server_B.setText('Connect to server')
		self.Param_Server_B.clicked.connect(self.connect_server)


def main():
	app = QtGui.QApplication(sys.argv)
	ex  = Principal()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()