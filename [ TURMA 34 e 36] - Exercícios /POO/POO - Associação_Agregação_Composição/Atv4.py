class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            print(f"- {jogador.nome} ({jogador.posicao})")

class Jogador:
    def __init__(self,nome,posicao):
        self.nome = nome
        self.posicao = posicao


time1 = Time("Sport")
jogador1 = Jogador("CR7", "Atacante")
jogador2 = Jogador("Magrão", "Goleiro")

time1.adicionar_jogador(jogador1)
time1.adicionar_jogador(jogador2)

time1.listar_jogadores()