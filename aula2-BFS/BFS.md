# Introdução

Existem vários algoritmos que percorrem de forma otimizada um grafo. Um deles é a **busca em largura** (Breadth First Search - BFS). Mas antes é necessário definir algumas coisas.


# Breadth First Search - BFS (Busca em Largura)

A busca em largura percorre o grafo de forma paralela, partindo de um vértice de origem, checando os vizinhos, e checando os vizinhos dos vizinhos até não sobrar mais vértices. O algoritmo usa uma fila para armazenar vértices que serão os próximos a serem analisados na sequẽncia.

Existe algumas formas para implementar o algoritmo. A mais clássica é a implementação básica.

### Algoritmo BFS: Default

```python
    def bfs(self, origem):
        # Crio uma lista com a mesma quantidade de vértices que diz, pelo index, se
        # o vértice foi ou não visitado. O index dessa lista de visitados é o mesmo
        # da lista de adjacências para vértices.
        visitados = ["Não"] * len(self.__lista_adj)

        # Inicio uma fila de prioridade com origem inserida. A fila serve para 
        # percorrer o grafo. Ficará mais claro abaixo.
        queue = [origem]

        while queue: # Enquanto a fila não estiver vazia

            # O vértice atual recebe o primeiro da fila. Esse vértice é usado
            # pra percorrer o grafo. 
            # Basicament "vértice atual" é um ponteiro que aponta pro primeiro da fila.
            vertice_atual = queue.pop(0)

            # Agora eu vou atrás dos vizinhos desse vértice atual que estou apontando
            # agora.
            for vizinho in self.__lista_adj[vertice_atual]:

                # Procuro os possíveis vizinhos do vértice atual na lista de adj.
                if visitados[vizinho] == "Não": # Se o vértice não foi visitado
                    visitados[vizinho] = "Sim" # Agora passa a ser marcado como sendo.
                    queue.append(vizinho) # Adiciono o vizinho na fila para depois ver os vizinhos do vizinho.
        return visitados
```

Posso também atribuir a cores, sendo branco os vértices não visitados, cinza os vértices da fila de prioridade e preto os vértices visitados. Essa é uma abordagem que o Cormen utiliza.

Caso eu deseje saber as distâncias dos vértices a partir da origem, faço uma pequena modificiação:

### Algoritmo BFS: modificação para calcular distâncias a partir da origem

Esse algoritmo retorna uma lista contendo as distâncias de cada vértice a partir do ponto de origem usando BFS. É apenas uma pequena modificação simples do algoritmo padrão.

```python
    def bfs(self, origem):
        # Da mesma forma, olho os visitados e agora ao invés de "Sim" e "Não,
        # atribuo as distâncias pra cada vértice.

        # No começo suponho que nenhum vértice seja alcançável...
        distancias_visitados = [float("inf")] * len(self.__lista_adj)

        # ...mas que a distância do vértice de origem pra ele mesmo é zero.
        distancias_visitados[origem] = 0

        queue = [origem]

        while queue:
            vertice_atual = queue.pop(0)
            for vizinho in self.__lista_adj[vertice_atual]:

                # Vejo se a distância é infinita. 
                if distancias_visitados[vizinho] == float("inf"):

                    # Se for, não faz sentido ser, pois existe um vizinho, ou seja, uma distância.
                    # E basta eu fazer uma soma da distância do vértice que estou agora em relação à origem com mais um vizinho (+1)
                    distancias_visitados[vizinho] = distancias_visitados[vertice_atual] + 1
                    queue.append(vizinho) # E assim adiciono o vizinho na fila para depois ver os vizinhos do vizinho.
        return distancia_visitados
```

### Algoritmo BFS: achar componentes conexas

É possível sim que o BFS não percorra todos os vértices, 
