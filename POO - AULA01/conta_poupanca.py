from conta_bancaria import Conta_Bancaria

class Conta_Poupanca(Conta_Bancaria):
    def __init__(self, numero, agencia, titular, taxa_rendimento):
        super().__init__(numero, agencia, titular)
        self.taxa_rendimento = taxa_rendimento

    def ver_extrato(self):
        print