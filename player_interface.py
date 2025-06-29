from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from time import sleep
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from mesa import Mesa


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.main_window = Tk()

        self.n_pontos_local = 0
        self.n_pontos_remoto = 0
        self.n_cartas_baralho = 0
        self.__matriz_mesa = []
        self.__mao = []
        self.__bandos_local = []
        self.__bandos_remoto = []
        self.__n_cartas_jogador_remoto = 0
        self.__turno = False
        self.__selecao_mao = []

        # imagens usadas ate o momento
        # tamanho padrao das cartas 86x120
        self.birds_images = [PhotoImage(file="images/carta1.png"),
                             PhotoImage(file="images/carta2.png"),
                             PhotoImage(file="images/carta3.png"),
                             PhotoImage(file="images/carta4.png"),
                             PhotoImage(file="images/carta5.png"),
                             PhotoImage(file="images/carta6.png"),
                             PhotoImage(file="images/carta7.png"),
                             PhotoImage(file="images/carta8.png")]

        self.birds_images_select = [PhotoImage(file="images/carta1s.png"),
                                    PhotoImage(file="images/carta2s.png"),
                                    PhotoImage(file="images/carta3s.png"),
                                    PhotoImage(file="images/carta4s.png"),
                                    PhotoImage(file="images/carta5s.png"),
                                    PhotoImage(file="images/carta6s.png"),
                                    PhotoImage(file="images/carta7s.png"),
                                    PhotoImage(file="images/carta8s.png")]

        self.add_image = PhotoImage(file="images/add.png")
        self.__back_card = PhotoImage(file="images/back.png")
        self.formar_bando_image = PhotoImage(file="images/formar bando.png")
        self.__passar_turno_image = PhotoImage(file="images/passar turno.png")

        self.fill_main_window()
        self.mesa = Mesa(self)
        game_state = self.mesa.get_status()
        self.atualizar_interface(game_state)
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)
        # preenchimento da janela
        self.main_window.mainloop()

    #### CONFIGURAÇÃO DA INTERFACE ####

    def fill_main_window(self):
        # Título, dimensionamento e fundo da janela
        self.main_window.title("Cubirds")
        self.main_window.geometry("1920x1000")
        self.main_window.resizable(False, False)
        self.main_window["bg"] = "lightgray"

        # configuracao do grid main window
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.columnconfigure(1, weight=1)
        self.main_window.columnconfigure(2, weight=1)
        self.main_window.rowconfigure(0, weight=0)
        self.main_window.rowconfigure(1, weight=1)
        self.main_window.rowconfigure(2, weight=1)

        # cria os frames que serao usados
        self.table_frame = Frame(self.main_window, width=1280, height=480, bg="lightgray")
        self.table_frame.grid(row=1, column=1)
        self.linhas_frames = [Frame(self.table_frame, width=1280, height=120, bg="lightgray"),
                              Frame(self.table_frame, width=1280, height=120, bg="lightgray"),
                              Frame(self.table_frame, width=1280, height=120, bg="lightgray"),
                              Frame(self.table_frame, width=1280, height=120, bg="lightgray")]
        for frame in range(len(self.linhas_frames)):
            self.linhas_frames[frame].grid(row=frame, column=0)
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

        # métodos que criam os elementos
        self.create_menubar()
        self.draw_tela()

    def draw_tela(self):
        self.clear_frame(self.linhas_frames[0])
        self.clear_frame(self.linhas_frames[1])
        self.clear_frame(self.linhas_frames[2])
        self.clear_frame(self.linhas_frames[3])
        self.clear_frame(self.mao_frame)
        self.clear_frame(self.mao_remota_frame)
        self.clear_frame(self.bandos_local_frame)
        self.clear_frame(self.bandos_remoto_frame)
        self.create_table()
        self.create_baralho()
        self.create_placar()
        self.create_mao()
        self.create_mao_remota()
        self.create_bandos_remoto()
        self.create_bandos_local()
        self.create_formar_bando()
        self.create_finalizar_turno()

    #### CRIAÇÃO DOS ELEMENTOS DA INTERFACE ####

    def create_menubar(self):
        self.menubar = Menu(self.main_window)
        self.menubar.option_add('*tearOff', FALSE)
        self.main_window['menu'] = self.menubar

        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='File')

        self.menu_file.add_command(label='Iniciar jogo', command=self.start_match)

        self.menubar.option_add('*tearOff', FALSE)

    def create_placar(self):
        if self.__turno:
            placar = Label(self.main_window, bg="steelblue",
                           text=str(self.n_pontos_local) + ' VS ' + str(self.n_pontos_remoto), font="arial 30")
            placar.grid(row=0, column=2)
        else:
            placar = Label(self.main_window, bg="firebrick2",
                           text=str(self.n_pontos_local) + ' VS ' + str(self.n_pontos_remoto), font="arial 30")
            placar.grid(row=0, column=2)

    def create_baralho(self):
        baralho = Label(self.main_window, bg="lightgray", text=self.n_cartas_baralho, font="arial 40",
                        image=self.birds_images[0], compound='center')
        baralho.grid(row=0, column=0)

    def create_table(self):
        # adiciona os botoes add no inicio de cada linha
        for linha in range(len(self.__matriz_mesa)):
            aLabel = Label(self.linhas_frames[linha], bd=0, image=self.add_image)
            aLabel.grid(row=0, column=0)
            aLabel.bind("<Button-1>", lambda event, a_line=linha, a_column=0: self.jogar_cartas(a_line, a_column))
        # adiciona as cartas
        for linha in range(len(self.__matriz_mesa)):
            for coluna in range(1, len(self.__matriz_mesa[linha]) + 1):
                carta = self.__matriz_mesa[linha][coluna - 1]
                aLabel = Label(self.linhas_frames[linha], bd=0, image=self.birds_images[carta - 1])
                aLabel.grid(row=0, column=coluna)
        # adiciona os botoes add no final de cada linha
        for linha in range(len(self.__matriz_mesa)):
            aLabel = Label(self.linhas_frames[linha], bd=0, image=self.add_image)
            aLabel.grid(row=0, column=len(self.__matriz_mesa[linha]) + 2)
            aLabel.bind("<Button-1>",
                        lambda event, a_line=linha, a_column=len(self.__matriz_mesa[linha]) + 1: self.jogar_cartas(
                            a_line, a_column))

    def create_mao(self):
        for x in range(len(self.__mao)):
            if self.__selecao_mao[x] == False:
                carta_mao = Label(self.mao_frame, bd=0, image=self.birds_images[self.__mao[x] - 1])
                carta_mao.grid(row=0, column=x + 1)
                carta_mao.bind("<Button-1>", lambda event, a_column=x: self.selecionar_carta(a_column))
            else:
                carta_mao = Label(self.mao_frame, bd=0, image=self.birds_images_select[self.__mao[x] - 1])
                carta_mao.grid(row=0, column=x + 1)
                carta_mao.bind("<Button-1>", lambda event, a_column=x: self.selecionar_carta(a_column))

    def create_mao_remota(self):
        for x in range(self.__n_cartas_jogador_remoto):
            carta_mao = Label(self.mao_remota_frame, bd=0, image=self.__back_card)
            carta_mao.grid(row=0, column=x + 1)

    def create_bandos_local(self):
        for x in range(len(self.__bandos_local)):
            for y in range(self.__bandos_local[x][1]):
                carta_bando = Label(self.bandos_local_frame, bd=0,
                                    image=self.birds_images[self.__bandos_local[x][0] - 1])
                carta_bando.grid(row=x, column=y)

    def create_bandos_remoto(self):
        for x in range(len(self.__bandos_remoto)):
            for y in range(self.__bandos_remoto[x][1]):
                carta_mao = Label(self.bandos_remoto_frame, bd=0,
                                  image=self.birds_images[self.__bandos_remoto[x][0] - 1])
                carta_mao.grid(row=x, column=y)

    def create_formar_bando(self):
        descarte = Label(self.acoes_frame, bd=0, image=self.formar_bando_image)
        descarte.bind("<Button-1>", lambda event: self.formar_bando())
        descarte.grid(row=0, column=0)

    def create_finalizar_turno(self):
        descarte = Label(self.acoes_frame, bd=0, image=self.__passar_turno_image)
        descarte.bind("<Button-1>", lambda event: self.finalizar_turno())
        descarte.grid(row=1, column=0)

    def clear_frame(self, frame):
        """Destroys all widgets within a given Tkinter frame."""
        for widget in frame.winfo_children():
            widget.destroy()

    #### MÉTODOS DE INTERAÇÃO ####
    def atualizar_interface(self, interface):
        self.n_pontos_local = interface.get_placar_local()
        self.n_pontos_remoto = interface.get_placar_remoto()
        self.n_cartas_baralho = interface.get_baralho()
        self.__matriz_mesa = interface.get_mesa()
        self.__mao = interface.get_cartas_na_mao_local()
        self.__bandos_local = interface.get_bandos_local()
        self.__bandos_remoto = interface.get_bandos_remoto()
        self.__n_cartas_jogador_remoto = interface.get_n_cartas_jogador_remoto()
        self.__turno = interface.get_turno()
        self.__selecao_mao = [False] * len(self.__mao)
        self.draw_tela()

    def adicionar_selecao_carta(self, posicao):
        self.__selecao_mao[posicao] = True
        self.draw_tela()

    def remover_selecao_carta(self, posicao):
        self.__selecao_mao[posicao] = False
        self.draw_tela()

    def encerrar_aplicacao(self):
        sleep(5)
        self.main_window.destroy()

    def send_move(self, move_to_send):
        self.dog_server_interface.send_move(move_to_send)

    def notificar(self, message):
        messagebox.showinfo(message=message)

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        code = start_status.get_code()
        message = start_status.get_message()
        if code == "0" or code == "1":
            messagebox.showinfo(message=message)
        else:
            players = start_status.get_players()
            local_player_id = start_status.get_local_id()
            self.mesa.iniciar_partida(players, local_player_id)
            move_to_send = self.mesa.get_move(inicio=True)
            self.dog_server_interface.send_move(move_to_send)
            self.mesa.remover_cartas_do_baralho()
            game_state = self.mesa.get_status()
            self.atualizar_interface(game_state)

    def receive_start(self, start_status):
        players = start_status.get_players()
        name = players[0][0]
        order = players[0][2]
        identifier = start_status.get_local_id()
        mensagem = start_status.get_message()
        self.mesa.inicializar_local_player(identifier, name)
        if order == "1":
            self.mesa.set_match_status(1)
        else:
            self.mesa.set_match_status(4)
        self.notificar(mensagem)

    def selecionar_carta(self, posicao):
        self.mesa.selecionar_carta(posicao)

    def jogar_cartas(self, linha, coluna):
        self.mesa.jogar_cartas(linha, coluna)

    def formar_bando(self):
        self.mesa.formar_bando()

    def finalizar_turno(self):
        self.mesa.finalizar_turno()

    def receive_move(self, jogada):
        self.mesa.receber_jogada(jogada)

    def receive_withdrawal_notification(self):
        self.mesa.set_match_status(5)
        self.notificar("O seu adversário abandonou a partida, você ganhou!")
        self.encerrar_aplicacao()


interface = PlayerInterface()