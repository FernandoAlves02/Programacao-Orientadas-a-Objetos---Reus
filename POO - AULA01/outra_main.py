from funcionario import Funcionario

f1 = Funcionario("Pafúncio da Sulva Sauro", 10, 137)

f2 = Funcionario("Aracnodolphio dos Santos", 30, 200)

f3 = Funcionario("Josephina Escatamatio Pinto", 22, 250)

empresa = []

empresa.append(f1)
empresa.append(f2)
empresa.append(f3)

f2.valor_hora = 40

for func in empresa:
    func.mostrar_holerite()