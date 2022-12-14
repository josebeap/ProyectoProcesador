
import Mar, Mbr
class Memoria:

    def __init__(self):
        self.DirCont = {}
        self.mar = Mar
        self.mbr = Mbr

#Retorna la clave(int) de la direccion cargada en la mar de la memoria
#JOSE CREE Q NECESITAMOS OTRO RETURN
    def buscarDireccion(self):
        for i in self.DirCont:
            cont = 0
            if cont > len(self.DirCont):
                print("El dato buscado no existe")
                break
            elif (cont == self.mar.getDireccion()):
                return i
            else:
                cont+= 1

#Carga el dato(Str) en la Mbr el dato se encuentra en la direccion proporcionada
    def cargarMBR(self, key):
        dato = self.DirCont[int(key)]
        self.mbr.setDato(dato)

#carga la mar con la posicion a buscar
    def cargarMar(self,posicion):
        self.mar.setDireccion(posicion)

#Carga las instruciones solicitadas a la memoria principal
    def cargarInstruccionesDiccionario(self, lista):
        longitudLista = len(lista)
        cont = 0
        print(longitudLista)
        for i in lista:
            self.DirCont[cont] = i
            cont = cont + 1
            longitudLista = longitudLista - 1

#Envia el resgistro de instruccion completo para ser decodificado por la UC
    def cargarRegistro(self):
        direccion = self.buscarDireccion()
        self.cargarMBR(direccion)


    def getMbr(self):
        return self.mbr
    def getMar(self):
        return self.mar


