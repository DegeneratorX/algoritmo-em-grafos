# Exercícios

Esses exercícios são referentes da aula 08 até 16.

# DFS

## Aula 08

Definição de Circuito em Grafos Direcionados.
Definição do 2º Grande Problema da Disciplina (DFS).
Discussão sobre o Problema.
Conclusões da Discussão: Formas e Semântica da Marcação de Vértices, Recursos para Uso no Percurso, etc.

- **Utilizando as conclusões obtidas no final da aula de hoje, após discussão sobre como resolver o problema da detecção de circuitos, escreva um algoritmo que receba um grafo direcionado e que informe se ele possui ou não pelo menos um circuito.**

## Aula 09

Recapitulação e síntese das ideias discutidas na aula anterior.
Escrita dialogada de um algoritmo materializando essas ideias.
Simulação de execução do algoritmo.
Análise assintótica do tempo de execução do algoritmo.

- **Conforme é possível verificar nas fotos da aula de hoje (última coluna), devido à pressa no final da aula, nós acabamos esquecendo de analisar o custo assintótico (em termos do tempo de execução) das linhas 8 e 9 do algoritmo "encontrou_circuito". Assim sendo, responda: (a) qual é o custo de execução individual de cada uma dessas linhas, quando executadas uma única vez? (b) Qual é o custo "total" dessas linhas, isto é, o custo agregado, somando-se todas todas as possíveis chamadas da função "encontrou_circuito" durante uma mesma execução do algoritmo "tem_circuito"?**

- **Justifique, por escrito, a análise de tempo de execução feita em sala para as seguintes linhas de código: (a) Linha 1 de "encontrou_circuito"; (b) Linha 2 de "encontrou_circuito"; (c) Linha 4 de "encontrou_circuito"; (d) Linha 7 de "encontrou_circuito"; (e) Linha 6 de "tem_circuito"; (f) Linha 7 de de "tem_circuito".**

- **Escreva uma variação do algoritmo em que seja retornado não mais um booleano, mas sim uma sequência de vértices: se houver circuito, deve ser retornada a sequência de vértices que forma o circuito detectado; se não houver circuito, deve ser retornada uma sequência vazia.**

## Aula 10

Reescrita do algoritmo de detecção de circuitos usando função definida dentro de função.
Início da discussão da corretude do algoritmo: corretude quando o retorno é "verdadeiro".
Pré e Pós-condições da Função Recursiva: Enunciado e Argumentações.

- **Observe que a argumentação do caso 1 da última coluna do quadro de hoje possui uma marcação "*1". A marcação tem o seguinte motivo: o fato de que "estado[v] = no_caminho" quando a linha 11 é executada não significaria, a priori, que "v" tinha esse estado quando a função foi chamada, pois, em princípio, "v" poderia ter passado a estar no estado "no_caminho" durante a chamada atual (por exemplo durante as iterações anteriores do laço). Entretanto, é possível que, no início da chamada da função, "v" não estivesse no estado "no_caminho"? Responda e escreva a sua argumentação (na hora de escrevê-la, depois de encontrar a essência da resposta, você pode precisar escrever novas pré-condições, pós-condições ou mesmo algum invariante para o laço da função).**

- **Como você argumenta o caso 2 da prova da pós-condição S1?**

- **Como argumentar que, se o retorno do algoritmo "tem_circuito" é "falso", então G não possui circuito?**

## Aula 11

Recapitulação da parte já realizada da prova de corretude do algoritmo de detecção de circuitos (Busca em Profundidade - "DFS").
Prova da inferência implícita "*1" marcada na demonstração da aula anterior para o caso 1 da ida da corretude.
Prova do caso 2 da ida da corretude (a discussão verbal foi mais completa que a escrita realizada no quadro).
Comentários sobre os elementos de uma prova de terminação: variantes de laço e métricas de terminação para algoritmos recursivos (funções decrescentes do estado do algoritmo em conjuntos bem-ordenados para a componente fortemente conexa das funções mutuamente recursivas em questão).

- **Enuncie a pós-condição "S2" sobre o conjunto de vértices no estado "no_caminho" não mudar quando o retorno da função é "falso".**

- **Usando a pós-condição S2, prove o invariante I1. Lembre de mostrar que as pré-condições da função são satisfeitas quando ela é chamada.**

- **Usando o invariante I1, prove a pós-condição S2.**

- **Busque argumentar que a volta da corretude é verdadeira; não é necessário expressar a argumentação em termos de invariantes, pré e pós-condições.**

## Aula 12

Definições: Subgrafo, subgrafo gerador, árvore geradora, árvore geradora mínima (AGM).
Discussão sobre o 3º grande problema da disciplina: como computar uma AGM de um grafo.
Análise do tempo de execução da estratégia "enquanto ainda houver algum ciclo, remover a aresta mais pesada de algum ciclo".

