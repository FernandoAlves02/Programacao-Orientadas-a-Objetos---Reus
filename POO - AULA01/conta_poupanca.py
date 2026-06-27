from conta_bancaria import Conta_Bancaria

class Conta_Poupanca(Conta_Bancaria):
    def __init__(self, numero, agencia, titular, taxa_rendimento):
        super().__init__(numero, agencia, titular)
        self.taxa_rendimento = taxa_rendimento

    def ver_extrato(self):
        print(f"EXTRATO CONTA POUPANÇA")
        print(f"NÚMERO: {self.numero}")
        print(f"AGÊNCIA: {self.agencia}")
        print(f"TITULAR: {self.titular}")
        print(f"SALDO: {self.saldo}")
    def depositar(self, valor):
        return super().depositar(valor)
    def sacar(self, valor):
        return super().sacar(valor)
