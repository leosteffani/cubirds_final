class Placar:
    def __init__(self):
        self.__pontos_player_local = 0
        self.__pontos_player_remoto = 0
        self.__bandos_formados_local = []
        self.__bandos_formados_remoto = []

    def get_pontos_local(self):
        return self.__pontos_player_local
    def get_pontos_remoto(self):
        return self.__pontos_player_remoto
    def atualizar_placar_local(self,pontos,bando):
        self.__pontos_player_local += pontos
        self.__bandos_formados_local.append(bando)
        
    def atualizar_placar_remoto(self, pontos, bandos):
        self.pontos_player_remoto = int(pontos)
        self.bandos_remoto = []
    
        if bandos != "sem_bandos":
            bandos_split = bandos.split(",")
        for bando in bandos_split:
            especie_tamanho = bando.split("/")
            especie = int(especie_tamanho[0])
            tamanho = int(especie_tamanho[1])
            self.bandos_remoto.append([especie, tamanho])

    def get_bandos_local(self):
        return self.__bandos_formados_local
    def get_bandos_remoto(self):
        return self.__bandos_formados_remoto