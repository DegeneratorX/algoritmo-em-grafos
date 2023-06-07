from collections import deque
from copy import deepcopy

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


    def computar_agm_removendo_ciclos(self):
        lista_de_ciclos = set()
        estado = [None] * len(self._lista_adj)
        for vertice in range(len(self._lista_adj)):
            estado[vertice] = "nao_atingido"
        for origem in range(len(self._lista_adj)):
            if estado[origem] == "nao_atingido":
                caminho_atual = []
                ciclo = self._encontrou_ciclo(estado, origem, caminho_atual)
                if ciclo:
                    lista_de_ciclos.add(ciclo)

        lista_de_ciclos = list(lista_de_ciclos)
        lista_de_arestas_maximas = set()
        while lista_de_ciclos:
            ciclo = lista_de_ciclos.pop()
            peso_maximo = 0
            for vertice in range(len(ciclo)):
                if self.peso_de(ciclo[vertice]) > peso_maximo:
                    peso_maximo = self.peso_de(ciclo[vertice])
                    vertice_peso_maximo = ciclo[vertice]
            lista_de_arestas_maximas.add((vertice_peso_maximo, peso_maximo))
        agm = [list()]*len(self._lista_adj)
        for i in range(len(self._lista_adj)):
            for j in range(len(self._lista_adj[i])):
                for k in range(len(lista_de_arestas_maximas)):
                    if (self._lista_adj[i][j], self._lista_adj[i][j+1]) != lista_de_arestas_maximas[k]:
                        agm[i].append(lista_de_arestas_maximas[k][0])
                        agm[i].append(lista_de_arestas_maximas[k][1])
        return agm

        

    def _encontrou_ciclo(self, estado, origem, caminho_atual):
        estado[origem] = "no_caminho_atual"
        caminho_atual.append(origem)
        for vizinho in self._lista_adj[origem]:
            if estado[vizinho] == "no_caminho_atual":
                ciclo_inicio = caminho_atual.index(vizinho)
                return caminho_atual[ciclo_inicio:]
            if estado[vizinho] == "nao_atingido":
                ciclo = self._encontrou_ciclo(estado, vizinho, caminho_atual)
                if ciclo:
                    return ciclo
            if estado[vizinho] == "finalizado":
                pass
        estado[origem] = "finalizado"
        caminho_atual.pop()
        return []
    
    def peso_de(self, vertice_1, vertice_2):
        for vizinho in range(0, len(self._lista_adj[vertice_1]), 2):
            if self._lista_adj[vertice_1][vizinho] == vertice_2:
                return self._lista_adj[vertice_1][vizinho+1]
            else:
                return 0



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
    grafo = Grafo(linhas, direcionado=True, tem_peso=False)
    print(f"Sequência: {[x for x in grafo.tem_circuito()]}")

if __name__ == '__main__':
    main()