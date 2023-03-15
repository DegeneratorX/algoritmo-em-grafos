# Teoria dos Grafos (Graph Theory)

Teoria dos grafos é o estudo dos grafos, que são estruturas matemáticas usadas para modelar relações de pares entre objetos.

Dado G(V,E) (ou G(V,A)), grafos são feitos por nós V (vértices) e conectados por E/A (edges/arestas).

Alguns conceitos básicos de grafos antes de começar a listar os principais tipos:

- Grafo Conexo: Todos os vértices são acessíveis a partir de quaisquer outros vértices por meio de um caminho possível.
- Grafo Não-Conexo: Existe pelo menos um vértice onde não existe caminho para acessá-lo. Ou seja, existe um vértice isolado.
- Ciclo: É um caminho fechado onde o primeiro e o último vértice são iguais. Pode ser um subgrafo de um grafo maior.
- Grafo Cíclico: Consiste em apenas um ciclo de caminho fechado.
- Grafo Acíclico: Não possui ciclos.

# Direção dos Grafos

Existem duas orientações de grafos principais: os grafos direcionados (directed graphs) e os não direcionados (undirected graphs).

## Grafos não direcionados (Undirected Graphs)

- Definição: Um grafo não-direcionado é um par ordenado $(V,E)$ tal que:
    - $V$ é um conjunto finito, e
    - $E \subseteq \{\{u,v\} \subseteq V : u \neq v\}$ (a primeira chave representa o conjunto de pares não ordenados de um vértice)

Um grafo não direcionado G(V,E) é um conjunto de vértices e arestas onde as arestas são "bidirecionais" (na verdade não é direcional de forma alguma, mas é como se fosse). Ou seja, para toda aresta {u,v}, é idêntica (=) a aresta {v,u} trivialmente, pois é um conjunto de pares, e em conjuntos a ordem não importa.

Normalmente é representado com apenas uma linha conectando dois nós. No caso de grafos não direcionados, todas as arestas são linhas.

![](2023-03-15-15-01-42.png)

No caso do primeiro exemplo, o grafo desenhado é o grafo $G_1 = (V,E)$ tal que:

$V = \{A,B,C,D\}$, onde V é o conjunto de vértices.

$E = \{\{A,B\},\{A,C\}\}$, onde E é o conjunto de arestas (edges).

## Grafos direcionados (Directed Graphs)

Um grafo direcionado G(V,E) é um conjunto de vértices e arestas onde pelo menos uma aresta é unidimensional. Ou seja, existe uma aresta (u,v) e pode não existir uma aresta (v,u) ou não ser idêntica.

![](2023-03-15-15-08-51.png)

# Tipos de Grafos

## Árvores (Trees)

Árvore é um grafo não direcionado aciclico conexo.

![](2023-03-13-13-09-11.png)

## Floresta (Forest)

Florestas são grafos onde todos os componentes conectados são árvores.

![](2023-03-13-16-43-52.png)

## Grafos acíclicos direcionados (Directed Acyclic Graph - DAG)

É um grafo finito direcionado sem 'ciclos direcionados' (crucial em muitos algoritmos).

![](2023-03-13-16-45-00.png)

Se um grafo não possui ciclos, então dá pra resolver muitos problemas de forma muito rápida. Por exemplo, o algoritmo de menor caminho pode ser resolvido em tempo O(n) graças a isso.

## Grafo Completo (Complete Graph)

É um grafo onde todos os vértices se conectam entre si. Ou seja, todas as possibilidades de pares de vértices são possiveis e existentes no conjunto de arestas.

![](2023-03-13-16-47-08.png)

# Representação dos Grafos

Existem duas formas de representar os grafos para trabalhar com algoritmos: Lista de Adjacências e Matriz de Adjacências.

## Lista de Adjacências (Adjacency List)

Nós atribuimos uma estrutura de dados (1D array) para cada vértice (nó) no grafo, e cada array guarda elementos que mostra a conexão (aresta) com outro vértice e o peso dessa conexão se o grafo tiver peso.

![](2023-03-14-09-38-28.png)

O uso de memória depende do número de arestas, o que pode salvar muita memória se a matriz de adjacências tiver bastante zeros. Ou seja, grafos dispersos é eficiente, mas grafos densos é ineficiente.

Buscar a aresta entre dois nós é O(k), onde k é o número de nós vizinhos.

É rápido adicionar ou deletar um nó e é rápido iterar sobre todas as arestas, pois você pode acessar qualquer nó vizinho diretamente.

## Matriz de Adjacências (Adjacency Matrix)

Se constrói uma matriz M com tamanho VxV onde M[i][j] representa o peso da aresta ao ir do nó i para o nó j.

Por exemplo:

![](2023-03-15-15-22-49.png)

Observe os pesos que ocupam cada setor da matriz. Por ser um grafo direcional com pelo menos uma orientação única (ou seja, tem pelo menos um aresta de ida, mas não de volta), não existe simetria. Porém, observe esse caso:

![](2023-03-15-15-25-04.png)

Aqui o grafo não possui peso, logo automaticamente se preenche os pesos da matriz com 1 ou 0, para indicar pelo menos a existência de uma aresta que conecta dois vértices.

E por se tratar de um grafo não-direcional, temos como resultado uma matriz com representação simétrica.

E por fim, se o grafo for direcional, mas bidirecional para toda aresta, ela também pode ter representação simétrica, desde que os pesos sejam iguais na ida e volta.

O uso de espaço é eficiente em grafos mais densos, mas requer memória O(V²) no pior caso.

Verificar o peso de uma aresta é O(1), e iterar sobre todas as arestas tem um custo de O(E²).

