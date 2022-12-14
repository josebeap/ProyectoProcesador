from Entidades.Ir import Ir
from Entidades.Pc import Pc
from Entidades.Memoria import Memoria
from Entidades.Alu import Alu
class Uc:

    def __init__(self):
        self.pilaOperandos = []
        self.registroInstrucciones = Ir()
        self.contadorPrograma = Pc()
        self.memoriaPrincipal = Memoria()
        self.alu = Alu()
        self.decodificador = ""
        self.operacionesPosibles = {'OUTPUT': "print",
                                     'COMPARE': "==",
                                     'CLEAR': "[]",
                                     'PUSH': "append",
                                     'POP': "pop",
                                     'INCREMENT': "+1",
                                     'DECREMENT': "-1",
                                     'AND': "and",
                                     'OR': "or",
                                     'NOT': "not",
                                     'SUM': '+',
                                     'RES': '-',
                                     'DIV': '/',
                                     'MPY': '*'
                                     }

#cargar lo q se mando a la memoria
    def cargarInstrucciones(self,lista):
        self.memoriaPrincipal.cargarInstruccionesDiccionario(lista)

#contador arranca en cero y empieza la primera
#busqueda de memoria
    def captacion(self):
        while(self.contadorPrograma.getNumeroInstr() < self.memoriaPrincipal.getLongitudPendientes()):
            self.memoriaPrincipal.cargarMar(self.contadorPrograma.getNumeroInstr())
            self.contadorPrograma.aumentarNumeroInstruccion()
            self.memoriaPrincipal.cargarRegistro()
            self.registroInstrucciones.setInstruccion(self.memoriaPrincipal.getMbr().getDato())
            self.decodificar()
            #print("Esta es la instruccion", self.decodificador)
            self.ejecutarInstruccion(self.decodificador)
            #print("Esta es la pila", self.pilaOperandos)

    def ejecucion(self):
        self.captacion()
        #bANDERA uc - Alu
        self.alu.operar()



#Asigna la funcion a ejecutar
    def decodificar(self):
        nueva = self.registroInstrucciones.getInstruccion()
        print("Esta es la IR", self.registroInstrucciones.getInstruccion())
        auxiliar = nueva.split(' ')
        instruccion = auxiliar[0]
        print("Esta es la isntruccion al dividir", instruccion)
        self.comprobarFuncion(instruccion)

#comprueba lka funcion solicitada si es posible o no
    def comprobarFuncion(self,funcion):
        if(funcion in self.operacionesPosibles):
            self.decodificador = funcion
        else:
            self.decodificador = None

    def ejecutarInstruccion(self,instruccion):
        dato = self.memoriaPrincipal.getMbr().getDato()
        match instruccion:
            case "PUSH":
                self.pilaOperandos.append(self.obtenerOperando(dato))
            case "OUTPUT":
                print(self.pilaOperandos.pop())
            case "COMPARE":
                self.enviarAlu('==')
            case "CLEAR":
                self.pilaOperandos=[]
            case "POP":
                print(self.pilaOperandos.pop())
            case "INCREMENT":
                self.enviarAlu2("1", "+1")
            case "DECREMENT":
                self.enviarAlu2("1", "-1")
            case "AND":
                self.enviarAlu1("and")
            case "OR":
                self.enviarAlu1("or")
            case "NOT":
                self.enviarAlu1("-1","*")
            case "SUM":
                self.enviarAlu1("+")
            case "RES":
                self.enviarAlu1("-")
            case "DIV":
                self.enviarAlu1("/")
            case "MPY":
                self.enviarAlu1("*")


    def obtenerOperando(self,dato):
        aux = dato.split(' ')
        return aux[1]
    def enviarAlu1(self,operacion):
        self.alu.setOperando1(self.pilaOperandos.pop())
        self.alu.setOperando2(self.pilaOperandos.pop())
        self.alu.setOperacion(operacion)

    def enviarAlu2(self,operando2,operacion):
        self.alu.setOperando1(self.pilaOperandos.pop())
        self.alu.setOperando2(operando2)
        self.alu.setOperacion(operacion)

