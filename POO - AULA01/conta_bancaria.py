from abc import ABC, abstractmethod

class Conta_Bancaria(ABC):
    def __init__(self, numero, agencia, titular):
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self.saldo = 0

    @abstractmethod
    def sacar(self, valor):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        return True
    
    @abstractmethod
    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def ver_extrato(self):
        pass