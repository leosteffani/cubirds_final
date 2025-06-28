from tkinter import *

class PlayerInterface:
    def __init__(self):
        self.main_window = Tk()
        self.n_pontos_player1 = 1
        self.n_pontos_player2 = 7
        self.n_cartas_baralho = 43
        self.__matriz_mesa = [[1, 2, 3], [4, 5, 6], [7, 8, 1], [2, 5, 7]]
        self.__mao = [1, 2, 3, 4, 5, 6, 7, 8]
        self.__bandos_local = [[4,2]]
        self.__bandos_remoto = [[6,2],[7,1]]
        self.__n_cartas_jogador_remoto = 8
        self.__turno = False

        #imagens usadas ate o momento
        #tamanho padrao das cartas 86x120
        self.birds_images = [PhotoImage(file="images/carta1.png"),
                             PhotoImage(file="images/carta2.png"),
                             PhotoImage(file="images/carta3.png"),
                             PhotoImage(file="images/carta4.png"),
                             PhotoImage(file="images/carta5.png"),
                             PhotoImage(file="images/carta6.png"),
                             PhotoImage(file="images/carta7.png"),
                             PhotoImage(file="images/carta8.png")
                             ]
        self.birds_images_select = [PhotoImage(file="images/carta1s.png"),
                             PhotoImage(file="images/carta2s.png"),
                             PhotoImage(file="images/carta3s.png"),
                             PhotoImage(file="images/carta4s.png"),
                             PhotoImage(file="images/carta5s.png"),
                             PhotoImage(file="images/carta6s.png"),
                             PhotoImage(file="images/carta7s.png"),
                             PhotoImage(file="images/carta8s.png")
                             ]
        self.add_image = PhotoImage(file="images/add.png")
        self.__back_card = PhotoImage(file="images/back.png")
        self.formar_bando_image = PhotoImage(file="images/formar bando.png")
        self.__passar_turno_image= PhotoImage(file="images/passar turno.png")

        self.fill_main_window()
        #self.create_descarte()
        # preenchimento da janela
        self.main_window.mainloop()

    def fill_main_window(self):
        # Título, dimensionamento e fundo da janela
        self.main_window.title("Cubirds")
        #self.main_window.iconbitmap("images/icon.ico")
        self.main_window.geometry("1920x1080")
        self.main_window.resizable(False, False)
        self.main_window["bg"] = "lightgray"
        #configuracao do grid main window
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.columnconfigure(1, weight=1)
        self.main_window.columnconfigure(2, weight=1)
        self.main_window.rowconfigure(0, weight=0)
        self.main_window.rowconfigure(1, weight=1)
        self.main_window.rowconfigure(2, weight=1)

        #cria os frames que serao usados
        self.table_frame = Frame(self.main_window,width= 1280,height= 480,bg="lightgray")
        self.table_frame.grid(row=1,column=1)
        self.mao_frame = Frame(self.main_window, width=1280, height=120, bg="lightgray")
        self.mao_frame.grid(row=2, column=1)
        self.mao_remota_frame = Frame(self.main_window, width=1280, height=120, bg="lightgray")
        self.mao_remota_frame.grid(row=0, column=1)
        self.bandos_local_frame = Frame(self.main_window, width=172, height=600, bg="lightgray")
        self.bandos_local_frame.grid(row=1, column=0)
        self.bandos_remoto_frame = Frame(self.main_window, width=172, height=600, bg="lightgray")
        self.bandos_remoto_frame.grid(row=1, column=2)
        self.acoes_frame = Frame(self.main_window, width=172, height=200, bg="lightgray")
        self.acoes_frame.grid(row=2, column=0)


        # imagem vazia para tudo ficar centralizado (nao sei se tem um jeito melhor de fazer isso)
        w = Canvas(self.main_window, width=86, height=120, highlightthickness=0, bg="lightgray")
        w.grid(row=0, column=2, sticky="NSEW")

        #métodos que criam os elementos
        self.create_menubar()
        #self.tela_inicial()

    def tela_inicial(self):
        self.create_table()
        self.create_baralho()
        self.create_placar()
        self.create_mao()
        self.create_mao_remota()
        self.create_bandos_remoto()
        self.create_bandos_local()
        self.create_formar_bando()
        self.create_finalizar_turno()
    #cria o descarte(desativado)
    def create_formar_bando(self):
        descarte = Label(self.acoes_frame, bd=0,image=self.formar_bando_image)
        descarte.bind("<Button-1>", lambda event: self.formar_bando())
        descarte.grid(row=0, column=0)
    def create_finalizar_turno(self):
        descarte = Label(self.acoes_frame, bd=0,image=self.__passar_turno_image)
        descarte.bind("<Button-1>", lambda event: self.finalizar_turno())
        descarte.grid(row=1, column=0)
    #cria o placar
    def create_placar(self):
        if self.__turno:
            placar= Label(self.main_window, bg="steelblue", text=str(self.n_pontos_player1)+' VS '+str(self.n_pontos_player2), font="arial 30")
            placar.grid(row=0, column=2)
        else:
            placar = Label(self.main_window, bg="firebrick2",text=str(self.n_pontos_player1) + ' VS ' + str(self.n_pontos_player2), font="arial 30")
            placar.grid(row=0, column=2)
    #cria o baralho
    def create_baralho(self):
        baralho = Label(self.main_window, bg="lightgray", text=self.n_cartas_baralho, font="arial 40",image=self.birds_images[0], compound='center')
        baralho.bind("<Button-1>", lambda event: self.baralho())
        baralho.grid(row=0, column=0)

    #preenche o grid da mesa
    def create_table(self):
        #adiciona os botoes add no inicio de cada linha
        for linha in range(len(self.__matriz_mesa)):
            aLabel = Label(self.table_frame, bd=0, image=self.add_image)
            aLabel.grid(row=linha, column=0)
            aLabel.bind("<Button-1>", lambda event,a_line=linha, a_column=0: self.add( a_line, a_column))
        #adiciona as cartas
        for linha in range(len(self.__matriz_mesa)):
            for coluna in range(1,len(self.__matriz_mesa[linha])+1):
                carta = self.__matriz_mesa[linha][coluna-1]
                aLabel = Label(self.table_frame, bd=0, image=self.birds_images[carta-1])
                aLabel.grid(row=linha, column=coluna)
        # adiciona os botoes add no final de cada linha
        for linha in range(len(self.__matriz_mesa)):
            aLabel = Label(self.table_frame, bd=0, image=self.add_image)
            aLabel.grid(row=linha, column=len(self.__matriz_mesa[linha])+2)
            aLabel.bind("<Button-1>", lambda event,a_line=linha, a_column=len(self.__matriz_mesa[linha])+1: self.add(a_line, a_column))
    #preenche o grid da mao
    def create_mao(self):
        for x in range(len(self.__mao)):
            carta_mao = Label(self.mao_frame, bd=0, image=self.birds_images[self.__mao[x]-1])
            carta_mao.grid(row=0, column=x+1)
            carta_mao.bind("<Button-1>", lambda event,a_column=x: self.click_carta_mao(a_column))
    def create_mao_remota(self):
        for x in range(self.__n_cartas_jogador_remoto):
            carta_mao = Label(self.mao_remota_frame, bd=0, image=self.__back_card)
            carta_mao.grid(row=0, column=x+1)
    def create_bandos_local(self):
        for x in range(len(self.__bandos_local)):
            for y in range(self.__bandos_local[x][1]):
                carta_bando = Label( self.bandos_local_frame, bd=0, image=self.birds_images[self.__bandos_local[x][0]-1])
                carta_bando.grid(row=x, column=y)
    def create_bandos_remoto(self):
        for x in range(len(self.__bandos_remoto)):
            for y in range(self.__bandos_remoto[x][1]):
                carta_mao = Label( self.bandos_remoto_frame, bd=0, image=self.birds_images[self.__bandos_remoto[x][0]-1])
                carta_mao.grid(row=x, column=y)
    #cria o menu e seus botoes
    def create_menubar(self):
        self.menubar = Menu(self.main_window)
        self.menubar.option_add('*tearOff', FALSE)
        self.main_window['menu'] = self.menubar

        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='File')

        self.menu_file.add_command(label='Iniciar jogo', command=self.start_match)
        self.menu_file.add_command(label='restaurar estado inicial', command=self.start_game)

        self.menubar.option_add('*tearOff', FALSE)

    #metodos de cada tipo de botao
    def start_match(self):
        self.tela_inicial()
        print('precionou iniciar jogo')
    def start_game(self):
        print('precionou restaurar estado inicial')
    def click_mesa(self, a_line, a_column):
        print('precionou botão na posicao '+str(a_line)+" "+ str(a_column) )
    def add(self, a_line, a_column):
        print('precionou botão add na posicao ' + str(a_line) + " " + str(a_column))
    def baralho(self):
        print('precionou baralho')
        #self.n_cartas_baralho +=1
        #self.create_baralho()
    def descarte(self):
        print('precionou descarte')
    def click_carta_mao(self,a_column):
        print('precionou botão carta da mao na posicao '+str(a_column))
    def finalizar_turno(self):
        print("finalizar_turno")
    def formar_bando(self):
        print("formar_bando")

interface = PlayerInterface()
