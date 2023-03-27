# Caminhos

Existem vários algoritmos que percorrem de forma otimizada um grafo. Mas antes é necessário definir algumas coisas.

Dado um grafo $G = (V,E)$, não direcionado, e dados $u,v \in V$, temos:

- **Passeio de $u$ a $v$**: é uma sequẽncia de vértices $x_0, x_1,...,x_k$ tal que:
    - $k \ge 0$
    - $x_0 = u$ e $x_k = v$
    - Para todo $i \in \left\{1,...,k\right\}$, é válido que $\left\{x_{i-1}, x_i\right\} \in E$
- **Caminho de $u$ a $v$**: é um passeio de $u$ a $v$ sem repetição de vértices.
    - Ou seja, um passeio $x_0,...,x_k$ tal que para todo $i,j \in \left\{0,...,k\right\}$, se $i < j$, então $x_i \neq x_j$
- **Distância de $u$ a $v$**: é o mínimo entre os números de arestas dos caminhos de $u$ a $v$.
    - Ou seja, $\delta (u,v) = k_i$, se existe um caminho de $u$ a $v$ com $k$ arestas, e não existe caminho de $u$ a $v$ ccom menos de $k$ arestas. É infinito, se não existe caminho de $u$ a $v$.

## Distância em Grafos Simples

**Exemplo**

Dado um grafo não direcionado $G = (V,E)$ e dado um vértice de origem $o \in V$, calcular a distância $\delta (o,v)$ para todo $v \in V$. Armazenar num vetor $d[0,...,n-1]$ tal que $d[v] = \delta (o,v)$.

