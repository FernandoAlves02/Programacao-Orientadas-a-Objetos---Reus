class Funcionario:
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        self.nome = nome
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_bruto(self):
        return self.valor_hora * self.horas_trabalhadas
        
    def calcular_inss(self):
        bruto = self.calcular_salario_bruto()
        if bruto <= 2500:
            return bruto * 0.09
        return bruto * 0.125
        
    def calcular_salario_liquido(self):
        return self.calcular_salario_bruto() - self.calcular_inss()
        
    def mostrar_holerite(self):
        print(f"NOME DO FUNCIONARIO: {self.nome}")
        print(f"VALOR HORA: {self.valor_hora}")
        print(f"HORAS TRABALHADAS DO MÊS: {self.horas_trabalhadas}")
        print(f"=" * 30)
        print(f"SALÁRIO BRUTO: {self.calcular_salario_bruto()}")
        print(f"DESCONTO DE INSS: {self.calcular_inss()}")
        print(f"SALÁRIO LÍQUIDO: {self.calcular_salario_liquido()}")