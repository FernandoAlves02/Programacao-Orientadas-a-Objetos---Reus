from animal import Animal

class Gato(Animal):
    def __init__(self, nome, peso_em_quilos):
        super().__init__(nome, peso_em_quilos)

    def emitir_som(self):
        print("Miau Miau... humanos...")