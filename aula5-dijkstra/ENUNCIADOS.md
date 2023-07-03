# Exercícios

Esses exercícios são referentes da aula 17 até 20.

## Aula 17

4º Grande Problema da Disciplina: Distâncias em Grafos Ponderados com Fonte Única.
Discussão sobre como resolver o problema: variações de algoritmos anteriores, etc.
Culminância da discussão com uma estratégia que resolve o problema: simulação, cômputo dos caminhos mínimos (e não apenas as distâncias), etc.

- **Escreva um algoritmo que materialize a estratégia discutida ao final da aula. Você pode começar com uma versão não otimizada, e depois tentar produzir uma implementação mais eficiente.**

- **Procure argumentar a corretude do algoritmo. Em particular, por que a estimativa de distância para o vértice de menor estimativa é de fato a própria distância até o vértice?**

- **A estratégia discutida ao final da aula ainda funciona na presença de pesos negativos? Argumente que sim, ou então apresente um contraexemplo com o menor número possível de arestas negativas.**

## Aula 18

Recapitulação e tira-dúvidas sobre o algoritmo da aula anterior para cômputo de distâncias em grafos ponderados (algoritmo de Dijkstra).
Discussão sobre as estruturas de dados a serem utilizadas para implementar o algoritmo.
Início da escrita do algoritmo.

- **(Importante) Uma implementação básica de monte ("heap") binário de mínimo tipicamente operece as seguintes operações: a) criar(m): cria um heap vazio para até "m" elementos (uma alternativa é já receber alguns elementos para inserir, e organizá-los como um heap usando o algoritmo linear de Floyd, mas isso não é necessário neste exercício); b) inserir(u): insere o elemento "u" no heap; c) consultar_mínimo(): retorna o elemento do topo do heap; d) remover_mínimo(): remove o elemento do topo do heap. Entretanto, conforme discutido na aula de hoje, se nós sabemos que todos os elementos que podem ser inseridos no heap são identificados por números naturais distintos no intervalo [0..n-1], então é possível armazenar as posições dos elementos num vetor e então viabilizar operações adicionais como: e) pertence(u): retorna um booleano informando se (o elemento identificado por) "u" está ou não no heap (executa em O(1)); f) consultar_peso(u): retorna o "peso" de (o elemento identificado por) "u"; g) alterar_peso(u, novo_p): altera o peso de (o elemento identificado por) "u" para "novo_p". Escreva então uma implementação de heap de mínimo que armazene pares (u,p), em que "u" é um identificador em [0..n-1] e "p" é o peso do elemento, que será usado para compará-lo com os demais elementos. O valor de "n" e o número "m" máximo de elementos que poderão estar simultaneamente armazenados no heap são recebidos no momento da criação do heap. É especialmente importante que a sua implementação inclua as funções/métodos "pertence", "consultar_peso" e "alterar_peso".**

- **Usando as operações acima, complete a implementação de algoritmo de caminhos mínimos iniciada em sala.**

- **Qual é a complexidade assintótica do tempo de execução do algoritmo?**

- **Argumente a corretude da estratégia do algoritmo de Dijkstra. Você pode focar na essência do argumento, sem necessariamente descer ao nível de precisão de invariantes de laço, por exemplo.**

# Aula 19

Escrita do algoritmo de Dijkstra para caminhos mínimos em grafos ponderados.
Tira-dúvidas sobre o código do algoritmo e exemplo de escrita de uma das funções do heap que usam o vetor de posições.
Simulação do algoritmo para um grafo concreto.
Análise assintótica do tempo de execução do algoritmo.

Aproveito para deixar registrado aqui, por escrito, alguns pontos da análise assintótica do tempo de execução do algoritmo de Dijkstra para caminhos mínimos, realizada na aula de hoje:

