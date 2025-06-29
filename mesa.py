from baralho import Baralho
from carta import Carta
from player import Player
from placar import Placar
from interface_image import InterfaceImage

class Mesa:
    def __init__(self, player_interface):
        self.__local_player = Player()
        self.__placar = Placar()
        self.__baralho = Baralho()
        self.__cartas_na_mesa = [[], [], [], []]  # 4 linhas, cada uma com uma lista de cartas
        self.__n_cartas_jogador_remoto = 0
        self.__player_interface = player_interface
        self.__match_status = 0

#### REQUISITOS FUNCIONAIS ####

    # iniciar_partida
    def iniciar_partida(self, players, local_player_id):
        self.__baralho.criar_baralho()
        self.criar_mesa()
        id = players[0][1]
        name = players[0][0]
        order = players[0][2]
        self.__local_player.initialize(id, name)
        self.montar_mao_jogador_local()

        if order == "1":
            self.__match_status = 1
            self.__player_interface.notificar("Você é o primeiro a jogar")
        else:
            self.__match_status = 4
            self.__player_interface.notificar("Aguardando o primeiro jogador jogar")
        
    # selecionar_carta
    def selecionar_carta(self, posicao):
        if self.__match_status == 1 or self.__match_status == 2 or self.__match_status == 3:
            if self.__local_player.verificar_selecao(posicao):
                self.__local_player.remover_carta_selecionada(posicao)
                self.__player_interface.remover_selecao_carta(posicao)
            else:
                self.__local_player.adicionar_carta_selecionada(posicao)
                self.__player_interface.adicionar_selecao_carta(posicao)

    # jogar_cartas
    def jogar_cartas(self, linha, coluna):
        if self.__match_status == 1:
            selecionadas = self.__local_player.get_cartas_selecionadas()

            if len(selecionadas) > 0:
                iguais = self.verificar_cartas_selecionadas_iguais(selecionadas)
                if iguais:
                    mao = self.__local_player.get_mao()
                    todas = self.verificar_especie_selecionada(mao, selecionadas)
                    if todas:
                        self.__local_player.remover_cartas_selecionadas_da_mao()
                        especie = selecionadas[0].get_especie()
                        sanduiche = self.verificar_sanduiche(especie, linha, coluna)
                        self.add_cartas_na_mesa(selecionadas, linha, coluna)

                        if len(sanduiche) > 0:
                            self.__local_player.adicionar_cartas_na_mao(sanduiche)
                            especies_na_fileira = 0
                            while especies_na_fileira <= 1:
                                especies_na_fileira = self.contar_especies_na_fileira(linha)
                                carta = self.__baralho.pegar_cartas(1)
                                self.add_cartas_na_mesa(carta, linha, coluna)
                        
                        self.__match_status = 2
                        game_state = self.get_status()
                        self.__player_interface.atualizar_interface(game_state)
                    else:
                        self.__player_interface.notificar("Você deve selecionar todas as cartas de uma espécie para jogar")      
                else:
                    self.__player_interface.notificar("As cartas selecionadas devem ser iguais")
            else:
                self.__player_interface.notificar("Você deve selecionar cartas para jogar")

    # formar_bando
    def formar_bando(self):
        if self.__match_status == 2 or self.__match_status == 3:
            selecionadas = self.__local_player.get_cartas_selecionadas()

            if len(selecionadas) > 0:
                pontos = self.verificar_formacao_bando(selecionadas)

                if pontos > 0:
                    especie = selecionadas[0].get_especie()
                    self.__placar.atualizar_placar_local(pontos, especie)
                    self.__local_player.remover_cartas_selecionadas_da_mao()

                    game_state = self.get_status()
                    self.__player_interface.atualizar_interface(game_state)

                    vitoria = self.verificar_vitoria()
                    if vitoria:
                        self.__player_interface.notificar("Você venceu a partida!")
                        self.__match_status = 5

                        move_to_send = self.get_move(inicio=False)
                        self.__player_interface.send_move(move_to_send)
                    else:
                        self.__match_status = 3
                        move_to_send = self.get_move(inicio=False)
                        self.__player_interface.send_move(move_to_send)
                else:
                    self.__player_interface.notificar("Não é possível formar um bando")
            else:
                self.__player_interface.notificar("Você deve selecionar cartas para formar bando")
        else:
            self.__player_interface.notificar("Você precisa jogar cartas na mesa antes de formar bando")

    # finalizar_turno
    def finalizar_turno(self):
        if self.__match_status == 2 or self.__match_status == 3:
            game_state = self.get_status()
            self.__player_interface.atualizar_interface(game_state)
            self.__match_status = 4
            move_to_send = self.get_move(inicio=False)
            self.__player_interface.send_move(move_to_send)

    # receber_jogada
    def receber_jogada(self, jogada):
        if jogada["inicio_partida"] == "1":
            self.__baralho.set_baralho(jogada["baralho_inicial"])
            self.montar_mao_jogador_local()
        else:
            if len(self.__local_player.get_mao()) == 0:
                cartas = self.__baralho.pegar_cartas(8)
                self.__local_player.adicionar_cartas_na_mao(cartas)
            self.atualizar_baralho(jogada["num_cartas_baralho"])
            self.__n_cartas_jogador_remoto = int(jogada["n_cartas_jogador"])
            self.__match_status = 1

        mesa_strings = [jogada["primeira_linha_mesa"], jogada["segunda_linha_mesa"], jogada["terceira_linha_mesa"], jogada["quarta_linha_mesa"]]
        self.montar_mesa_recebida(mesa_strings)

        game_state = self.get_status()
        self.__player_interface.atualizar_interface(game_state)

        if jogada["match_status"] == "finished":
            self.__player_interface.notificar("A partida terminou! Derrota.")
            self.__match_status = 5
            self.__player_interface.encerrar_aplicacao()

