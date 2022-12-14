from Entidades import Uc

class Controlador:

    def __init__(self):
        self.uc = Uc


    def cargarIntruccionesVista(self, lista):
        self.uc.cargarInstrucciones(lista)
        self.uc.ejecucion()
        print(self.uc.alu.getResultado())