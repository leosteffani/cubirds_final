class InterfaceImage:
    def __init__(self):
        self.__placar_local = 0
        self.__placar_remoto = 0
        self.__baralho = 0
        self.__cartas_na_mao_local = []
        self.__cartas_mesa = []
        self.__n_cartas_jogador_remoto = 0
        self.__bandos_local = {}
        self.__bandos_remoto = {}

    def set_baralho(self,n_cartas):
        self.__baralho = n_cartas
    def set_mesa(self,matriz_mesa):
        self.__cartas_mesa = matriz_mesa
    def set_n_cartas_jogador_remoto(self,n_cartas):
        self.__n_cartas_jogador_remoto = n_cartas
    def set_pontos_local(self,pontos):
        self.__placar_local = pontos
    def set_pontos_remoto(self,pontos):
        self.__placar_remoto = pontos
    def set_mao(self,cartas):
        self.__cartas_na_mao_local = cartas

    def get_baralho(self):
        return self.__baralho
    def get_mesa(self):
        return self.__cartas_mesa
    def get_n_cartas_jogador_remoto(self):
        return self.__n_cartas_jogador_remoto
    def get_pontos_local(self):
        return self.__placar_local
    def get_pontos_remoto(self):
        return self.__placar_remoto
    def get_mao(self):
        return self.__cartas_na_mao_local


