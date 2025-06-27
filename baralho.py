from carta import Carta
import random

class Baralho:
    def __init__(self):
        self.__cartas = []
        self.__referencia_especies = [
            [2, 3, 7],  # especie 1: 2 cartas = bando pequeno, 3 cartas = bando grande, 7 cartas = total
            [3, 4, 10],  # especie 2: 3 cartas = bando pequeno, 4 cartas = bando grande, 10 cartas = total
            [3, 4, 10],  # especie 3: 3 cartas = bando pequeno, 4 cartas = bando grande, 10 cartas = total
            [4, 6, 13],  # especie 4: 4 cartas = bando pequeno, 6 cartas = bando grande, 13 cartas = total
            [4, 6, 13],  # especie 5: 4 cartas = bando pequeno, 6 cartas = bando grande, 13 cartas = total
            [5, 7, 17],  # especie 6: 5 cartas = bando pequeno, 7 cartas = bando grande, 17 cartas = total
            [6, 9, 20],  # especie 7: 6 cartas = bando pequeno, 9 cartas = bando grande, 20 cartas = total
            [6, 9, 20],  # especie 8: 6 cartas = bando pequeno, 9 cartas = bando grande, 20 cartas = total
        ]

    def get_cartas(self):
        return self.__cartas
    def get_num_cartas(self):
        return len(self.__cartas)
    def pegar_cartas(self,n_cartas):
        cartas = []
        for _ in range(n_cartas):
            temp = self.__cartas.pop()
            cartas.append(temp)
        return cartas
    def set_baralho(self,cartas_string):
        lista_cartas = list(cartas_string)
        for carta in lista_cartas:
            carta = int(carta)
            tipo_carta = self.__referencia_especies[carta-1]
            obj_carta = Carta(carta,tipo_carta[0],tipo_carta[1])
            self.__cartas.append(obj_carta)

    def criar_baralho(self):
        for especie in range(len(self.__referencia_especies)):
            for i in range(self.__referencia_especies[especie][2]):
                bando_pequeno = self.__referencia_especies[especie][0]
                bando_grande = self.__referencia_especies[especie][1]
                self.__cartas.append(Carta(especie + 1, bando_pequeno, bando_grande))
        random.shuffle(self.__cartas)  # Embaralha as cartas do baralho

    def remove_carta(self, index):
        self.__cartas.pop(index)

    def get_cartas_iniciais(self):
        retorno = []
        for carta in self.__cartas:
            retorno.append(str(carta.get_especie()))
        retorno = "".join(retorno)
        return retorno