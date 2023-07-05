class HeapMinimo:
    def __init__(self):
        self.heap = []

    def inserir(self, u, peso):
        self.heap.append((u, peso))
        self.sift_up(len(self.heap) - 1)

    def extrair_minimo(self):
        minimo = self.heap[0]
        ultimo = self.heap.pop()
        if self.heap:
            self.heap[0] = ultimo
            self.sift_down(0)
        return minimo

    def consultar_peso(self, v):
        for vertex, peso in self.heap:
            if vertex == v:
                return peso
        return float('inf')

    def atualizar_peso(self, v, novo_peso):
        for i, (vertex, peso) in enumerate(self.heap):
            if vertex == v:
                self.heap[i] = (vertex, novo_peso)
                self.sift_up(i)
                break

    def sift_up(self, i):
        while i > 0:
            pai = (i - 1) // 2
            if self.heap[i][1] < self.heap[pai][1]:
                self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
                i = pai
            else:
                break

    def sift_down(self, i):
        n = len(self.heap)
        while i < n:
            filho_esq = 2 * i + 1
            filho_dir = 2 * i + 2
            menor = i

            if filho_esq < n and self.heap[filho_esq][1] < self.heap[menor][1]:
                menor = filho_esq
            if filho_dir < n and self.heap[filho_dir][1] < self.heap[menor][1]:
                menor = filho_dir

            if menor != i:
                self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
                i = menor
            else:
                break


def dijkstra(adj_list, start):
    n = len(adj_list)
    distancias = [float('inf')] * n
    ancestrais = [-1] * n
    distancias[start] = 0
    heap = HeapMinimo()
    heap.inserir(start, 0)

    while not len(heap.heap) == 0:
        u, peso = heap.extrair_minimo()
        for i in range(0, len(adj_list[u]), 2):
            v = adj_list[u][i]
            peso_u_v = adj_list[u][i + 1]
            if distancias[v] == float('inf'):
                peso_via_u = peso + peso_u_v
                if v not in [vertex for vertex, _ in heap.heap]:
                    heap.inserir(v, peso_via_u)
                    ancestrais[v] = u
                else:
                    if peso_via_u < heap.consultar_peso(v):
                        heap.atualizar_peso(v, peso_via_u)
                        ancestrais[v] = u

    return distancias, ancestrais

# Define the "peso_de" function based on the adjacency list
    # The adjacency list is represented as a list of lists.
    # Each element in the list corresponds to a vertex, and its content is the list of neighbors and respective weights.
    # We can access the weight between vertex u and vertex v as follows:
    # u_index = u - 1 (Apologies for the incomplete response in the previous message. Here's the complete implementation of the "peso_de" function and an example usage of the Dijkstra's algorithm:

def peso_de(adj_list, u, v):
    # Find the index of vertex u in the adjacency list
    u_index = u - 1
    if u_index < 0 or u_index >= len(adj_list):
        return float('inf')

    # Check if vertex v is a neighbor of vertex u
    if v in adj_list[u_index]:
        # Find the index of vertex v in the neighbor list of vertex u
        v_index = adj_list[u_index].index(v)
        # Return the weight associated with the edge (u, v)
        return adj_list[u_index][v_index + 1]

    return float('inf')

# Example usage:
adj_list = [
    [2, 60, 3, 100],
    [1, 30],
    [5, 423, 0, 1234]
]

start_vertex = 0
distances, ancestors = dijkstra(adj_list, start_vertex)
print("Distances:", distances)
print("Ancestors:", ancestors)