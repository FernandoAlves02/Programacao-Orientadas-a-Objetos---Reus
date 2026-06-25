from colorama import Fore, Style, init

init(autoreset=True)

def valor_estoque(valor, estoque):
    return valor * estoque

def verificar_estoque(estoque): 
    if estoque <= 10: 
        return Fore.RED + Style.BRIGHT + "Estoque baixo"
    elif estoque <= 50: 
        return Fore.YELLOW + Style.BRIGHT + "Atenção"
    elif estoque > 50: 
        return Fore.GREEN + Style.BRIGHT + "Estoque abastecido"
    
def mostrar_produtos(produto):
    print(f"{produto['ID']:<8}", end="")
    print(f"{produto['Nome']:<43}", end="")
    print(f"R$ {produto['Valor_Unitario']:<15.2f}", end="")
    print(f"{produto['Estoque']:<13}", end="")
    print(f"R$ {valor_estoque(produto['Valor_Unitario'], produto['Estoque']):<15.2f}", end="")
    print(f"{verificar_estoque(produto['Estoque']):<23}")
    print(Fore.GREEN + Style.BRIGHT + "-" *125)

def mostrar_header():
    print(Fore.GREEN + Style.BRIGHT + "=" *125)
    print(Fore.GREEN + Style.BRIGHT + f"{'LISTA DE PRODUTOS':^125}")
    print(Fore.GREEN + Style.BRIGHT + "=" *125)
    print(Fore.GREEN + Style.BRIGHT + f"{'ID':<5} | {'NOME':<40} | {'VALOR UNITÁRIO':<15} | {'ESTOQUE':<10} | {'TOTAL':<15} | {'STATUS':<20}")
    print(Fore.GREEN + Style.BRIGHT + "-" *125)

def mostrar_menu(acao):
    
    produto_encontrado = False

    if acao == 1:
        mostrar_header()
        for produto in produtos:
            mostrar_produtos(produto)
    if acao == 2:
        while True:
            try:           
                id_produto = int(input("Digite o ID do produto: "))
                break
            except ValueError:
                print ("Valor inválido! Por favor, digite um número inteiro.")
            except KeyboardInterrupt:
                print ("\nOperação cancelada pelo usuário.")
                exit (1)
        mostrar_header()
        for produto in produtos:
            if produto['ID'] == id_produto:
                mostrar_produtos(produto)
                produto_encontrado = True
        if not produto_encontrado:
            print(Fore.RED + Style.BRIGHT + "Produto não encontrado.")
 
    
produtos = [
    {
        "ID" : 1,
        "Nome" : "Notebook",
        "Valor_Unitario" : 3500.00,
        "Estoque" : 10
    },
    {
        "ID" : 2,
        "Nome" : "Smartphone",
        "Valor_Unitario" : 1500.00,
        "Estoque" : 20
    },
    {
        "ID" : 3,
        "Nome" : "Tablet",
        "Valor_Unitario" : 2000.00,
        "Estoque" : 15
    },
    {
        "ID" : 4,
        "Nome" : "Monitor",
        "Valor_Unitario" : 800.00,
        "Estoque" : 8
    },
    {
        "ID" : 5,
        "Nome" : "Teclado",
        "Valor_Unitario" : 200.00,
        "Estoque" : 25
    },
    {
        "ID" : 6,
        "Nome" : "Mouse",
        "Valor_Unitario" : 150.00,
        "Estoque" : 51
    }
]

acao = int(input("Digite 1 para exibir os produtos e verificar o estoque, ou 2 para um produto específico: "))

mostrar_menu(acao)