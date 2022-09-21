import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import*
from qgis.utils import*

from .raster import interfaz

class mainMenu:
    def __init__(self,iface):
        self.iface = iface

    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Raster")
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(),self.IMenu)
        self.IMenuBar = self.iface.addToolBar("Raster")

        self.ejemplo = QAction(QIcon(""), "Raster", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemplo)
        self.ejemplo.triggered.connect(self.startInterfaz)

    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers = QgsProject.instance().mapLayers().values() 
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType()== QgsWkbTypes.PolygonGeometry:
                vLayer = layer
            if layer.type()==QgsRasterLayer.RasterLayer:
                rLayer = layer
                self.dialogo.ui.comboBox.addItem(rLayer.name())
                epsg = rLayer.crs()
                self.dialogo.ui.lb1.setText(str(epsg.authid()))
    def unload(self):
            self.IMenu.deleteLater()    
    
            
            