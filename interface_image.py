class InterfaceImage:
    def __init__(self):
        self.__baralho = 0
        self.__mesa = []
        self.__placar_local = 0
        self.__placar_remoto = 0
        self.__cartas_na_mao_local = []
        self.__n_cartas_jogador_remoto = 0
        self.__bandos_local = []
        self.__bandos_remoto = []

    #getters
    def get_baralho(self):
        return self.__baralho
    def get_mesa(self):
        return self.__mesa
    def get_placar_local(self):
        return self.__placar_local
    def get_placar_remoto(self):
        return self.__placar_remoto
    def get_cartas_na_mao_local(self):
        return self.__cartas_na_mao_local
    def get_n_cartas_jogador_remoto(self):
        return self.__n_cartas_jogador_remoto
    def get_bandos_local(self):
        return self.__bandos_local
    def get_bandos_remoto(self):
        return self.__bandos_remoto
    

    # setters
    def set_baralho(self, baralho):
        self.__baralho = baralho
    def set_mesa(self, mesa):
        self.__mesa = mesa
    def set_placar_local(self, placar_local):
        self.__placar_local = placar_local
    def set_placar_remoto(self, placar_remoto):
        self.__placar_remoto = placar_remoto
    def set_cartas_na_mao_local(self, cartas_na_mao_local):
        self.__cartas_na_mao_local = cartas_na_mao_local
    def set_n_cartas_jogador_remoto(self, n_cartas_jogador_remoto):
        self.__n_cartas_jogador_remoto = n_cartas_jogador_remoto
    def set_bandos_local(self, bandos_local):
        self.__bandos_local = bandos_local
    def set_bandos_remoto(self, bandos_remoto):
        self.__bandos_remoto = bandos_remoto

