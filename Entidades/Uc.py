import Ir, Pc, Memoria, Alu
class Uc:

    def __init__(self):
        self.pilaOperandos = []
        self.registroInstrucciones = Ir
        self.contadorPrograma = Pc
        self.memoriaPrincipal = Memoria
        self.alu = Alu
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
        self.memoriaPrincipal.cargarMar(self.contadorPrograma.getNumeroInstr())
        self.memoriaPrincipal.cargarRegistro()
        self.registroInstrucciones.setInstruccion(self.memoriaPrincipal.getMbr().getDato())
        self.decodificar()

#Asigna la funcion a ejecutar
    def decodificar(self):
        nueva = self.registroInstrucciones.getInstruccion()
        auxiliar = nueva.split(' ')
        instruccion = auxiliar[0]
        self.comprobarFuncion(instruccion)



#comprueba lka funcion solicitada si es posible o no
    def comprobarFuncion(self,funcion):
        if(funcion in self.operacionesPosibles):
            self.decodificador = self.operacionesPosibles[funcion]
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
                self.enviarAlu(self.decodificador)
            case "CLEAR":
                self.pilaOperandos=[]
            case "POP":
                print(self.pilaOperandos.pop())
            case "INCREMENT":
                self.enviarAlu(1, "+")
            case "DECREMENT":
                self.enviarAlu(1, "-")
            case "AND":
                self.enviarAlu("and")
            case "OR":
                self.enviarAlu("or")
            case "NOT":
                self.enviarAlu(-1,"*")
            case "SUM":
                self.enviarAlu("+")
            case "RES":
                self.enviarAlu("-")
            case "DIV":
                self.enviarAlu("/")
            case "MPY":
                self.enviarAlu("*")


    def obtenerOperando(self,dato):
        aux = dato.split(' ')
        return aux[1]
    def enviarAlu(self,operacion):
        self.alu.setOperando1(self.pilaOperandos.pop())
        self.alu.setOperando2(self.pilaOperandos.pop())
        self.alu.setOperacion(operacion)

    def enviarAlu(self,operando2,operacion):
        self.alu.setOperando1(self.pilaOperandos.pop())
        self.alu.setOperando2(operando2)
        self.alu.setOperacion(operacion)

