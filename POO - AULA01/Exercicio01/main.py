from cachorro import Cachorro
from gato import Gato

def main():
    # Pedi pro meu mano Gemini criar os objetos pra mim, tava sem criatividade, mas não pedi para validar meu código
    # Criar um array de animais que vai imprimir independente se for cachorro ou gato as informações
    # Instanciando 5 cachorros com diferentes portes e pesos iniciais
    cachorros = [
        Cachorro("Bob", 5.0, "P"),
        Cachorro("Rex", 15.0, "M"),
        Cachorro("Thor", 35.0, "G"),
        Cachorro("Mel", 6.0, "P"),
        Cachorro("Freud", 22.0, "M")
    ]

    # Instanciando 5 gatos com diferentes pesos iniciais
    gatos = [
        Gato("Mingau", 4.0),
        Gato("Garfield", 8.5),
        Gato("Luna", 3.2),
        Gato("Tom", 5.0),
        Gato("Simba", 4.8)
    ]

    # Arrumar abaixo, conforme linha 6
    print("--- TESTANDO OS CACHORROS ---")
    for cao in cachorros:
        if Cachorro:
            print(f"\nAnimal: {cao.nome} | Porte: {cao.porte}")
        else:
            print(f"\nAnimal: {cao.nome})
        print(f"  Peso Inicial: {cao.peso_em_quilos:.3f} kg")
        
        # Emitindo som
        print("  Som: ", end="")
        cao.emitir_som()
        
        # Testando comer (ex: 500g)
        cao.comer(500)
        print(f"  Peso após comer 500g: {cao.peso_em_quilos:.3f} kg")
        
        # Testando andar (ex: 2000 metros)
        cao.andar(2000)
        print(f"  Peso após andar 2000m: {cao.peso_em_quilos:.3f} kg")

    print("\n" + "="*40 + "\n")

    print("--- TESTANDO OS GATOS ---")
    for gatinho in gatos:
        print(f"\nAnimal: {gatinho.nome}")
        print(f"  Peso Inicial: {gatinho.peso_em_quilos:.3f} kg")
        
        # Emitindo som
        print("  Som: ", end="")
        gatinho.emitir_som()
        
        # Testando comer (ex: 300g)
        gatinho.comer(300)
        print(f"  Peso após comer 300g: {gatinho.peso_em_quilos:.3f} kg")
        
        # Testando andar (ex: 1500 metros)
        gatinho.andar(1500)
        print(f"  Peso após andar 1500m: {gatinho.peso_em_quilos:.3f} kg")

if __name__ == "__main__":
    main()