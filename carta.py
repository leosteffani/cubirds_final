class Carta:
    def __init__(self,especie,bando_pequeno,bando_grande):
        self.__especie = especie
        self.__bando_grande = bando_grande
        self.__bando_pequeno = bando_pequeno
    def get_especie(self):
        return self.__especie
    def get_bando_grande(self):
        return self.__bando_grande
    def get_bando_pequeno(self):
        return self.__bando_pequeno