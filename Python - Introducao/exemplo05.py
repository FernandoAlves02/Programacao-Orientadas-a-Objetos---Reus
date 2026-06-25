# Exemplo de lista

lista = [10, 20, 30, 40, 50]
lista.append(60)
# print(lista)
lista[3] = 90
# print(lista)


# Exemplo de tupla
tupla = (10, 20, 30, 40, 50)
# print(tupla)


# Exemplo de dicionario
dicionario = {
    "RA" : "2345678",
    "Nome" : "Gabriel Pensador",
    "Idade" : 20,
    "Curso" : "TDS"
}

# print(dicionario["Nome"])

print("Imprime a lista")
for item in lista:
    print(item)

print("Imprime a tupla")
for item in tupla:
    print(item)

print("Imprime o dicionário versão 1")
for chave in dicionario:
    print(chave, ":", dicionario[chave])

print("Imprime o dicionário versão 2")
for chave, valor in dicionario.items():
    print(chave, ":", valor)