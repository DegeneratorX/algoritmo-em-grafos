# Algoritmo que separa componentes conexas
# Victor Medeiros Martins - 401339

# Reorganizei o código, dessa vez com funções

# LEITURA VIA ARQUIVO
def leitura_do_arquivo(arquivo):
    with open(f'exemplos/instancias/{arquivo}.in', 'r') as file:
        while (True):
            if file.read() == '':  # Se arquivo vazio
                exit(1)
            else:
                break
        file.seek(0, 0)
        linhas = file.readlines()
    return linhas


# LEITURA DO INPUT
def leitura_do_input():
    linhas = []

    while True:
        try:
            linha = input()
            if not linha:
                break
            linhas.append(linha)
        except EOFError:
            break
    return linhas


# TRATA OS DADOS RECEBIDOS
def tratamento_dos_dados(linhas):
    num_vertices = int(linhas[2].split("=")[1])

    lista_de_arestas = []
    for linha in linhas[4:]:
        linha = linha.strip().split()
        for col in linha:
            linha[0] = int(linha[0])
            linha[1] = int(linha[1])
        lista_de_arestas.append(linha)

    return lista_de_arestas, num_vertices


# ALGORITMO DE BUSCA EM LARGURA
def bfs(origem, lista_adj, visitados, componente):

    fila = [origem]

    while fila:
        vertice_atual = fila.pop(0)
        componente.add(vertice_atual)
        for vizinho in lista_adj[vertice_atual]:
            if vizinho not in visitados:
                # Repito as duas primeiras linhas desse método quando busco
                # por vizinhos
                visitados.add(vizinho)
                fila.append(vizinho)


# ALGORITMO DE ACHAR AS COMPONENTES CONEXAS DE UM GRAFO RECEBIDO.
def componentes_conexas(lista_de_arestas, num_vertices):

    # Crio uma lista de adjacências vazia e preencho ela com conjuntos,
    # pois em um conjunto os elementos não se repetem.
    # Lembrando que a lista de adjacências vai de 0 a n-1.
    lista_adj = []
    for i in range(num_vertices):
        lista_adj.append(set())

    # Preencho a lista de adjacências com os vértices (índices da lista) e
    # suas respectivas conexões. Como é não direcionado, faço ida e volta.
    # O -1 é justamente pq estamos convertendo a lista de arestas do arquivo
    # que trabalha de 1 a n, pra lista de adjacências que trabalha de 0 a n-1.
    for vert1, vert2 in lista_de_arestas:
        lista_adj[vert1-1].add(vert2-1)
        lista_adj[vert2-1].add(vert1-1)


    # Algoritmo de achar componentes conexas.
    visitados = set()
    componentes = []

    # Esse "for", por mais que pareça inútil, garante que TODOS os vértices 
    # foram percorridos, mesmo que tenha um vértice único isolado, pois um 
    # vértice isolado é uma componente.
    for i in range(num_vertices):
        if i not in visitados:
            componente = set()
            visitados.add(i)
            bfs(i, lista_adj, visitados, componente)
            componentes.append(sorted(componente))

    return componentes

# Leio os 120 arquivos mandados pelo professor Pablo em exemplo.zip
"""
for i in range(120):
    print()
    print(f"Arquivo {i}:")
    lista_de_arestas, num_vertices = tratamento_dos_dados(leitura_do_arquivo(i))
    componentes = componentes_conexas(lista_de_arestas, num_vertices)

    for componente in componentes:
        linha = ""
        for vertice_atual in componente:
            linha = linha + str(vertice_atual + 1) + " "
        print(linha.strip())
    print()
"""

# Leio apenas input
lista_de_arestas, num_vertices = tratamento_dos_dados(leitura_do_input())
componentes = componentes_conexas(lista_de_arestas, num_vertices)

for componente in componentes:
    linha = ""
    for vertice_atual in componente:
        linha = linha + str(vertice_atual + 1) + " "
    print(linha.strip())