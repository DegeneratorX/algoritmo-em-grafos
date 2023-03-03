# Grafo

Um grafo é uma estrutura matemática que descreve conexões entre objetos.

Os objetos são chamados de nós ou vértices (vertex), e as conexões são chamadas de arestas (edges).

Normalmente é representado através de um conjunto G(V,E).

## Grafo Direcionado (Dígrafo)

Um grafo direcionado ou orientado é quando possui arestas onde a direção de suas ligações importam para a representação do grafo. Normalmente se utilizam setas para representar o início e o fim.

## Grafo Não Direcionado

Um grafo não direcionado é quando possui mão dupla orientada em todas as arestas, de tal forma que a direção de cada aresta se torna irrelevante para a representação do grafo. Ou seja, uma simples linha conectando dois vértices já seria suficiente para representar uma ligação.

## Outras definições de grafos

### Adjacência (Adjacency)

Definição de dois vértices que são conectados por uma aresta.

### Grau do vértice (Degree of a vertex)

É o número de arestas incidindo sobre um vértice.

### Caminho (Path)

Uma sequência de vértices conectados por arestas.

### Ciclo (Cycle)

Um caminho que começa e termina no mesmo vértice

### Componente conectado

Um conjunto máximo de vértices de tal forma que tem um caminho entre quaisquer dois vértices no conjunto.

# Representação dos grafos

## Matriz de adjacências

Uma matriz quadrada onde as linhas e colunas correspondem aos vértices de um grafo, e as entradas indicam se dois vértices são adjacentes.

## Lista de adjacências

Uma lista de vizinhos para cada vértice.

# Algoritmos de percurso em grafos (Graph traversal algorithms)

## Busca em Largura (Breadth-first search - BFS)

Dado um nó, ele explora todos os vizinhos no nível atual antes de avançar pro póximo nível.

É um algoritmo útil para achar o menor caminho entre dois nós em um grafo sem peso.

- Etapa 1: Escolha um nó inicial e adicione a uma fila.

- Etapa 2: Marque esse nó inicial como visitado.

- Etapa 3: Enquanto a fila não está vazia, faça o seguinte:

    - Etapa 3.1: Pop do nó na frente da fila e chame de "nó atual".
    - Etapa 3.2: Para cada vizinho do nó atual que não foi ainda visitado:
        - 3.2.1: Marque o nó vizinho como visitado
        - 3.2.2: Push nesse nó vizinho
        - 3.2.3: Guarde o parente desse nó vizinho.

- Etapa 4: Repita a etapa 3 até que a fila fique vazia.

- Etapa 5: Se ainda estiver nós vazios, escolha um deles como o novo nó inicial e repita o passo 2 até 4.

Pronto, o algoritmo de busca em largura visituou todos os nós alcançáveis.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MAXN = 100005; // Maximum number of nodes in the graph
vector<int> adj[MAXN]; // The adjacency list of the graph
bool visited[MAXN]; // Array to mark visited nodes

void bfs(int start) {
    queue<int> q; // Queue to store nodes to be visited
    q.push(start); // Add the starting node to the queue
    visited[start] = true; // Mark the starting node as visited

    while (!q.empty()) { // While there are still nodes to visit
        int cur = q.front(); // Get the next node from the queue
        q.pop(); // Remove the node from the queue

        // Process the current node
        cout << "Visiting node " << cur << endl;

        // Add unvisited neighbors of the current node to the queue
        for (int next : adj[cur]) {
            if (!visited[next]) {
                q.push(next);
                visited[next] = true;
            }
        }
    }
}

int main() {
    int n, m; // n is the number of nodes, m is the number of edges
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int u, v; // Edge from u to v
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // For undirected graphs
    }

    int start; // Starting node for BFS
    cin >> start;

    bfs(start); // Call the BFS function

    return 0;
}
```

const int MAXN = 100005: Número máximo de nós do grafo

vector<int> adj[MAXN]: Array de vetores que representa uma lista de adjacências

