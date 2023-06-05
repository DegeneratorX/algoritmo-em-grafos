# ALUNO: VICTOR MEDEIROS MARTINS
# MATRÍCULA: 401339

from collections import deque

# Criei uma classe de lista encadeada.
class Node:
    def __init__(self, valor, prox=None, ant=None) -> None:
        self.valor = valor
        self.prox = prox
        self.ant = ant

class ListaEncadeada:
    def __init__(self, valor=None) -> None:
        if valor is not None:
            self.head = Node(valor)
            self.tail = Node(valor)
            self.tam = 1
        else:
            self.head = valor
            self.tail = valor
            self.tam = 0

    def append(self, valor):
            new_node = Node(valor)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.ant = self.tail
                self.tail.prox = new_node
                self.tail = new_node

    def pop(self):
        if self.tail is None:
            return None

        valor = self.tail.valor

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.ant
            self.tail.prox = None

        return valor

    def join(self, lista_para_unir):
        if lista_para_unir.head is not None:
            if self.head is None:
                self.head = lista_para_unir.head
                self.tail = lista_para_unir.tail
            else:
                lista_para_unir.head.ant = self.tail
                self.tail.prox = lista_para_unir.head
                self.tail = lista_para_unir.tail

        lista_para_unir.head = None
        lista_para_unir.tail = None


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
            if not tem_peso:
                linha.pop(2)
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


    # Pseudocódigo (sala de aula) para python
    def computar_arvore_geradora_minima(self):
        lista_ordenada_por_peso = deque([[item[0] - 1, item[1] - 1, item[2]] for item in sorted(self._lista_de_arestas, key=lambda x: x[2])])
        a = deque()
        representantes = [0]*len(self._lista_adj)
        componentes = []
        componentes = [ListaEncadeada() for _ in range(len(self._lista_adj))]

        for vertice in range(len(self._lista_adj)):
            componentes[vertice].head = Node(vertice)
            componentes[vertice].tail = componentes[vertice].head
            componentes[vertice].tam = 1
            representantes[vertice] = vertice
        while len(a) != len(self._lista_adj)-1:
            u, v, w = lista_ordenada_por_peso.popleft()
            if representantes[u] != representantes[v]:
                a.append([u,v,w])
                x = representantes[u]
                y = representantes[v]
                if componentes[x].tam < componentes[y].tam:
                    x, y = y, x
                z = componentes[y].head
                componentes[x].tail.prox = z
                componentes[x].tail = componentes[y].tail
                componentes[x].tam = componentes[x].tam + componentes[y].tam
                while z is not None:
                    representantes[z.valor] = x
                    z = z.prox
        soma = self._soma_dos_pesos_da_agm(a)
        return a, soma

    def _soma_dos_pesos_da_agm(self, agm):
        return sum(i[2] for i in agm)


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

# Leio os 120 arquivos mandados pelo professor Pablo em trabalho_2_entradas_e_saidas_para_teste.zip
# Depreciado por hora, o programa pegou de primiera, vamos ver se vai.
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

linhas = leitura_do_input()
#linhas = leitura_do_arquivo(4)
grafo = Grafo(linhas, False, True)
agm, peso_total = grafo.computar_arvore_geradora_minima()
print(f"{peso_total:.3f}")
