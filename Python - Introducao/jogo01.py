def escreve_jogada(jogada):
    match jogada:
        case 1:
            return("Pedra")
        case 2:
            return("Papel")
        case 3:
            return("Tesoura")

def analisa_jogada(jogada1, jogada2):
    if jogada1 == jogada2:
        return "E"
    elif (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
        return "P1"
    else:
        return "P2"

def ler_jogada():
    while True:
        try:
            jogada = int(input("Digite sua jogada (1 - Pedra, 2 - Papel, 3 - Tesoura): "))
            if jogada in [1, 2, 3]:
                return jogada
            else:
                print("Jogada inválida. Por favor, digite 1, 2 ou 3.")
        except ValueError:
            print("Jogada inválida. Por favor, digite 1, 2 ou 3.")

def game_loop():
    while True:
        try:
            escolha = input("Deseja continuar jogando (S/N)? ")
            if escolha in ["S", "N"]:
                return escolha
            else:
                print("Jogada inválida. Por favor, digite 'S' ou 'N'.")
        except ValueError:
            print("Jogada inválida. Por favor, digite 'S' ou 'N'.")

def escreve_resultado(resultado):
    match resultado:
        case "E":
            print("Empate!")
        case "P1":
            print("Jogador 1 venceu!")
        case "P2":
            print("Jogador 2 venceu!")

def main():
    while True:
        print("Jogador 1, faça sua jogada:")
        jogada1 = ler_jogada()
        print("Jogador 2, faça sua jogada:")
        jogada2 = ler_jogada()

        resultado = analisa_jogada(jogada1, jogada2)

        print("Jogada do Jogador 1:", escreve_jogada(jogada1))
        print("Jogada do Jogador 2:", escreve_jogada(jogada2))
        escreve_resultado(resultado)

        if game_loop() == "N": break

if __name__ == "__main__":
    main()