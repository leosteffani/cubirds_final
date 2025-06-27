class Placar:
    def __init__(self):
        self.__placar_local = 0
        self.__placar_remoto = 0
        self.__bandos_formados_local = []
        self.__bandos_formados_remoto = []

    def get_placar_local(self):
        return self.__placar_local
    def get_placar_remoto(self):
        return self.__placar_remoto
    def atualizar_placar_local(self,pontos,bando):
        self.__placar_local += pontos
        self.__bandos_formados_local.append(bando)
    def atualizar_placar_remoto(self,pontos,bando):
        self.__placar_remoto += pontos
        self.__bandos_formados_remoto.append(bando)