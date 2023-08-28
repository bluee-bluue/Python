from Models.pessoa import Pessoa
from Models.suite import Suite


class Reserva:
    def __init__(self, diariasReservadas):
        self.diariasReservadas = diariasReservadas

    def cadastrarHospedes(self, hospedes: [Pessoa]):
        if self.suite.capacidade >= len(hospedes):
            self.hospedes = hospedes
        else:
            raise Exception("A capacidade da suite é menor que o número de hospedes")

    def cadastrarSuite(self, suite: Suite):
        self.suite = suite

    def obterQuantidadeHospedes(self):
        return len(self.hospedes)

    def calcularValorDiaria(self):
        valor = 0

        if self.diariasReservadas >= 10:
            valorOriginal = self.diariasReservadas * self.suite.valorDiaria
            valor = valorOriginal - (valorOriginal * 10 / 100)
        else:
            valor = self.diariasReservadas * self.suite.valorDiaria

        return valor
