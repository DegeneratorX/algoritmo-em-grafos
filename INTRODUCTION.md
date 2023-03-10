# Teoria dos Grafos (Graph Theory)

Teoria dos grafos é o estudo dos grafos, que são estruturas matemáticas usadas para modelar relações de pares entre objetos.

Dado G(V,E) (ou G(V,A)), grafos são feitos por nós V (vértices) e conectados por E/A (edges/arestas).

# Direção dos Grafos

Existem dois tipos de grafos principais: os grafos direcionados (directed graphs) e os não direcionados (undirected graphs).

## Grafos não direcionados (Undirected Graphs)

Um grafo não direcionado G(V,E) é um conjunto de vértices e arestas onde as arestas são bidirecionais. Ou seja, para toda aresta (u,v), é idêntica a aresta (v,u).

Normalmente é representado com apenas uma linha conectando dois nós. No caso de grafos não direcionados, todas as arestas são linhas.

## Grafos direcionados (Directed Graphs)

Um grafo direcionado G(V,E) é um conjunto de vértices e arestas onde pelo menos uma aresta é unidimensional. Ou seja, existe uma aresta (u,v) e pode não existir uma aresta (v,u).

# Tipos de Grafos

## Árvores (Trees)

Árvore é um grafo não direcionado onde quaisquer dois vértices (nós) são conectados por exatamente um caminho.

Ou seja, para qualquer vértice que se deseja acessar, só existe um caminho para chegar até ele. Não existe um caminho alternativo.

## Floresta (Forest)

Florestas são grafos não direcionados, onde todos os componentes conectados são árvores.

## Grafos acíclicos direcionados (DIrected Acyclic Graph - DAG)

É um grafo finito direcionado sem ciclos direcionados (crucial em muitos algoritmos).

Ciclo é basicamente a possibilidade de poder voltar para o vértice de partida. Se ele não possui ciclos, então é um grafo acíclico.

Se um grafo não possui ciclos, então dá pra resolver muitos problemas de forma muito rápida. Por exemplo, o algoritmo de menor caminho pode ser resolvido em tempo O(n) graças a isso.

## Grafo Completo (Complete Graph)

É um grafo onde todos os vértices se conectam entre si. Ou seja, todas as possibilidades de pares de vértices são possiveis e existentes no conjunto de arestas.

# Lista de Adjacências