from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, peso_em_quilos):
        self.nome = nome
        self.peso_em_quilos = peso_em_quilos

    @abstractmethod
    def emitir_som():
        pass

    def comer(self, quantidade_em_gramas):
        self.peso_em_quilos += quantidade_em_gramas / 1000

    def andar(self, distancia_em_metros):
        self.peso_em_quilos -= ((distancia_em_metros / 1000) * 50) / 1000
