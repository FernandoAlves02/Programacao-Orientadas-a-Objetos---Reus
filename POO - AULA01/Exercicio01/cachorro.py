from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, peso_em_quilos, porte):
        super().__init__(nome, peso_em_quilos)
        self.porte = porte

    def emitir_som(self):
        match self.porte:
            case "P":
                print("Au-au-au!")
            case "M":
                print("Au! Au!")
            case "G":
                print("Ruff! Ruff!")

    def anda(self, peso, distancia):
        return ((distancia / 1000) * peso) / 1000

    def andar(self, distancia_em_metros):
        match self.porte:
            case "P":
                self.peso_em_quilos -= self.anda(10, distancia_em_metros)
            case "M":
                self.peso_em_quilos -= ((distancia_em_metros / 1000) * 60) / 1000
            case "G":
                self.peso_em_quilos -= ((distancia_em_metros / 1000) * 100) / 1000

    