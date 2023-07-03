from collections import deque
from copy import deepcopy

class MinHeap:
    def __init__(self, n, m):
        self.n = n  # Número total de elementos identificados por [0..n-1]
        self.m = m  # Número máximo de elementos no heap
        self.heap = []  # Armazena os pares (u, p)
        self.positions = [-1] * n  # Armazena as posições dos elementos no heap
        self.size = 0  # Tamanho atual do heap

    def criar(self):
        self.heap = []
        self.positions = [-1] * self.n
        self.size = 0

    def pertence(self, u):
        return self.positions[u] != -1

    def consultar_peso(self, u):
        if not self.pertence(u):
            raise ValueError("Elemento não está no heap")
        _, p = self.heap[self.positions[u]]
        return p

    def alterar_peso(self, u, novo_p):
        if not self.pertence(u):
            raise ValueError("Elemento não está no heap")
        idx = self.positions[u]
        _, p = self.heap[idx]
        self.heap[idx] = (u, novo_p)
        if novo_p < p:
            self._subir(idx)
        elif novo_p > p:
            self._descer(idx)

    def esta_vazio(self):
        return self.size == 0

    def inserir(self, u, p):
        if self.size == self.m:
            raise ValueError("Heap está cheio")
        if self.pertence(u):
            raise ValueError("Elemento já está no heap")
        self.heap.append((u, p))
        self.positions[u] = self.size
        self._subir(self.size)
        self.size += 1

    def consultar_minimo(self):
        if self.esta_vazio():
            raise ValueError("Heap está vazio")
        return self.heap[0]

    def remover_minimo(self):
        if self.esta_vazio():
            raise ValueError("Heap está vazio")
        minimo = self.heap[0]
        ultimo = self.heap[self.size - 1]
        self.heap[0] = ultimo
        self.positions[ultimo[0]] = 0
        self.positions[minimo[0]] = -1
        self.heap.pop()
        self.size -= 1
        self._descer(0)
        return minimo

    def _subir(self, idx):
        pai = (idx - 1) // 2
        while idx > 0 and self.heap[idx][1] < self.heap[pai][1]:
            self.heap[idx], self.heap[pai] = self.heap[pai], self.heap[idx]
            self.positions[self.heap[idx][0]] = idx
            self.positions[self.heap[pai][0]] = pai
            idx = pai
            pai = (idx - 1) // 2

    def _descer(self, idx):
        esq = 2 * idx + 1
        dir = 2 * idx + 2
        menor = idx
        if esq < self.size and self.heap[esq][1] < self.heap[menor][1]:
            menor = esq
        if dir < self.size and self.heap[dir][1] < self.heap[menor][1]:
            menor = dir
        if menor != idx:
            self.heap[idx], self.heap[menor] = self.heap[menor], self.heap[idx]
            self.positions[self.heap[idx][0]] = idx
            self.positions[self.heap[menor][0]] = menor
            self._descer(menor)


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

    def dijkstra(self, origem):
        distancias = []
        ancestrais = []
        for vertice in range(len(self._lista_adj)):
            distancias[vertice] = float('inf')
            ancestrais[vertice] = -1
        heap = MinHeap()
        heap.inserir(origem, 0)
        while not heap.esta_vazio():
            u, p = heap.remover_minimo()
            distancias[u] = p
            for vertice in range(len(self._lista_adj[u])):
                if distancias[vertice] == float('inf'):
                    peso_via_u = p + self.peso_de(u, vertice)
                    if not heap.pertence(vertice):
                        heap.inserir(vertice, peso_via_u)
                        ancestrais[vertice] = u
                    else:
                        if peso_via_u < heap.consultar_peso(vertice):
                            heap.alterar_peso(vertice, peso_via_u)
                            ancestrais[vertice] = u
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
    grafo.dijkstra(0)
    

if __name__ == '__main__':
    main()