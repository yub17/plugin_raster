import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import*
from qgis.utils import*

from .interfaz import Ui_ModuloRaster

class interfaz (QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = Ui_ModuloRaster
        self.ui.setupUi(self)
