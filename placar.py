class Placar:
    def __init__(self):
        self.__pontos_player_local = 0
        self.__pontos_player_remoto = 0
        self.__bandos_formados_local = [] # [[especie, tamanho], ...] 1 ponto = bando pequeno, 2 pontos = bando grande
        self.__bandos_formados_remoto = [] # [[especie, tamanho], ...] 1 ponto = bando pequeno, 2 pontos = bando grande

    # get_pontos_local
    def get_pontos_local(self):
        return self.__pontos_player_local
    
    # get_pontos_remoto
    def get_pontos_remoto(self):
        return self.__pontos_player_remoto
    
    # get_bandos_local
    def get_bandos_local(self):
        return self.__bandos_formados_local
    
    # get_bandos_remoto
    def get_bandos_remoto(self):
        return self.__bandos_formados_remoto
    
    # atualizar_placar_local
    def atualizar_placar_local(self, pontos, especie):
        self.__pontos_player_local += pontos
        self.__bandos_formados_local.append([especie, pontos])

    # atualizar_placar_remoto
    def atualizar_placar_remoto(self, pontos, bandos):
        self.__pontos_player_remoto = int(pontos)
        self.__bandos_formados_remoto = []

        if bandos != "sem_bandos":
            bandos_split = bandos.split(",")
            for bando in bandos_split:
                especie_tamanho = bando.split("/")
                especie = int(especie_tamanho[0])
                tamanho = int(especie_tamanho[1])
                self.__bandos_formados_remoto.append([especie, tamanho])

