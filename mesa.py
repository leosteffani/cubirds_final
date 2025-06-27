from baralho import Baralho
from carta import Carta
from interface2 import PlayerInterface
from player import Player
from placar import Placar
from interface_image import InterfaceImage

class Mesa:
    def __init__(self):
        self.__player = Player()
        self.__baralho = Baralho()
        self.__placar = Placar()
        self.__interface = PlayerInterface()
    def descartar(self):
        pass
    def finalizar_turno(self):
        pass
    def formar_bando(self):
        selecionadas = self.__player.get_cartas_selecionadas()
        if len(selecionadas) > 0:
            pontos = self.verificar_formacao_bando(selecionadas)
            if pontos > 0:
                self.__placar.add_bandos_local(selecionadas.get_especie(),pontos)
                self.__player.remover_cartas_selecionadas()
            else:
                self.__interface.notificar("Não é possível formar um bando")
        else:
            self.__interface.notificar("Você deve selecionar cartas para formar bando")
    def iniciar_partida(self):
        self.__player.inicialize("00","leonardo")
        self.__baralho.criar_baralho()
        self.criar_mesa()
        cartas = self.__baralho.pegar_cartas(8)
        self.__player.adicionar_cartas_na_mao(cartas)
        self.__player.alt_turno()

    def get_status(self):
        interface_image = InterfaceImage()

        # baralho
        interface_image.set_baralho(self.baralho.get_num_cartas())

        # numero de cartas na mão do jogador remoto
        interface_image.set_n_cartas_jogador_remoto(self.n_cartas_jogador_remoto)

        # placar
        interface_image.set_pontos_local(self.placar.get_pontos_local())
        interface_image.set_pontos_remoto(self.placar.get_pontos_remoto())

        # mesa
        matriz_posicoes = []
        for linha in range(4):
            nova_linha = []
            for coluna in range(len(self.cartas_na_mesa[linha])):
                nova_linha.append(self.cartas_na_mesa[linha][coluna].get_id())
            matriz_posicoes.append(nova_linha)

        interface_image.set_mesa(matriz_posicoes)
        return interface_image