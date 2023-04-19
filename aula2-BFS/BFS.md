# Breadth First Search - BFS (Busca em Largura)

Existem vários algoritmos que percorrem de forma otimizada um grafo. Um deles é a **busca em largura** (Breadth First Search - BFS). 

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

É possível sim que o BFS não percorra todos os vértices, principalmente quando envolve grafos desconexos (propriedade mostrada na INTRODUCTION.md).

Ou seja, o BFS, em uma chamada só, percorre apenas uma componente conexa a partir de uma origem caso não exista pelo menos uma ponte que ligue uma componente conexa a outra.

Portanto, precisamos testar todos os vértices para que sejam, em algum momento, a origem no BFS, para que não falte analisar todas as componentes conexas, e assim percorremos o grafo por inteiro, mesmo ele despedaçado. Então precisamos fazer um outro loop para cada vértice na lista de ajdacências.

```python
# Algoritmo de achar componentes conexas.
def componentes_conexas(self):
    visitados = set()
    lista_de_componentes = []

    # Esse "for", por mais que pareça inútil, garante que TODOS os vértices 
    # sejam percorridos, mesmo que tenha um vértice único isolado, pois um 
    # vértice isolado é uma componente.
    for i in range(len(self.__lista_adj)): # Pra cada vértice
        if i not in visitados: # Se o vértice não foi visitado
            componente = set() # Começo a escrever o que tem dentro da componente conexa partindo do zero.
            bfs(i, visitados, componente) # Percorro a componente inteira. Componente e visitados são passados por referência em python (listas e sets).
            lista_de_componentes.append(sorted(componente)) # a componente agora está completa.

    return lista_de_componentes # Retorno todas as componentes do grafo.

def bfs(origem, visitados, componente):
    visitados.add(origem) # Marco como visitado e adiciono ao conjunto
    fila = [origem]

    while fila:
        vertice_atual = fila.pop(0)
        componente.add(vertice_atual) # Marco como parte da componente conexa o primeiro e subsequentes vértices
        for vizinho in lista_adj[vertice_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho) # Marco vizinhos como visitados (para prevenir iterações futuras desnecessárias)
                # e adiciono ao conjunto.
                # Obviamente, usamos conjuntos pq os valores VÃO se repetir, 
                # pois de novo será visitada outras origens (o bfs será executado n vezes), 
                # mas n queremos repetição, por isso usamos set.
                fila.append(vizinho)
```

### Algoritmo BFS: Achar se é verdade que o grafo tem pelo menos um ciclo

```python
# Algoritmo que retorna True ou False se detectar ou não um ciclo no grafo
    def tem_ciclo(self):
        visitados = ["Não"] * len(self.__lista_adj)
        pais = [None] * len(self.__lista_adj)

        for i in range(len(self.__lista_adj)):
            if visitados[i] == "Não":

                # BFS

                visitados[i] = "Sim"
                fila = [i]
                pais[i] = i
                while fila:
                    vertice_atual = fila.pop(0)
                    for vizinho in self.__lista_adj[vertice_atual]:
                        if visitados[vizinho] == "Não":
                            visitados[vizinho] = "Sim"
                            fila.append(vizinho)
                            pais[vizinho] = vertice_atual
                        elif pais[vertice_atual] != vizinho:
                            return True
                            
        return False
```
### TODO: Estudar Invariante de Laço

https://www.youtube.com/watch?v=AQ7A2Z0TdM4&ab_channel=CarlaQuemDisse

### TODO: Fazer 3 exercícios:

- Grau máximo do G
- Todos os graus de G
- Se tem ciclo em um grafo
- Retornar ciclos de um grafo