from queue import Queue
from collections import deque


class Grafo:
    def __init__(self, __lista_adj) -> None:
        self.__lista_adj = __lista_adj
        self.num_vertices = len(__lista_adj)


    def _numero_de_vertices(self):
        num = 0
        for i in self.__lista_adj:
            num += 1


    def set_vizinho(self, vertice, vizinho):
        self.__lista_adj[vertice].append(vizinho)


    def get_vizinhos(self, vertice):
        return self.__lista_adj[vertice]

    # Busca o vértice de maior grau. Convertido do pseudocódigo do Pablo pra python.
    def vertice_de_grau_maximo(self):
        grau_maximo = -1
        vertice_grau_maximo = None

        for vertice in range(len(self.__lista_adj)):
            grau = 0
            for aresta in self.__lista_adj[vertice]:
                grau += 1
            if grau > grau_maximo:
                grau_maximo = grau
                vertice_grau_maximo = vertice

        return vertice_grau_maximo
    

    def distance_graph_simple(self, o):
        n = len(self.__lista_adj)
        d = [float('inf')] * n
        d[o] = 0
        queue = [o]
        while queue:
            u = queue.pop(0)
            for v in self.__lista_adj[u]:
                if d[v] == float('inf'):
                    d[v] = d[u] + 1
                    queue.append(v)
        return d


    def is_star_graph(self):
        vertices_centrais = [] # Crio uma lista para guardar potenciais "centro(s)" do grafo
        
        for i in range(self.num_vertices): # Itero sobre os vértices do grafo
            # Se o vértice tem o número de vizinhos igual ao de vértices-1 
            # (pois não pode ser vizinho dele mesmo), então é um vértice central.
            if len(self.__lista_adj[i]) == self.num_vertices-1: 
                vertices_centrais.append(i)
        
        # Depois verifico nas iterações se ele veio vazio, e se sim, imediatamente 
        # sabe-se que não é uma estrela, pois não tem um ponto central que 
        # conecta a todos os outros vértices.
        if len(vertices_centrais) == 0: 
            return False
        
        # De novo, itero sobre a lista de adjacências e os vértices
        for i in range(self.num_vertices):
            # Se o índice não é um nó central, já dá pra verificar as outras condições
            # Se o grau do vértice não-central for maior que 1 (mais de 1 vizinho),
            # de cara não tem como ser uma estrela. Ou se o vizinho dele não for
            # o próprio centro, não tem como também ser estrela, pois estaria
            # conectado a outro vértice aleatório.
            if i not in vertices_centrais and (len(self.__lista_adj[i]) != 1 or self.__lista_adj[i][0] not in vertices_centrais):
                return False # Então retorna falso.
            
        # Se todas as condições de barrar um grafo não estrela forem superadas,
        # então não resta dúvidas que é um grafo estrela.
        return True


    def bfs(self, origem):
        # Inicializa as distâncias do vetor de distância com "infinito" de 
        # acordo com a quantidade de vértices possíveis. Isso é feito, pois
        # inicialmente não sabemos as distâncias.
        distances = [float("inf")] * len(self.__lista_adj)
        distances[origem] = 0 # Defino a distância para a própria origem como zero.

        # Inicio uma fila de prioridade com origem zero. A fila serve para 
        # percorrer o grafo.
        queue = [origem]

        while queue: # Enquanto ela não estiver vazia

            # O vértice atual recebe o primeiro da fila. Esse vértice é usado
            # pra percorrer o grafo.
            curr_node = queue.pop(0)

            # Agora eu vou atrás dos vizinhos desse vértice que estou apontando
            # agora.
            for neighbor in self.__lista_adj[curr_node]:

                # Se o vizinho não foi visitado ainda, a distância é atualizada
                # da seguinte forma: 
                if distances[neighbor] == float("inf"):
                    distances[neighbor] = distances[curr_node] + 1
                    queue.append(neighbor)
            # O algoritmo se torna mais fácil de entender quando desenhado no
            # papel.
        return distances


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


lista_adj_estrela = [
    [1,2,3,4],
    [0],
    [0],
    [0],
    [0],
]

grafo = Grafo(lista_adj)
grafo_estrela = Grafo(lista_adj_estrela)
#print(grafo.vertice_de_grau_maximo())
print(grafo.distance_graph_simple(2))
print(grafo_estrela.is_star_graph())
print(grafo_estrela.bfs(1))