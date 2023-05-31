import leitura

class GrafoDirecionado:
    def __init__(self, lista_adj:list) -> None:
        self._lista_adj = lista_adj

    def tem_circuito(self)->bool:
        estado:list = [None]* len(self._lista_adj)
        for vertice in range(len(self._lista_adj)):
            estado[vertice] = "nao_atingido"
        for origem in range(len(self._lista_adj)):
            if estado[origem] == "nao_atingido":
                if self._encontrou_circuito(estado, origem):
                    return True
        return False


    def _encontrou_circuito(self, estado, origem) -> bool:
        estado[origem] = "no_caminho_atual"
        for vizinho in self._lista_adj[origem]:
            if estado[vizinho] == "no_caminho_atual":
                return True
            if estado[vizinho] == "nao_atingido":
                if self._encontrou_circuito(estado, vizinho):
                    return True
            if estado[vizinho] == "finalizado":
                pass
        estado[origem] = "finalizado"
        return False


def main():
    lista_de_arestas, num_vertices = leitura.tratamento_dos_dados(leitura.leitura_do_arquivo("grafo.in"))
    grafo = GrafoDirecionado(leitura.para_lista_adj(lista_de_arestas, num_vertices))
    if grafo.tem_circuito():
        print("O grafo tem circuito")
    else:
        print("O grafo não tem circuito")


if __name__ == "__main__":
    main()