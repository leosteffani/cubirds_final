from carta import Carta
import random

class Baralho:
    def __init__(self):
        self.__cartas = []
        self.__dicionario_especies = [
            [2, 3, 7], # especie 1: 2 cartas = bando pequeno, 3 cartas = bando grande, 7 cartas = total
            [3, 4, 10], # especie 2: 3 cartas = bando pequeno, 4 cartas = bando grande, 10 cartas = total
            [3, 4, 10], # especie 3: 3 cartas = bando pequeno, 4 cartas = bando grande, 10 cartas = total
            [4, 6, 13], # especie 4: 4 cartas = bando pequeno, 6 cartas = bando grande, 13 cartas = total
            [4, 6, 13], # especie 5: 4 cartas = bando pequeno, 6 cartas = bando grande, 13 cartas = total
            [5, 7, 17], # especie 6: 5 cartas = bando pequeno, 7 cartas = bando grande, 17 cartas = total
            [6, 9, 20], # especie 7: 6 cartas = bando pequeno, 9 cartas = bando grande, 20 cartas = total
            [6, 9, 20], # especie 8: 6 cartas = bando pequeno, 9 cartas = bando grande, 20 cartas = total
        ]

    #get_cartas
    def get_cartas(self):
        return self.__cartas
    
    #get_num_cartas
    def get_num_cartas(self):
        return len(self.__cartas)
    
    #get_dicionario_especies
    def get_dicionario_especies(self):
        return self.__dicionario_especies
    
    #get_cartas_iniciais
    def get_cartas_iniciais(self):
        retorno = []
        for carta in self.__cartas:
            retorno.append(str(carta.get_especie()))
        retorno = "".join(retorno)
        return retorno
    
    #pegar_cartas
    def pegar_cartas(self, n_cartas):
        cartas = []
        for _ in range(n_cartas):
            temp = self.__cartas.pop()
            cartas.append(temp)
        return cartas
    
    # criar_baralho
    def criar_baralho(self):
        for especie in range(len(self.__dicionario_especies)):
            for total_cartas in range(self.__dicionario_especies[especie][2]):
                bando_pequeno = self.__dicionario_especies[especie][0]
                bando_grande = self.__dicionario_especies[especie][1]
                obj_carta = Carta(especie+1, bando_pequeno, bando_grande)
                self.__cartas.append(obj_carta)

        random.shuffle(self.__cartas)

    #set_baralho
    def set_baralho(self, cartas_string):
        lista_cartas = list(cartas_string)
        for carta in lista_cartas:
            especie = int(carta)
            especie_dicionario = self.__dicionario_especies[especie-1]
            obj_carta = Carta(especie, especie_dicionario[0], especie_dicionario[1])
            self.__cartas.append(obj_carta)
    
    #remover_carta
    def remover_carta(self, index):
        self.__cartas.pop(index)