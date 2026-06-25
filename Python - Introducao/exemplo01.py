numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite um valor: "))

resposta = numero1 + numero2
print("Resposta ", resposta)

numero1, numero2 = numero2, numero1

print("Numero 1: ", numero1)
print("Numero 2: ", numero2)