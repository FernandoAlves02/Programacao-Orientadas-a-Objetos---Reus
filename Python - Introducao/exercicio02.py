from colorama import Fore, init, Back, Style

init(autoreset=True)

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

pares = 0
impares = 0

print("Dado N números, dizer quantos desses números são pares, e quantos, ímpares:")
while True:
    valor = ler_dados()            

    if ( valor == 0 ):
        break

    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print(Fore.GREEN + Style.BRIGHT + f"Total de valores pares: {Fore.BLUE}{pares}")
print(Fore.GREEN + Style.BRIGHT + f"Total de valores impares: {Fore.RED}{impares}")
