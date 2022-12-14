
class Alu:
    def __init__(self):
        self.operando1 = []
        self.operando2 = []
        self.operacion = "string"
        self.resultado = []

#!!!!! Casos especiales, operaciones logicas and, or, not
    def operar(self):
        if(self.validarOperandoDigito(self.operando1) and
                self.validarOperandoDigito(self.operando2)):

            match self.operacion:
                case '==':
                    self.resultado.append(self.operando1[0] == self.operando2[0])
                case "+1":
                    self.resultado.append(self.operando1[0] + 1)
                case "-1":
                    self.resultado.append(self.operando1[0] + 1)
                case "+":
                    self.resultado.append(self.operando1[0] + self.operando2[0])
                case "-":
                    self.resultado.append(self.operando1[0] - self.operando2[0])
                case "/":
                    self.resultado.append(self.operando1[0] / self.operando2[0])
                case "*":
                    self.resultado.append(self.operando1[0] * self.operando2[0])
        else:
            match self.operacion:
                case '==':
                    self.resultado.append(self.operando1[0] == self.operando2[0])
                case "+":
                    self.resultado.append(self.operando1[0] + self.operando2[0])

    def validarOperandoDigito(self, operando):
        return operando.isdigit()

    def setOperando1(self,numero):
        self.operando1.append(numero)

    def setOperando2(self,numero):
        self.operando2.append(numero)

    def setOperacion(self,operacion):
        self.operacion = operacion

    def getResultado(self):
        return self.resultado[0]