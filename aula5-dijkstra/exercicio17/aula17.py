from collections import deque
from copy import deepcopy

class MinHeap:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.heap = []
        self.positions = {}  # Dicionário para armazenar as posições dos elementos

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.positions[self.heap[i][0]] = i
        self.positions[self.heap[j][0]] = j

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx][1] < self.heap[parent_idx][1]:
            self._swap(idx, parent_idx)
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _heapify_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        smallest = idx

        if (left_child_idx < len(self.heap) and
                self.heap[left_child_idx][1] < self.heap[smallest][1]):
            smallest = left_child_idx

        if (right_child_idx < len(self.heap) and
                self.heap[right_child_idx][1] < self.heap[smallest][1]):
            smallest = right_child_idx

        if smallest != idx:
            self._swap(idx, smallest)
            self._heapify_down(smallest)

    def criar(self):
        self.heap = []
        self.positions = {}

    def inserir(self, u, p):
        if u < self.n and len(self.heap) < self.m:
            self.heap.append((u, p))
            self.positions[u] = len(self.heap) - 1
            self._heapify_up(len(self.heap) - 1)

    def consultar_minimo(self):
        return self.heap[0] if self.heap else None

    def remover_minimo(self):
        if not self.heap:
            return None

        min_element = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self.positions[last_element[0]] = 0
            self._heapify_down(0)

        del self.positions[min_element[0]]
        return min_element

    def pertence(self, u):
        return u in self.positions

    def consultar_peso(self, u):
        if u in self.positions:
            return self.heap[self.positions[u]][1]
        return None

    def alterar_peso(self, u, novo_p):
        if u in self.positions:
            idx = self.positions[u]
            old_p = self.heap[idx][1]
            self.heap[idx] = (u, novo_p)
            if novo_p < old_p:
                self._heapify_up(idx)
            elif novo_p > old_p:
                self._heapify_down(idx)

    def esta_vazio(self):
        return len(self.heap) == 0


class Grafo:
    def __init__(self, linhas, direcionado=False, tem_peso=False) -> None:
        self._lista_de_arestas, self._num_vertices = self.__tratamento_dos_dados(linhas, tem_peso)
        self._lista_adj = self.__para_lista_adj(direcionado, tem_peso)

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
            else:
                return 0

    def vizinhos_de(self, vertice):
        pass

    def dijkstra(self, origem):
        distancias = [0]*len(self._lista_adj)
        ancestrais = [0]*len(self._lista_adj)
        print(self._lista_adj)
        for vertice in range(len(self._lista_adj)):
            distancias[vertice] = float('inf')
            ancestrais[vertice] = -1
        heap = MinHeap(10000, 10000)
        heap.inserir(origem, 0)
        while not heap.esta_vazio():
            u, p = heap.remover_minimo()
            distancias[u] = p
            for vertice in range(0, len(self._lista_adj[u]), 2):
                print(f"self._lista_adj[u][vertice] = {self._lista_adj[u][vertice]}")
                print(f"distancias[self._lista_adj[u][vertice]] = {distancias[self._lista_adj[u][vertice]]}")
                if distancias[self._lista_adj[u][vertice]] == float('inf'):
                    peso_via_u = p + self.peso_de(u, self._lista_adj[u][vertice])
                    if not heap.pertence(self._lista_adj[u][vertice]):
                        heap.inserir(self._lista_adj[u][vertice], peso_via_u)
                        ancestrais[self._lista_adj[u][vertice]] = u
                    else:
                        if peso_via_u < heap.consultar_peso(self._lista_adj[u][vertice]):
                            heap.alterar_peso(self._lista_adj[u][vertice], peso_via_u)
                            ancestrais[self._lista_adj[u][vertice]] = u
        return (distancias, ancestrais)


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
    distancias, ancestrais = grafo.dijkstra(0)
    print(f"Distancias: {distancias}")
    print(f"Ancestrais: {ancestrais}")

    

if __name__ == '__main__':
    main()