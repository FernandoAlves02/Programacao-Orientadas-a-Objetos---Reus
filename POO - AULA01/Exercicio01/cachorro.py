from animal import Animal
from colorama import init, Fore, Style

init(autoreset=True)

class Cachorro(Animal):
    def __init__(self, nome, peso_em_quilos, porte):
        super().__init__(nome, peso_em_quilos)
        self.porte = porte

    def emitir_som(self):
        match self.porte:
            case "P":
                return f"{Fore.BLUE+Style.BRIGHT}Au-au-au!"
            case "M":
                return f"{Fore.BLUE+Style.BRIGHT}Au! Au!"
            case "G":
                return f"{Fore.BLUE+Style.BRIGHT}Ruff! Ruff!"

    def andar(self, distancia_em_metros):
        match self.porte:
            case "P":
                taxa = 0.01
            case "M":
                taxa = 0.06
            case "G":
                taxa = 0.1
            case _:
                #fallback caso o usuário informe algo errado
                taxa = 0.05

        self.peso_em_quilos -= (distancia_em_metros / 1000.0) * taxa

    def mostrar_dados(self):
        print(f"Nome do cachorro: {self.nome}")
        print(f"Peso: {self.peso_em_quilos}")
        print(f"O cachorro faz {self.emitir_som()}")
        print("-"*50)