- **(Algoritmo mais Rápido) Ao final da aula de hoje, nós observamos que a estratégia "enquanto houver ciclos, escolha um ciclo e dele remova uma aresta de peso máximo (dentre aquelas desse ciclo)" é uma candidata plausível para resolver o problema da AGM, e que essa estratégia pode ser implementada em tempo O( (n+m)*(m-(n-1)) ) = O(m² - n²), o que é um tempo significativamente maior que o dos algoritmos estudados anteriormente (busca em largura e busca em profundidade), que executam em tempo O(n+m). Procure então encontrar uma estratégia mais rápida (considere observar, por exemplo, as origens do tempo gasto no algoritmo descrito em sala (para então buscar melhorá-lo), ou então pensar em estratégias alternativas).**

- **(Detalhar Algoritmo de Sala) Escreva detalhadamente um algoritmo que implemente a estratégia descrita em sala: "enquanto houver ciclos, escolha um ciclo e dele remova uma aresta de peso máximo (dentre aquelas desse ciclo)". Dê especial atenção ao trecho do algoritmo que identifica e remove a aresta mais pesada do ciclo.**

## Aula 13

Discussão sobre como melhorar o algoritmo da aula anterior.
Discussão levando à Estratégia 1: (ao invés de começar com o grafo de entrada G inteiro e proceder retirando arestas pesadas de ciclos) começar com um grafo "A" contendo todos os vértices e nenhuma aresta, e então proceder considerando as arestas em ordem crescente de peso. Quando uma aresta {u,v} é considerada, ela é incluída em "A" se e somente se "u" e "v" pertencem a componentes conexas distintas em "A" (em caso contrário, um ciclo seria introduzido em A). Para identificar as componentes conexas, nós utilizamos "representantes": cada componente é identificada por um de seus vértices, e, para cada vértice "u", nós armazenamos o representante da componente de "u"; nesse caso, dois vértices "u" e "v" pertencem à mesma componente se e somente se possuem o mesmo representante. Ao adicionar uma aresta {u,v} a A, nós unimos as componentes de "u" e "v", o que implica em atualizar o representante de uma das 2 componentes; em sala, nós escolhemos atualizar o representante da componente de menor tamanho (para diminuir o tempo gasto nessa operação). Para fazer essa atualização, nós precisamos conhecer os vértices de cada componente, o que pode ser armazenado numa lista encadeada (para cada componente).
Discussão complementar levando à Estratégia 2: partindo de apenas um vértice, então apenas de uma aresta (digamos uma aresta de peso mínimo em G), nós mantemos um subgrafo conexo A de G, e então repetidamente ampliamos "A" pela inclusão de uma nova aresta {u,v} tal que u ∈ A e v ∉ A (o que garante que "A" permanece conexo e acíclico). A aresta {u,v} é escolhida como sendo a mais leve dentre aquelas que possuem uma extremidade em "A" e outra fora de "A".

- **Escreva detalhadamente um algoritmo que implemente a "estratégia 1" discutida em sala (descrição abaixo). (Você também pode escolher implementar de forma diferente a representação das componentes conexas, conforme ideia alternativa mencionada em sala.)**

- **Qual é o tempo de execução do algoritmo da questão anterior?**

- **Você consegue encontrar um contraexemplo para a estratégia 1 em questão? E para a estratégia 2?**

## Aula 14

Recapitulação da "estratégia 1" da aula anterior para computação de AGMs (e da trajetória até a estratégia).
Exemplo de aplicação da estratégia em um grafo concreto.
Escrita dialogada de parte de um algoritmo para materializar essa estratégia.

- **Escreva as funções repr(u) e unir(u,v) que ficaram faltando escrever ao final da aula de hoje. Conforme conversamos, repr(u) retorna o vértice que representa a componente conexa de "u", e unir(u,v) faz a união das componentes conexas dos vértices "u" e "v" (partindo do conhecimento de que "u" e "v" pertencem a componentes distintas).**

- **Qual é o tempo de execução do algoritmo da aula de hoje?**

- **Aprimorando o que vimos na aula 12: como detectar em tempo O(n) se um grafo não-direcionado possui ou não ciclos?**

## Aula 15

Finalização da escrita do algoritmo da "estratégia 1" das aulas anteriores para computação de AGMs.
Execução detalhada do algoritmo para uma entrada concreta.
Cálculo da complexidade assintótica do tempo de execução do algoritmo.

- **Argumente a corretude do algoritmo estudado na aula.**

## Aula 16

Escrita em alto nível de abstração do algoritmo de Kruskal (que é o da "estratégia 1" das aulas passadas).
Discussão sobre como demonstrar a corretude do algoritmo.
Demonstração verbal e por desenhos do invariante principal da corretude do algoritmo.

- **Prove os invariantes I0, I1, I2 e I4 enunciados no material complementar. (Todos são bem simples e, em particular, muito mais simples que o invariante I3 demonstrado no material.)**

- **Nós não abordamos em sala a terminação do algoritmo de Kruskal. Argumente então que o algoritmo sempre termina (você pode fazer isso apresentando uma métrica de terminação para o laço do algoritmo, ou seja, uma expressão que diminui a cada iteração, e que não pode assumir valores abaixo de um certo limite inferior). As seguintes perguntas são relevantes nesse contexto: (a) O conjunto "A" aumenta a cada iteração do laço? (b) É possível que, no início de alguma iteração, o conjunto "A" ainda não possua n-1 arestas e que a lista L esteja vazia?**