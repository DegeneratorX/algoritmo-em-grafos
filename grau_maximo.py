from queue import Queue

class Grafo:
    def __init__(self, lista_adj) -> None:
        self.lista_adj = lista_adj
        num_vertices = len(lista_adj)

    def _numero_de_vertices(self, lista_adj):
        num = 0
        for i in lista_adj:
            num = num + 1

    # Busca o vértice de maior grau. Convertido do pseudocódigo do Pablo pra python.
    def vertice_de_grau_maximo(self):
        grau_maximo = -1
        vertice_grau_maximo = None

        for vertice in range(len(self.lista_adj)):
            grau = 0
            for aresta in self.lista_adj[vertice]:
                grau += 1
            if grau > grau_maximo:
                grau_maximo = grau
                vertice_grau_maximo = vertice

        return vertice_grau_maximo
    
    

    def distance_graph_simple(self, o):
        n = len(self.lista_adj)
        d = [float('inf')] * n
        d[o] = 0
        queue = [o]
        while queue:
            u = queue.pop(0)
            for v in self.lista_adj[u]:
                if d[v] == float('inf'):
                    d[v] = d[u] + 1
                    queue.append(v)
        return d


lista_adj = [[1,4],
             [0,5],
             [3,5,6],
             [2,6],
             [0],
             [1,2,6],
             [2,3,5],
             [0,1,2,3,4,5,6,8],
             [0,1,2,3,4,5,6,7,9],
             [0,1,2,3,4,5,6,7,8],]

grafo = Grafo(lista_adj)
#print(grafo.vertice_de_grau_maximo())
print(grafo.distance_graph_simple(2))