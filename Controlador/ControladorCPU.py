from Entidades import Uc
from Vista import main

class Controlador:

    def __init__(self):
        self.uc = Uc
        self.vista = main


    def cargarIntruccionesVista(self, lista):
        self.uc.cargarInstrucciones(lista)
        self.uc.ejecucion()