#### MÉTODOS DE COMUNICAÇÃO ####

    def get_move(self, inicio):
        move_to_send = {}

        if inicio: # se for o início da partida
            move_to_send["inicio_partida"] = "1"
            if self.__match_status == 1:
                move_to_send["match_status"] = "progress"
            else:
                move_to_send["match_status"] = "next"
            
            move_to_send["baralho_inicial"] = self.__baralho.get_cartas_iniciais()
            self.__baralho.pegar_cartas(8)
        
        else: # se for o andamento do jogo
            move_to_send["inicio_partida"] = "0"

            # cartas no baralho
            move_to_send["num_cartas_baralho"] = str(self.__baralho.get_num_cartas())

            # placar
            move_to_send["pontos_local"] = str(self.__placar.get_pontos_local())

            # bandos
            bandos = self.__placar.get_bandos_local()
            if len(bandos) == 0:
                bandos_string = "sem_bandos"
            else:
                for i in range(len(bandos)):
                    especie = bandos[i][0]
                    tamanho = bandos[i][1]
                    if i == 0:
                        bandos_string = str(especie) + "/" + str(tamanho)
                    else:
                        bandos_string += "," + str(especie) + "/" + str(tamanho)
            move_to_send["bandos"] = bandos_string

            # numero de cartas na mão do jogador local
            n_cartas_jogador_local = len(self.__local_player.get_mao())
            move_to_send["n_cartas_jogador"] = str(n_cartas_jogador_local)

            if self.__match_status == 5:
                move_to_send["match_status"] = "finished"
            else:
                move_to_send["match_status"] = "next"
        
        # mesa - envio sendo inicio ou nao
        mesas_strings = self.obtem_mesa_to_string()
        move_to_send["primeira_linha_mesa"] = str(mesas_strings[0])
        move_to_send["segunda_linha_mesa"] = str(mesas_strings[1])
        move_to_send["terceira_linha_mesa"] = str(mesas_strings[2])
        move_to_send["quarta_linha_mesa"] = str(mesas_strings[3])

        return move_to_send

    def get_status(self):
        interface_image = InterfaceImage()

        # baralho
        interface_image.set_baralho(self.__baralho.get_num_cartas())

        # numero de cartas na mão do jogador remoto
        interface_image.set_n_cartas_jogador_remoto(self.__n_cartas_jogador_remoto)

        # cartas na mão do jogador local
        lista_mao =[]
        mao =self.__local_player.get_mao()
        for carta in mao:
            lista_mao.append(carta.get_especie())
        interface_image.set_cartas_na_mao_local(lista_mao)

        # placar
        interface_image.set_placar_local(self.__placar.get_pontos_local())
        interface_image.set_placar_remoto(self.__placar.get_pontos_remoto())

        #bandos
        interface_image.set_bandos_local(self.__placar.get_bandos_local())
        interface_image.set_bandos_remoto(self.__placar.get_bandos_remoto())

        # mesa
        matriz_posicoes = []
        for linha in range(4):
            nova_linha = []
            for coluna in range(len(self.__cartas_na_mesa[linha])):
                nova_linha.append(self.__cartas_na_mesa[linha][coluna].get_especie())
            matriz_posicoes.append(nova_linha)

        interface_image.set_mesa(matriz_posicoes)

        return interface_image

