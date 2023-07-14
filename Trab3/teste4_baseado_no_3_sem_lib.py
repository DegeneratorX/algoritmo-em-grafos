from collections import deque

class Grafo:
    def __init__(self, linhas, tem_peso=False) -> None:
        self._lista_de_arestas, self._num_vertices = self.__tratamento_dos_dados(linhas, tem_peso)
        self._matriz_adj= self.__para_matriz_adj()

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
        return lista_de_arestas, num_vertices+1

    def __para_matriz_adj(self):
        matriz_adj = [[0 for _ in range(self._num_vertices)] for _ in range(self._num_vertices)]
        for i, j, w in self._lista_de_arestas:
            matriz_adj[i][j] = w

        return matriz_adj

    def fluxo_maximo(self, origem, destino):
        n = len(self._matriz_adj)
        fluxos = [[0] * n for _ in range(n)]

        # Lembrar que a capacidade residual de u a v é Cap[u][v] - Fluxos[u][v]
        while True:
            caminho = self.bfs(fluxos, origem, destino)
            if not caminho:
                break
                
            # Acha a capacidade mínima no caminho
            fluxo = min(self._matriz_adj[u][v] - fluxos[u][v] for u, v in caminho)
            
            # Aumenta o fluxo ao longo do caminho
            for u, v in caminho:
                fluxos[u][v] += fluxo
                fluxos[v][u] -= fluxo
                
        return sum(fluxos[origem][i] for i in range(n))

    # BFS pra achar o menor caminho aumentante
    def bfs(self, fluxos, origem, destino):
        fila = deque([origem])
        caminhos = {origem: []}
        while fila:
            vertice_atual = fila.pop()
            for vizinho in range(len(self._matriz_adj)):
                if (self._matriz_adj[vertice_atual][vizinho] - fluxos[vertice_atual][vizinho] > 0) and vizinho not in caminhos:
                    caminhos[vizinho] = caminhos[vertice_atual] + [(vertice_atual, vizinho)]
                    if vizinho == destino:
                        return caminhos[vizinho]
                    fila.append(vizinho)
        return None


def leitura_do_arquivo(arquivo):
    with open(f'Trab3/solucoes/{arquivo}.in', 'r') as file:
        while (True):
            if file.read() == '':  # Se arquivo vazio
                exit(1)
            else:
                break
        file.seek(0, 0)
        linhas = file.readlines()
    return linhas

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

def retira_ponto_zero_do_float(numero):
    if int(numero) == numero:
        return int(numero)
    else:
        return numero

"""
# edges [from, to, capacity]
edges = [
    [1, 3, 78.25],
    [2, 3, 76.75],
    [3, 5, 63.5],
    [3, 2, 51.25],
    [3, 1, 62.875],
    [4, 3, 13.625],
    [4, 2, 1.625],
    [4, 1, 14.125],
    [5, 2, 10.875],
    [5, 1, 40.0],
]
"""

def main():
    #for arq in range(13):
    linhas = leitura_do_input()
        #print()
        #print(f"Arquivo {arq}:")
        #linhas = leitura_do_arquivo(arq)
    grafo = Grafo(linhas, tem_peso=True)

    # Calcula todos os fluxos máximos pedidos
    for vertice in range(2, grafo._num_vertices):
        print(f"{vertice} {retira_ponto_zero_do_float(grafo.fluxo_maximo(1, vertice))}")

if __name__ == '__main__':
    main()