import copy

# LEITURA VIA ARQUIVO

for id in range(120):
    with open(f'exemplos/instancias/{id}.in', 'r') as file:
        lines = file.readlines()

        # Capturo o número de vértices
        num_vertices = int(lines[2].split("=")[-1].strip())

        # Crio uma lista de adjacências a partir das linhas restantes
        lista_adj = [list(map(int, line.split())) for line in lines[4:] if line.strip()]

    numeros = [v for lista in lista_adj for v in lista]

    # Encontro os vértices faltantes
    vertices_faltantes = set(range(1, num_vertices+1)) - set(numeros)
    lista_adj += [[v] for v in vertices_faltantes]

    # Crio uma lista auxiliar de adjacências
    lista_adj_aux = copy.deepcopy(lista_adj)

    # Encontro os componentes conectados
    saida = []
    while lista_adj_aux:
        componente = []
        visitados = set()
        fila = [lista_adj_aux.pop()]

        while fila:
            aresta = fila.pop()
            visitados.add(aresta[0])
            visitados.add(aresta[1])
            componente.extend(aresta)
            for i, aresta2 in enumerate(lista_adj_aux):
                if aresta[0] in aresta2 or aresta[1] in aresta2:
                    fila.append(lista_adj_aux.pop(i))

        componente = list(set(componente))
        componente.sort()
        saida.append(componente)

    # Ordeno a saída
    saida.sort()

    # Imprimo a saída
    for componente in saida:
        print(' '.join(map(str, componente)))