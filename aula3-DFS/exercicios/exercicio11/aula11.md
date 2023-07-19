**Questão 1**

Pós-condição 2: Se "encontrou_circuito" retornar falso, os  vértices no conjunto de vértices no estado "no_caminho_atual" não mudam de estado.

**Questão 2 e 3**

- Prova do invariante usando a pós condição 2:

Considere a invariância no conjunto de vértices com estado "no_caminho_atual".

Guardamos esse conjunto em uma variável $C$, para que possamos comparar o conjunto original com ele futuramente para saber se ele foi alterado ou não. Ou seja, conjunto de vértices com estado "no_caminho_atual" = C é verdadeiro.

Durante a execução da função, se um vértice vizinho é visitado e tem estado "no_caminho_atual", retorna True, ou seja, encontrou um circuito. Se não, se tiver "não_atingido", chama recursivamente "encontrou_circuito(vizinho)". 

Perceba que o conjunto original de vértices com estado "no_caminho_atual" não se altera, não importa quantas vezes chamamos recursivamente a função. Apenas estamos caminhando.

Agora... se nenhuma condição for atendida, vizinho tem seu estado finalizado, e daí em diante analisamos outros vizinhos. Depois de percorrer todos a partir da origem, finalizamos com "finalizado" o vértice de partida, origem. Lembrando, a atribuição de "origem" com "no_caminho_atual" ou "finalizado" não necessariamente diz que pertence ao caminho, pois está fora do laço, e portanto provar o invariante seria provar que o estado não muda dentro do laço.

E com isso, o conjunto de vértices "no_caminho_atual" permanece igual ao conjunto C, e isso prova o invariante.

- Prova da pós condição 2 usando o invariante

Começo novamente com a atribuição de que C recebe o conjunto de vértices com estado "no_caminho_atual", e portanto C = conjunto de vértices com estado "no_caminho_atual" é uma afirmação verdadeira.

Quando executa a função encontrou_circuito(origem), se encontrar um circuito durante a DFS, então retornará True e não teremos alterações no estado dos vértices. Agora se retornar False, não encontramos circuito, mas o vértice origem é alterado pra finalizado. Isso significa que o vértice origem não faz parte do caminho atual.

Ou seja, todos os vértices que foram visitados durante o DFS e que estavam no caminho atual permanecem nesse estado.

Portanto, a afirmação C = conjunto de vértices com estado "no_caminho_atual" continua verdadeira, e isso prova a pós condição 2 usando o invariante.

**Questão 4**

A volta da corretude se baseia no fato de que quando o algoritmo itera sobre todos os vizinhos do vértice de origem, o estado do vértice de origem é alterado para finalizado e não faz parte mais do caminho atual, retornando False, e portanto não foi encontrado um circuito a partir desse vértice.

Veja que o DFS verifica sempre o estado dos vértices. Há um circuito se e somente se encontrar um vizinho que já está no caminho atual.

Além disso, o algoritmo garante que os vértices do caminho atual permaneçam com o estado "no_caminho_atual" a cada chamada recursiva. Isso também garante que todos os vértices sejam explorados em profundidade a partir de um vértice de origem até o momento em que o último vértice explorado no caminho seja marcado como finalizado, e portanto garante que apenas os vértices na parte interna do caminho estejam no caminho atual. Isso é importante, pois é o que garante que em algum momento tenha a possibilidade de uma busca encontrar outro vértice com o mesmo caminho atual, retornando assim True e imediatamente detectando um circuito no grafo.