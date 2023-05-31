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

def leitura_do_arquivo(arquivo):
    with open(f'{arquivo}', 'r') as file:
        while (True):
            if file.read() == '':  # Se arquivo vazio
                exit(1)
            else:
                break
        file.seek(0, 0)
        linhas = file.readlines()
    return linhas

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

def para_lista_adj(lista_de_arestas, num_vertices, direcionado=True):
    lista_adj = []
    for _ in range(num_vertices):
        lista_adj.append(set())
    for vert1, vert2 in lista_de_arestas:
            lista_adj[vert1-1].add(vert2-1)
            if not direcionado:
                lista_adj[vert2-1].add(vert1-1)

    return lista_adj

