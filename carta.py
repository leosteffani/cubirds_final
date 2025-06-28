class Carta:
    def __init__(self,especie,bando_pequeno,bando_grande):
        self.__especie = especie
        self.__bando_grande = bando_grande
        self.__bando_pequeno = bando_pequeno

    # get_especie
    def get_especie(self):
        return self.__especie
    
    # get_bando_grande
    def get_bando_grande(self):
        return self.__bando_grande
    
    # get_bando_pequeno
    def get_bando_pequeno(self):
        return self.__bando_pequeno