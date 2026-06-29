from animal import Animal
from colorama import init, Fore, Style

init(autoreset=True)

class Gato(Animal):
    def __init__(self, nome, peso_em_quilos):
        super().__init__(nome, peso_em_quilos)

    def emitir_som(self):
        return f"{Fore.YELLOW+Style.BRIGHT} Miau Miau... humanos..."
    
    def mostrar_dados(self):
        print(f"Nome do gato: {self.nome}")
        print(f"Peso: {self.peso_em_quilos}")
        print(f"O gato faz {self.emitir_som()}")
        print("-"*50)