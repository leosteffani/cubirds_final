class Player:
    def __init__(self):
        self.__identifier = 0
        self.__nome = ""
        self.__mao = []
        self.__cartas_selecionadas = []

    # initialize
    def initialize(self, id, nome):
        self.__identifier = id
        self.__nome = nome

    # adicionar_cartas_na_mao
    def adicionar_cartas_na_mao(self, cartas):
        for carta in cartas:
            self.__mao.append(carta)
    
    # remover_cartas_selecionadas_da_mao
    def remover_cartas_selecionadas_da_mao(self):
        # remove em ordem decrescente para evitar mudança de índices
        for posicao in sorted(self.__cartas_selecionadas, reverse=True):
            self.__mao.pop(posicao)
        # limpa a lista de cartas selecionadas após remoção
        self.__cartas_selecionadas.clear()

    # get_mao
    def get_mao(self):
        return self.__mao

    # adicionar_carta_selecionada
    def adicionar_carta_selecionada(self, carta):
        self.__cartas_selecionadas.append(carta)
    
    # remover_carta_selecionada
    def remover_carta_selecionada(self, posicao):
        self.__cartas_selecionadas.remove(posicao)
    
    # get_cartas_selecionadas    
    def get_cartas_selecionadas(self):
        retorno = []
        for posicao in self.__cartas_selecionadas:
            retorno.append(self.__mao[posicao])
        return retorno
    
    # verificar_selecao
    def verificar_selecao(self, posicao):
        if posicao in self.__cartas_selecionadas:
            return True
        else:
            return False

