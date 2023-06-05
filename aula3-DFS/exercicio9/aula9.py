from collections import deque

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

    def tem_circuito(self):
        estado: list = [None] * len(self._lista_adj)
        for vertice in range(len(self._lista_adj)):
            estado[vertice] = "nao_atingido"
        for origem in range(len(self._lista_adj)):
            sequencia = deque()
            if estado[origem] == "nao_atingido":
                self._encontrou_circuito(estado, origem, sequencia)
                break
        aux = sequencia.popleft()
        sequencia.append(aux)
        sequencia.reverse()
        return sequencia

    def _encontrou_circuito(self, estado, origem, sequencia) -> bool:
        estado[origem] = "no_caminho_atual"
        for vizinho in range(len(self._lista_adj[origem])):
            if estado[self._lista_adj[origem][vizinho]] == "no_caminho_atual":
                sequencia.append(self._lista_adj[origem][vizinho])
                return True
            if estado[self._lista_adj[origem][vizinho]] == "nao_atingido":
                if self._encontrou_circuito(estado, self._lista_adj[origem][vizinho], sequencia):
                    sequencia.append(self._lista_adj[origem][vizinho])
                    return True
            if estado[self._lista_adj[origem][vizinho]] == "finalizado":
                pass
        estado[origem] = "finalizado"
        return False

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