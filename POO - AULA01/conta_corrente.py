from conta_bancaria import Conta_Bancaria

class Conta_Corrente(Conta_Bancaria):
    def __init__(self, numero, agencia, titular, limite):
        super().__init__(numero, agencia, titular)
        self.limite = limite

    def depositar(self,valor):
        return super().depositar(valor)
    
    def sacar(self, valor):
        if(valor > self.saldo + self.limite):
            return False
        self.saldo -= valor
        return True
    
    def ver_extrato(self):
        print(f"EXTRATO CONTA CORRENTE")
        print(f"NÚMERO: {self.numero}")
        print(f"AGÊNCIA: {self.agencia}")
        print(f"TITULAR: {self.titular}")
        print(f"SALDO: {self.saldo}")
        print(f"LIMITE: {self.limite}")