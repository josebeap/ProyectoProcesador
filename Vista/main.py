from tkinter import *
#from Sistema.Graph import Graph
#from Sistema.Vertex import Vertex


class main:
    def __init__(self):
        self.app = Tk()
        self.app.title('Procesador')
        self.app.state('zoomed')

        #self.g = Graph()
        #self.city = None


        self.alu = PhotoImage(file="../Imagenes/alu.png")
        self.mar = PhotoImage(file="../Imagenes/MAR.png")
        self.ir = PhotoImage(file="../Imagenes/IR.png")
        self.mbr = PhotoImage(file="../Imagenes/MBR.png")
        self.pc = PhotoImage(file="../Imagenes/PC.png")
        self.uc = PhotoImage(file="../Imagenes/UC.png")
        self.ac = PhotoImage(file="../Imagenes/AC.png")
        self.banco = PhotoImage(file="../Imagenes/banco.png")
        self.op1 = PhotoImage(file="../Imagenes/op.png")
        #self.donkey = PhotoImage(file="../Images/donkey1.png")
        #self.plane = PhotoImage(file="../Images/plane.png")
        #self.car = PhotoImage(file="../Images/car.png")
        #self.cityIcon = PhotoImage(file="../Images/city1.png")
        #self.donkeyDead = PhotoImage(file="../Images/donkeyDead.png")
        #self.backParker = PhotoImage(file="../Images/mochilero.png")

        self.frame = Frame(self.app)
        self.frame.pack(fill="both")
        self.frame.config(width=1360, height=760, bg='navy')


        self.entry3 = StringVar()
        self.textField3 = Entry(self.frame, textvariable=self.entry3).place(x=10, y=60)

        self.button2 = Button(
            button2=Button(self.frame, text="Cargar Datos", command="self.drawElement").place(x=10, y=90))


        self.button4 = Button(button4=Button(self.frame, text="Suma", command="self.transportSelection").place(x=10, y=200))
        self.button5 = Button(button5=Button(self.frame, text="Resta", command="self.transportSelection2").place(x=10, y=230))
        self.button6 = Button(button6=Button(self.frame, text="Multiplicación", command="self.transportSelection3").place(x=10, y=260))
        self.button7 = Button(button7=Button(self.frame, text="División", command="self.timeTravel").place(x=10, y=290))
        self.button8 = Button(button8=Button(self.frame, text="Comparar", command="self.timeTravel").place(x=10, y=320))




        self.map = Canvas(self.frame, width=1360, height = 760, bg='grey')
        self.map.place(x=250, y=0)

        #self.map.create_rectangle(530, 30, 600, 100, fill="gold")

        self.map.create_image(10, 200, anchor=NW, image=self.alu)
        self.map.create_text(250, 530, fill="black", font="Times 30", text="ALU")

        self.map.create_image(30, 30, anchor=NW, image=self.mar)
        self.map.create_text(100, 100, fill="black", font="Times 30", text="MAR")

        self.map.create_image(350, 30, anchor=NW, image=self.ir)
        self.map.create_text(425, 100, fill="black", font="Times 30", text="IR")

        self.map.create_image(30, 610, anchor=NW, image=self.mbr)
        self.map.create_text(100, 680, fill="black", font="Times 30", text="MBR")

        self.map.create_image(800, 200, anchor=NW, image=self.pc)
        self.map.create_text(870, 270, fill="black", font="Times 30", text="PC")

        self.map.create_image(800, 350, anchor=NW, image=self.uc)
        self.map.create_text(870, 420, fill="black", font="Times 30", text="UC")

        self.map.create_image(800, 500, anchor=NW, image=self.ac)
        self.map.create_text(870, 570, fill="black", font="Times 30", text="AC")

        self.map.create_image(470, 350, anchor=NW, image=self.banco)
        self.map.create_text(540, 570, fill="black", font="Times 30", text="Banco Registros")

        self.map.create_image(20, 190, anchor=NW, image=self.op1)
        self.map.create_text(50, 220, fill="black", font="Times 30", text="OP1")

        self.map.create_image(350, 190, anchor=NW, image=self.op1)
        self.map.create_text(380, 220, fill="black", font="Times 30", text="OP2")

        #self.openFile()
        self.app.mainloop()


main()