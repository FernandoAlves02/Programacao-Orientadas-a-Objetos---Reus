while True:
    try:
        valor1 = int(input("Digite o primeiro valor: "))
        break
    except ValueError:
        print("Valor inválido! Por favor, digite um número inteiro.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        exit(1)

while True:
    try:
        valor2 = int(input("Digite o segundo valor: "))
        break
    except ValueError:
        print("Valor inválido! Por favor, digite um número inteiro.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        exit(1)

while True:
    print("Selecione uma opção: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    try:
        opcao = int(input("Digite a opção desejada: "))
        break
    except ValueError:
        print("Opção inválida! Por favor, digite um número inteiro.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        exit(1)

resultado = None
match opcao:
    case 1:
        resultado = valor1 + valor2
    case 2:
        resultado = valor1 - valor2
    case 3:
        resultado = valor1 * valor2
    case 4:
        try:
            resultado = valor1 / valor2
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida!")
    case _:
        print("Opção inválida!")
if resultado is not None:
    print("Resultado: ", resultado)