#### MÉTODOS DE CONVERSÃO DA MESA ####

    def obtem_mesa_to_string(self):
        mesa_strings = []
        
        for linha in self.__cartas_na_mesa:
            if len(linha) == 0:
                mesa_strings.append("")
            else:
                cartas_ids = []
                for carta in linha:
                    cartas_ids.append(str(carta.get_especie()))
                mesa_strings.append("/".join(cartas_ids))
        
        return mesa_strings

    def montar_mesa_recebida(self, mesa_strings):
        matriz_mesa = []
        dicionario_especies = self.__baralho.get_dicionario_especies()

        for linha in mesa_strings:
            linha_mesa = []
            
            if linha == "":
                matriz_mesa.append(linha_mesa)
                continue
                
            nova_linha = linha.split('/')
            for carta in nova_linha:
                especie = int(carta)
                indice_especie = especie - 1
                nova_carta = Carta(especie, dicionario_especies[indice_especie][0], dicionario_especies[indice_especie][1])
                linha_mesa.append(nova_carta)
            matriz_mesa.append(linha_mesa)

        self.__cartas_na_mesa = matriz_mesa

#### MÉTODOS DE VALIDAÇÃO ####

    def verificar_cartas_selecionadas_iguais(self, selecionadas):
        especie = selecionadas[0].get_especie()
        cont = 0

        for carta in selecionadas:
            if carta.get_especie() == especie:
                cont += 1

        return cont == len(selecionadas)
    
    def verificar_especie_selecionada(self, mao, selecionadas):
        especie = selecionadas[0].get_especie()
        cont = 0

        for carta in mao:
            if carta.get_especie() == especie:
                cont += 1
        
        return cont == len(selecionadas)

    def verificar_formacao_bando(self, cartas):
        primeira_carta = cartas[0]

        # Verifica se todas as cartas têm a mesma espécie
        for i in range(1, len(cartas)):
            if cartas[i].get_especie() != primeira_carta.get_especie():
                return 0
        
        # Verifica se o número de cartas corresponde ao tamanho do bando
        if len(cartas) == primeira_carta.get_bando_pequeno():
            return 1
        elif len(cartas) == primeira_carta.get_bando_grande():
            return 2
        else:
            return 0

    def verificar_vitoria(self):
        pontos_local = self.__placar.get_pontos_local()
        return pontos_local >= 5

#### MÉTODOS DA MANIPULAÇÃO DA MESA ####

    def criar_mesa(self):
        for linha in range(4):
            especies_usadas_linha = []  # Para controlar espécies já usadas na linha atual
            
            for _ in range(3):
                baralho = self.__baralho.get_cartas()
                for i in range(len(baralho)):
                    carta_atual = baralho[i]
                    especie_atual = carta_atual.get_especie()
                    if especie_atual not in especies_usadas_linha:
                        self.__cartas_na_mesa[linha].append(carta_atual)
                        especies_usadas_linha.append(especie_atual)
                        self.__baralho.remover_carta(i)
                        break

    def verificar_sanduiche(self, especie, linha, coluna):
        retorno = []

        if coluna == 0: # cartas adicionadas à esquerda
            for carta in range(len(self.__cartas_na_mesa[linha])):
                if self.__cartas_na_mesa[linha][carta].get_especie() == especie:
                    for carta_sanduiche in range(carta):
                        carta_removida = self.__cartas_na_mesa[linha].pop(0)
                        retorno.append(carta_removida)
                    return retorno
        else: # cartas adicionadas à direita
            for carta in range(len(self.__cartas_na_mesa[linha])-1,-1,-1):
                if self.__cartas_na_mesa[linha][carta].get_especie() == especie:
                    for carta_sanduiche in range(carta):
                        carta_removida = self.__cartas_na_mesa[linha].pop()
                        retorno.append(carta_removida)
                    return retorno
        return retorno

    def add_cartas_na_mesa(self, cartas, linha, coluna):
        if coluna == 0:
            for carta in cartas:
                self.__cartas_na_mesa[linha].insert(0, carta)
        else:
            for carta in cartas:
                self.__cartas_na_mesa[linha].append(carta)
    
    def contar_especies_na_fileira(self, linha):
        especies = []
        for carta in self.__cartas_na_mesa[linha]:
            if carta.get_especie() not in especies:
                especies.append(carta.get_especie())
        return len(especies)

 #### MÉTODOS AUXILIARES ####

    def atualizar_baralho(self, quantidade):
        cartas_retiradas = self.__baralho.get_num_cartas() - int(quantidade)
        self.__baralho.pegar_cartas(cartas_retiradas)
    
    def montar_mao_jogador_local(self):
        cartas = self.__baralho.pegar_cartas(8)
        self.__local_player.adicionar_cartas_na_mao(cartas)

    def set_match_status(self, status):
        self.__match_status = status

    def inicializar_local_player(self, identifier, name):
        self.__local_player.initialize(identifier, name)