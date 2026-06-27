from cachorro import Cachorro
from gato import Gato

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

    print("--- TESTANDO OS ANIMAIS ---")
    for anim in animais:
        if isinstance(anim, Cachorro): # <- mano gemini me mostrou esse isinstance pra verificar se o objeto é tal classe
            print(f"\nClasse: Cachorro | Nome: {anim.nome} | Porte: {anim.porte}")
        else:
            print(f"\nClasse: Gato | Nome: {anim.nome}")

        print(f"  Peso Inicial: {anim.peso_em_quilos:.3f} kg")

        print("  Som: ", end="")
        anim.emitir_som()

        anim.comer(500)
        print(f"  Peso após comer 500g: {anim.peso_em_quilos:.3f} kg")

        anim.andar(2000)
        print(f"  Peso após andar 2000m: {anim.peso_em_quilos:.3f} kg")

        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()