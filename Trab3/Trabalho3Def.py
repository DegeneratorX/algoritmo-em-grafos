class Grafo:
    def __init__(self, linhas, direcionado=False, tem_peso=False) -> None:
        self._lista_de_arestas, self._num_vertices = self.__tratamento_dos_dados(linhas, tem_peso)
        for i in self._lista_de_arestas:
            print(i)
        self._lista_adj = self.__para_lista_adj(direcionado, tem_peso)
        self.visited = []

    # Tratamento das strings.
    def __tratamento_dos_dados(self, linhas, tem_peso):
        num_vertices = int(linhas[2].split("=")[1])

        lista_de_arestas = []
        for linha in linhas[4:]:
            linha = linha.strip().split()
            for col in linha:
                linha[0] = int(linha[0])
                linha[1] = int(linha[1])
                if tem_peso:
                    linha[2] = float(linha[2])

            lista_de_arestas.append(linha)
        return lista_de_arestas, num_vertices


    # Conversão para lista de adjacências
    def __para_lista_adj(self, direcionado, tem_peso):
        lista_adj = []
        for _ in range(self._num_vertices):
            lista_adj.append([])
        if tem_peso:
            for vert1, vert2, peso in self._lista_de_arestas:
                lista_adj[vert1-1].append(vert2-1)
                lista_adj[vert1-1].append(peso)
                if not direcionado:
                    lista_adj[vert2-1].append(vert1-1)
                    lista_adj[vert2-1].append(peso)
        else:
            for vert1, vert2 in self._lista_de_arestas:
                lista_adj[vert1-1].append(vert2-1)
                if not direcionado:
                    lista_adj[vert2-1].append(vert1-1)
        return lista_adj
    
    def peso_de(self, vertice_1, vertice_2):
        for vizinho in range(0, len(self._lista_adj[vertice_1]), 2):
            if self._lista_adj[vertice_1][vizinho] == vertice_2:
                return self._lista_adj[vertice_1][vizinho+1]
        return 0
    
    def bfs(self, parent, source, sink):
        visited = [False] * self._num_vertices
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for v in range(0,self._num_vertices):
                if not visited[v] and self._lista_adj[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self._num_vertices
        max_flow = 0

        while self.bfs(parent, source, sink):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self._lista_adj[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self._lista_adj[u][v] -= path_flow
                self._lista_adj[v][u] += path_flow
                v = parent[v]

        return max_flow
    

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
    with open(f'{arquivo}.in', 'r') as file:
        while (True):
            if file.read() == '':  # Se arquivo vazio
                exit(1)
            else:
                break
        file.seek(0, 0)
        linhas = file.readlines()
    return linhas


def main():
    #linhas = leitura_do_arquivo("grafo")
    linhas = leitura_do_input()
    grafo = Grafo(linhas, direcionado=True, tem_peso=True)
    print(grafo.ford_fulkerson(0, 3))
    

if __name__ == '__main__':
    main()