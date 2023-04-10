# Algoritmo que separa componentes conexas
# Victor Medeiros Martins - 401339

import copy



# LEITURA VIA ARQUIVO

for id in range(120):
    with open(f'instancias/{id}.in', 'r') as file:
        while (True):
            if file.read() == '':  # Se arquivo vazio
                exit(1)
            else:
                break
        file.seek(0, 0)  # Volto pra linha 0 do arquivo pra releitura
        linhas = file.read().split('\n')  # Separo em uma lista as linhas
        # Capturo a linha que sempre contém o número de vértices
        str_num_vertices = linhas[2]

        partes = str_num_vertices.split("=")  # Separo essa captura em [n,10]
        # Pego o último da lista e removo todos os espaços (strip)
        num_vertices = int(partes[-1].strip())

        str_lista_adj = linhas[4:]
        if (str_lista_adj[-1] == ''):
            str_lista_adj.pop(-1)
        lista_adj = []

        for elemento in str_lista_adj:
            partes = elemento.split()  # divide o elemento em partes, separadas por espaços
            numeros = []
            for p in partes:  # converte as partes em inteiros
                numeros.append(int(p))
            lista_adj.append(numeros)  # adiciona os inteiros à lista nova


            # LEITURA VIA MÉTODO INPUT()
    """
    linhas = []

    while True:
        try:
            linha = input()
            if not linha:
                break
            linhas.append(linha)
        except EOFError:
            break
    """

    # Capturo a linha que sempre contém o número de vértices
    str_num_vertices = linhas[2]

    partes = str_num_vertices.split("=")  # Separo essa captura em [n,10]
    # Pego o último da lista e removo todos os espaços (strip)
    num_vertices = int(partes[-1].strip())

    str_lista_adj = linhas[4:]
    if (str_lista_adj[-1] == ''):
        str_lista_adj.pop(-1)
    lista_adj = []

    for elemento in str_lista_adj:
        partes = elemento.split()  # divide o elemento em partes, separadas por espaços
        numeros = []
        for p in partes:  # converte as partes em inteiros
            numeros.append(int(p))
        lista_adj.append(numeros)  # adiciona os inteiros à lista nova

    numeros = []
    for i in lista_adj:
        numeros += i

    maximo = num_vertices+1
    minimo = 1

    vertices_faltantes = []

    for i in range(minimo, maximo):
        if i not in numeros:
            vertices_faltantes.append(i)

    lista_adj_aux = copy.deepcopy(lista_adj)
    saida = []
    count = 0

    concatenado = []

    for i in range(len(lista_adj)):
        if lista_adj[i][0] not in concatenado or lista_adj[i][1] not in concatenado:
            concatenado = []
        for j in range(len(lista_adj)):
            if (i != j):
                if (lista_adj[i][0] in lista_adj[j] or lista_adj[i][1] in lista_adj[j]):
                    concatenado = concatenado + lista_adj[i]
                    concatenado = concatenado + lista_adj[j]
                    lista_adj_aux[i] = None
                    lista_adj_aux[j] = None

        concatenado = list(set(concatenado))
        concatenado.sort()
        saida.append(concatenado)

    for i in lista_adj_aux:
        if i is not None:
            saida.append(i)
    for i in vertices_faltantes:
        saida.append([i])

    for i in range(len(saida)):
        saida[i] = tuple(saida[i])

    saida = list(set(saida))
    saida.sort()

    for i in range(len(saida)):
        saida[i] = list(saida[i])

    for i in range(len(saida)):
        for j in range(len(saida)):
            if (i != j):
                if (len(saida[i]) < len(saida[j])):
                    for k in saida[i]:
                        if k in saida[j]:
                            saida[j] += saida[i]
                            saida[j] = list(set(saida[j]))
                            saida[j].sort()
                            saida[i] = []
                            break
                else:
                    for k in saida[j]:
                        if k in saida[i]:
                            saida[i] += saida[j]
                            saida[i] = list(set(saida[i]))
                            saida[i].sort()
                            saida[j] = []
                            break
    saida = [i for i in saida if i]

    print(f"\nArquivo {id}")
    saida.sort()
    for i in range(len(saida)):
        for j in range(len(saida[i])-1):
            print(saida[i][j], end=" ")
        print(saida[i][-1], end="")
        if (i != len(saida)-1):
            print()
    print("\n")
