def category():
    return "Raster"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)