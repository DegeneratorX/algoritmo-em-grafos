import sys

# Leitura da entrada
#input_data = sys.stdin.readlines()
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

def tratamento_dos_dados(linhas, tem_peso):
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

from collections import deque

def ford_fulkerson(graph, source, sink):
  """
  Calcula o fluxo máximo de um vértice de menor índice para cada um dos outros vértices do grafo direcionado recebido como entrada.

  Args:
    graph: Um grafo direcionado.
    source: O vértice de origem.
    sink: O vértice de destino.

  Returns:
    A lista de fluxos máximos de um vértice de menor índice para cada um dos outros vértices do grafo.
  """

  # Cria uma matriz de fluxos.
  flows = [[0 for _ in range(len(graph))] for _ in range(len(graph))]

  # Inicializa o fluxo para zero.
  for i in range(len(graph)):
    for j in range(len(graph)):
      flows[i][j] = 0

  # Encontra um caminho augmentante.
  while True:
    path = augmenting_path(graph, source, sink)
    if not path:
      break

    # Adiciona o fluxo máximo ao caminho augmentante.
    min_capacity = float("inf")
    for i in range(len(path) - 1):
      min_capacity = min(min_capacity, graph[path[i]][path[i + 1]])
    for i in range(len(path) - 1):
      flows[path[i]][path[i + 1]] += min_capacity
      flows[path[i + 1]][path[i]] -= min_capacity

  # Retorna a lista de fluxos máximos.
  return flows

def augmenting_path(graph, source, sink):
  """
  Encontra um caminho augmentante de um vértice de menor índice para outro vértice de um grafo direcionado.

  Args:
    graph: Um grafo direcionado.
    source: O vértice de origem.
    sink: O vértice de destino.

  Returns:
    Uma lista com os vértices do caminho augmentante, ou None se não encontrar um caminho.
  """

  # Inicializa uma fila com o vértice de origem.
  queue = [source]

  # Marca todos os vértices como visitados.
  visited = set()
  visited.add(source)

  # Enquanto a fila não estiver vazia:
  while queue:
    v = queue.pop(0)

    # Para cada vizinho de v:
    if isinstance(v, int):
      for neighbor in graph[v]:
        # Se o vizinho não foi visitado e tem capacidade remanescente:
        queue.append(neighbor)
        visited.add(neighbor)

        # Se o vizinho for o vértice de destino:
        if neighbor == sink:
          # Retorna o caminho augmentante.
          return list(visited)

  # Se a fila ficar vazia, não há caminho augmentante.
  return None

input_data = leitura_do_input()
graph, _ = tratamento_dos_dados(input_data, True)
flows, augmenting_path = ford_fulkerson(graph, 0, len(graph) - 1)
  # Imprime a saída.
for i in range(1, len(graph)):
    print(i, flows[0][i])

