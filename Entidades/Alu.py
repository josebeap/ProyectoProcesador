
class Alu:
    def __init__(self):
        self.operando1 = 0
        self.operando2 = 0
        self.operacion = "string"


    def Operar(self,simbolo):
        if(simbolo == "-"):
            self.operacion = self.operando1 - self.operando2
        elif(simbolo == "*"):
            self.operacion = self.operando1 * self.operando2
        elif(simbolo == "/"):
            self.operacion = self.operando1 / self.operando2
        elif(simbolo == "+"):
            self.operacion = self.operando1 + self.operando2
        else:
            print("No es operacion valida")
    def setOperando1(self,numero):
        self.operando1 = numero
    def setOperando2(self,numero):
        self.operando2 = numero

    def setOperacion(self,operacion):
        self.operacion = operacion
    def getResultado(self):
        return self.operacion