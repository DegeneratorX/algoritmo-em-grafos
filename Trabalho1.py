import re
import copy

with open('instancia.in', 'r') as file:
    while(True):
        if file.read() == '': # Se arquivo vazio
            exit(1)
        else:
            break
    file.seek(0,0) # Volto pra linha 0 do arquivo pra releitura
    linhas = file.read().split('\n') # Separo em uma lista as linhas
    str_num_vertices = linhas[2] # Capturo a linha que sempre contém o número de vértices

    partes = str_num_vertices.split("=") # Separo essa captura em [n,10]
    num_vertices = int(partes[-1].strip()) # Pego o último da lista e removo todos os espaços (strip)
    print(num_vertices)

    str_lista_adj = linhas[4:]
    lista_adj = []

    for elemento in str_lista_adj:
        partes = elemento.split() # divide o elemento em partes, separadas por espaços
        numeros = []
        for p in partes: # converte as partes em inteiros
            numeros.append(int(p))
        lista_adj.append(numeros) # adiciona os inteiros à lista nova


numeros = []

for i in lista_adj:
    numeros += i

maximo = max(numeros)
minimo = 1


vertices_faltantes = []

for i in range(minimo, maximo):
    if i not in numeros:
        vertices_faltantes.append(i)

print(lista_adj)

lista_adj_aux = copy.deepcopy(lista_adj)
saida = []

for i in range(len(lista_adj)):
    for j in range(2):
        lista_adj[i][]




"""
        primeiro = i[0]
        ultimo = i[1]
        for j in lista_adj_aux:
            if i[0] == j[0] or i[0] == j[1] or i[1] == j[0] or i[1] == j[1]:
                saida.append(list(set(i+j)).sort())
print(saida)
"""
