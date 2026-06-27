from conta_poupanca import Conta_Poupanca
from conta_corrente import Conta_Corrente

def main():
    cc1 = Conta_Corrente(1234, 321, "João da Silva", 500)

    cc1.ver_extrato()
    print("-"*50)
    print("Adicionando valores")
    print("-"*50)
    cc1.depositar(2500)
    print("-"*50)
    print("Sacar valores")
    print("-"*50)
    if(not cc1.sacar(2600)):
        print("Pobre maldito!!!")
    print("-"*50)
    cc1.ver_extrato()

if __name__ == "__main__":
    main()