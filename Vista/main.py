from tkinter import *

class main:
    def __init__(self):
        self.app = Tk()
        self.app.title('Procesador')
        self.app.state('zoomed')

        self.alu = PhotoImage(file="../Imagenes/alu.png")

        self.frame = Frame(self.app)
        self.frame.pack(fill="both")
        self.frame.config(width=1360, height=760, bg='navy')

        self.mensaje = Text(self.frame, width=25, height=20)
        self.mensaje.place(x=10, y=20)

        self.simbolos = {'Input': (1),
                         'Output': (2),
                         'Compare': (3),
                         'Clear': (4),
                         'Set': (5),
                         'Push': (6),
                         'Pop': (7),
                         'Incremet': (8),
                         'Decrement': (9),
                         'AND': (10),
                         'OR': (11),
                         'NOT': (12)
                         }

        self.button2 = Button(
            button2=Button(self.frame, text="Cargar Datos", command=self.mostrar).place(x=10, y=400))

        self.map = Canvas(self.frame, width=1360, height = 760, bg='grey')
        self.map.place(x=250, y=0)

        self.map.create_text(100, 550, fill="black", font="Times 20", text="Ejemplo: \n Push A \n Push B")

        #ALU
        self.map.create_image(10, 200, anchor=NW, image=self.alu)
        self.map.create_text(250, 530, fill="black", font="Times 30", text="ALU")

        #MAR
        self.map.create_rectangle(30, 30, 180, 120, fill="limegreen")
        self.map.create_text(100, 100, fill="black", font="Times 30", text="MAR")

        #IR
        self.map.create_rectangle(350, 30, 500, 120, fill="firebrick1")
        self.map.create_text(425, 100, fill="black", font="Times 30", text="IR")

        #MRB
        self.map.create_rectangle(30, 610, 180, 700, fill="cyan2")
        self.map.create_text(100, 680, fill="black", font="Times 30", text="MBR")

        #PC
        self.map.create_rectangle(600, 200, 750, 300, fill="mediumblue")
        self.map.create_text(670, 270, fill="black", font="Times 30", text="PC")

        #UC
        self.map.create_rectangle(600, 350, 800, 600, fill="tomato3")
        self.map.create_rectangle(620, 360, 780, 400, fill="darkorange1")
        self.map.create_text(700, 410, fill="black", font="Times 20", text="Decodificador")
        self.map.create_text(670, 550, fill="black", font="Times 30", text="UC")

        #Resultado
        self.map.create_rectangle(900, 10, 1100, 250, fill="gold")
        self.map.create_text(1000, 30, fill="black", font="Times 30", text="Resultado: ")

        #Memoria
        self.map.create_rectangle(850, 350, 1050, 700, fill="gold")
        self.map.create_text(970, 330, fill="black", font="Times 30", text="MEMORIA")
        self.map.create_text(950, 370, fill="black", font="Times 30", text="Dir    Cont")
        self.map.create_line(850, 400, 1050, 400, width=8, fill="black")
        self.map.create_line(935, 350, 935, 700, width=8, fill="black")

        #Datos que ingresan a la alu
        self.map.create_rectangle(10, 190, 150, 250, fill="deeppink")
        self.map.create_rectangle(340, 190, 480, 250, fill="yellow2")

        #Lineas Mbr - ALU
        self.map.create_line(300, 490, 300, 660, width=8, fill="black")
        self.map.create_line(300, 660, 180, 660, width=8, fill="black")

        #Lineas Mbr - memoria
        self.map.create_line(180, 690, 850, 690, width=8, fill="black")

        #Lineas uc - mar
        self.map.create_line(600, 420, 550, 420, width=8, fill="black")
        self.map.create_line(550, 420, 550, 150, width=8, fill="black")
        self.map.create_line(550, 150, 100, 150, width=8, fill="black")
        self.map.create_line(100, 150, 100, 120, width=8, fill="black")

        #Lineas uc - ir
        self.map.create_line(600, 380, 580, 380, width=8, fill="black")
        self.map.create_line(580, 380, 580, 100, width=8, fill="black")
        self.map.create_line(580, 100, 500, 100, width=8, fill="black")

        #Lineas uc - pc
        self.map.create_line(650, 300, 650, 350, width=8, fill="black")

        #Lineas pc a pc
        self.map.create_line(670, 200, 670, 170, width=8, fill="black")
        self.map.create_line(670, 170, 780, 170, width=8, fill="black")
        self.map.create_line(780, 170, 780, 250, width=8, fill="black")
        self.map.create_line(780, 250, 750, 250, width=8, fill="black")

        #lineas mar - memoria
        self.map.create_line(150, 30, 150, 10, width=8, fill="black")
        self.map.create_line(150, 10, 870, 10, width=8, fill="black")
        self.map.create_line(870, 10, 870, 350, width=8, fill="black")

        #self.openFile()
        self.app.mainloop()

    #metodo para mostrar la cadena ingresada
    def mostrar(self):

        self.map.create_text(1000, 60, fill="black", font="Times 10", text=self.mensaje.get(1.0, "end-1c"))
        listaRetorno = self.separar_Cadena(self.mensaje.get(1.0, "end-1c"))
        #elf.map.create_text(1000, 60, fill="black", font="Times 10", text=listaRetorno)


    # Pintar Lineas Mbr - ALU
    def pintar_mbr_alu(self):
        self.map.create_line(300, 490, 300, 660, width=4, fill="gold")
        self.map.create_line(300, 660, 180, 660, width=4, fill="gold")
    # Pintar Lineas Mbr - memoria
    def pintar_mbr_memoria(self):
        self.map.create_line(180, 690, 850, 690, width=4, fill="gold")
    # Pintar Lineas uc - mar
    def pintar_uc_mar(self):
        self.map.create_line(600, 420, 550, 420, width=4, fill="gold")
        self.map.create_line(550, 420, 550, 150, width=4, fill="gold")
        self.map.create_line(550, 150, 100, 150, width=4, fill="gold")
        self.map.create_line(100, 150, 100, 120, width=4, fill="gold")
    # Pintar Lineas uc - ir
    def pintar_uc_ir(self):
        self.map.create_line(600, 380, 580, 380, width=4, fill="gold")
        self.map.create_line(580, 380, 580, 100, width=4, fill="gold")
        self.map.create_line(580, 100, 500, 100, width=4, fill="gold")
    # Pintar Lineas uc - pc
    def pintar_uc_pc(self):
        self.map.create_line(650, 300, 650, 350, width=4, fill="gold")
    # Pintar Lineas pc a pc
    def pintar_pc_pc(self):
        self.map.create_line(670, 200, 670, 170, width=4, fill="gold")
        self.map.create_line(670, 170, 780, 170, width=4, fill="gold")
        self.map.create_line(780, 170, 780, 250, width=4, fill="gold")
        self.map.create_line(780, 250, 750, 250, width=4, fill="gold")
    # Pintar lineas mar - dir memoria
    def pintar_mar_memoria(self):
        self.map.create_line(150, 30, 150, 10, width=4, fill="gold")
        self.map.create_line(150, 10, 870, 10, width=4, fill="gold")
        self.map.create_line(870, 10, 870, 350, width=4, fill="gold")

    #Metodo para separar la cadena que ingresa
    def separar_Cadena(self,texto):
        listaSimbolosCadena = []
        listaCadena = texto.split('\n')
        for e in listaCadena:
            aux = e.split(' ')
            listaSimbolosCadena.append(aux)
        for f in listaSimbolosCadena:
            print("examino la lista de los simbolos")
            if str(f[0]) in str(self.simbolos.keys()):
                print("si estoy : ", f[0])
        print(" Estos son los simbolos cadena ", listaSimbolosCadena)
        print(" Esta es la cadena ", listaCadena)
        print(" Estos son los simbolos ", self.simbolos)
        return listaCadena

main()