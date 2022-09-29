import imp
import os
from re import S
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import*
from qgis.utils import*

from .interfaz import ModuloRaster, Ui_ModuloRaster

class interfaz (QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = Ui_ModuloRaster
        self.ui.setupUi(ModuloRaster=)

        self.ui.btn4.clicked.connect(self.cerrar)
        self.ui.btn1.clicked.connect("ingresar codigo")
        self.ui.cmb1.currentIndexChanged.connect("ingresar codigo")

    def cerrar(self):
        self.close()
    
    def nombreCmb(self):
        layers = QgsProject.instance().mapLayers().values() 
        for layer in layers:
            if layer.type() == 0:
                nomVLayer = layer.name()
                self.ui.lb1.setText(nomVLayer)
            if layer.type()== 1:
                nomRLayer = layer.name()
                self.ui.lb1.setText(nomRLayer)
    def abrirRaster(self):
        lypath, _ = QFileDialog.getOpenFileName(self, "Agrega un archivo raster (MDE)", "C:\\", "Raster (*.tif *.GRID)")
        lyInfo = QFileInfo(lypath)
        rlayer = QgsRasterLayer(lypath, lyInfo.fileName())
        if not rlayer.isValid():
            return
        QgsProject.instance().addMapLayer(rlayer)
        self.ui.cmb1.addItem("ingresar codigo")
        self.ui.lb1.setText("ingresar codigo")
    
    def selectRaster(self):
        Layertex = self.ui.cBox4.currentText()
        layers = QgsProject.instance().mapLayers().values()
        if self.ui.cBox4.currentIndex() >= 0:
            for layer in layers:
                if layer.name() == "ingresar codigo":
                    self.ui.LineE2.setText("ingresar codigo")
        else:
            self.ui.lb1.setText("")
            self.ui.lb1.setText("")