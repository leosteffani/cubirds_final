class Player:
    def __init__(self):
        self.__identifier = 0
        self.__nome = ""
        self.__mao = []
        self.__cartas_selecionadas = []
    def get_cartas_selecionadas(self):
        retorno = []
        for posicao in self.__cartas_selecionadas:
            retorno.append(self.__mao[posicao])
        return retorno
    def remover_cartas_selecionadas_da_mao(self):
        for posicao in self.__cartas_selecionadas:
            self.__mao.pop(posicao)
    def adicionar_cartas_na_mao(self,cartas):
        for carta in cartas:
            self.__mao.append(carta)
    def initialize(self,identifier,nome):
        self.__identifier = identifier
        self.__nome = nome
    def get_mao(self):
        return self.__mao
    def adicionar_carta_seleionada(self,carta):
        self.__cartas_selecionadas.append(carta)
    def verificar_selecao(self,posicao):
        if posicao in self.__cartas_selecionadas:
            return True
        else:
            return False
    def remover_carta_selecionada(self,posicao):
        self.__cartas_selecionadas.remove(posicao)
