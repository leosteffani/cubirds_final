class Placar:
    def __init__(self):
        self.__placar_local = 0
        self.__placar_remoto = 0
    def get_placar_local(self):
        return self.__placar_local
    def get_placar_remoto(self):
        return self.__placar_remoto
    def add_placar_local(self,pontos):
        self.__placar_local += pontos
    def add_placar_remoto(self,pontos):
        self.__placar_remoto += pontos