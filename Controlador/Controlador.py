from Entidades.Uc import Uc

class Controlador:

    def __init__(self):
        self.uc = Uc()


    def cargarIntruccionesVista(self, lista):
        print("Esta es la lista inicial: ", lista)
        self.uc.cargarInstrucciones(lista)
        #OPCION: TENER BANDERA
        self.uc.ejecucion()
        print(self.uc.alu.getResultado())