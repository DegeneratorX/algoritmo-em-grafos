**Questão 1:**
- $O(1)$ para os dois casos. $O(n)$ para o pior caso de chamadas recursivas.
- 

**Questão 2:**
- Linha 1 encontrou_circuito: $O(1)$, pois a função por si só é executada apenas 1 vez. Porém, com chamadas recursivas, pode ser executada, no pior caso, $O(n)$, pois um grafo poderia ser cíclico, onde todos os vértices seriam percorridos e estes mesmos vértices fazem parte do circuito.

- Linha 2 encontrou_circuito: No pior caso, seria $O(grau(u))$, pois o laço percorre os vizinhos, e no pior caso, todos os vizinhos precisariam ser analisados, com chance de não retornar verdadeiro, inclusive.

- Linha 4 encontrou_circuito: No pior caso $O(1)$, pois se encontrar um vértice que está atualmente no percurso, então essa será a única vez que isso será retornado, e em cadeia (ao esvaziar a call stack), esse retorno não será mais executado, e sim o da linha 7.

- Linha 7 encontrou_circuito: Esse retorno será executado $O(n)$ no total, pois quando a call stack começar a esvaziar, esse retorno será executado $n$ vezes, a fim de retornar para o algoritmo "tem_circuito" um booleano verdadeiro.

- Linha 6 tem_circuito: O(n) no total, pois no pior caso, todos os vértices $o$ precisam ser percorridos com DFS até encontrar um circuito. Afinal, precisamos testar para todos os vértices, incluindo um grafo desconexo.

- Linha 7 tem_circuitos: O(1), pois essa linha será executada apenas uma vez se a condicional da linha 6 for atendida.