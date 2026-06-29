from cachorro import Cachorro
from gato import Gato

def mostra_lista(lista_de_animais):
    for animal in lista_de_animais:
        animal.mostrar_dados()

def main():
    # Pedi pro meu mano Gemini criar os objetos pra mim, tava sem criatividade, mas não pedi para validar meu código
    # Criar um array de animais que vai imprimir independente se for cachorro ou gato as informações <- Prof Réus comentou

    animais = [
        Cachorro("Bob", 5.0, "P"),
        Cachorro("Rex", 15.0, "M"),
        Cachorro("Thor", 35.0, "G"),
        Cachorro("Mel", 6.0, "P"),
        Cachorro("Freud", 22.0, "M"),
        Gato("Mingau", 4.0),
        Gato("Garfield", 8.5),
        Gato("Luna", 3.2),
        Gato("Tom", 5.0),
        Gato("Simba", 4.8)
    ]

    mostra_lista(animais)

if __name__ == "__main__":
    main()