A criação do heap custa Θ(n), ao invés de O(1), pois não se trata apenas de alocar o vetor do heap e inicializar a estrutura/registro, mas também de inicializar cada elemento do vetor de posições, de forma que fique registrado, para cada vértice "u", que "u" inicialmente não está no heap.
Descobrir se um vértice "v" está ou não no heap (linha 14), e consultar o peso de um vértice "v" que está no heap (linha 18), são operações que custam O(1) no caso especial do heap que estamos utilizando, pois o heap guarda as posições dos elementos. A operação "peso_de" foi inclusive escrita na última coluna do quadro, a pedido de um estudante, e mostra como podemos utilizar o vetor de posições.
Na linha 15, o custo total é O(n*lg n) porque a linha 15 corresponde apenas ao caso em que o vértice é inserido no heap, e cada vértice é inserido no heap no máximo uma vez. Essa linha é também o momento em que o vértice é atingido pela primeira vez, o que naturalmente ocorre apenas uma vez para cada vértice.
Na linha 19, atualizar o peso de um vértice uma vez custa O(lg n), pois, usando o vetor de posições, nós chegamos à posição do vértice no heap em tempo constante, e daí é só atualizar o peso e executar a função "subir" do heap, que leva tempo logarítmico. Além disso, cada vértice tem seu peso atualizado no máximo uma vez para cada aresta que nele chega, ou seja, tem seu peso atualizado um número de vezes que é no máximo igual ao seu grau de entrada. Como a soma dos graus de entrada dos vértices é igual ao número de arestas do grafo, então, no total do algoritmo, o custo da linha 19 é O(m*lg n).
Na análise do algoritmo de Kruskal, para o problema da AGM, foi possível simplificar O( (m+n)*lg n ) para O(m*lg n) porque lá o grafo é conexo, logo m >= n-1 ∴ n <= m+1 ∴ n = O(m). Entretanto, não é possível fazer o mesmo no caso do algoritmo de Dijkstra, pois não há restrição envolvendo o número de arestas do grafo.

- **O item 5 acima explica que, no caso geral do algoritmo de Dijkstra, não é possível concluir que m+n = O(m). Entretanto, e no caso específico em que se sabe que todos os vértices são atingíveis a partir da origem: é possível concluir que m+n = O(m)? Argumente.**

- **Escreva uma versão do algoritmo de Dijkstra que, ao invés de um heap, utilize apenas um vetor simples com as estimativas de distâncias, e que, para descobrir o "próximo vértice a entrar na fronteira", simplesmente percorre o vetor "calculando o mínimo", gastando portanto tempo Θ(n). Se você precisar de um vetor auxiliar para distinguir entre os vértices que estão dentro e os que estão fora da fronteira, fique à vontade para utilizar um.**

- **Qual é o tempo de execução da versão do algoritmo de Dijkstra do item anterior, utilizando um vetor simples ao invés de um heap?**

- **Existem casos em que a versão do algoritmo de Dijkstra baseada em vetor simples é mais rápida que a versão usando heap? Explique, com base no valor de "m".**

- **Você consegue escrever um algoritmo mais rápido que o algoritmo de Dijkstra para o caso específico do problema de caminhos mínimos em que já se sabe que o grafo de entrada não possui circuitos?**

- **Você consegue adaptar o algoritmo de Dijkstra gerando uma materialização da "estratégia 2" da aula 13 para o problema da AGM? (Veja a notícia do SIGAA com o conteúdo da aula 13 para recapitular essa estratégia.)**

## Aula 20

Corretude do Algoritmo de Caminhos Mínimos de Dijkstra: Intuição e enunciado do Lema principal, discussão e escrita da prova.

CORREÇÃO: na especificação do conjunto "A", substituir o trecho [existe caminho de "o" a "u"] por [existe um caminho mínimo de "o" a "u" contendo apenas vértices em "A"].

- **Enuncie um invariante para o laço principal do algoritmo de Dijkstra, afirmando que as distâncias estão calculadas corretamente.**

- **Prove o invariante do item anterior usando o lema provado na aula de hoje. Você pode enunciar invariantes auxiliares, se necessário.**

- **Que métrica de terminação pode ser usada para argumentar que o algoritmo termina?**