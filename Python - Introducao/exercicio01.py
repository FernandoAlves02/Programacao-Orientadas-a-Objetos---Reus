def ler_dados():
    while True:
        try:           
            valor = int(input("Digite um número inteiro: ")) 
            return valor
        except ValueError:
            print ("Valor inválido! Por favor, digite um número inteiro.")
        except KeyboardInterrupt:
            print ("\nOperação cancelada pelo usuário.")
            exit (1)  
soma = 0
total = 0

print("Dado 5 números, calcular a média:")
for i in range (1,6):
    soma += ler_dados()
    total += 1
media = soma / total
print(f"A média dos 5 valores inseridos é: {media:.2f}") 