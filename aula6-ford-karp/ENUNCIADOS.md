# Exercícios

Esses exercícios são referentes da aula 21 até 27.

## Aula 21

Introdução informal ao Problema de Fluxo Máximo: (a) Noção de fluxo e relação com transporte ao longo do tempo; (b) Motivação da restrição de conservação; (c) Exemplos concretos e discussão sobre os elementos do problema de fluxo máximo; (d) Fluxo chegando na origem e Valor do Fluxo; (e) Fluxo em arestas opostas e simplificação correspondente.

- **Pense em como resolver o problema do fluxo máximo.**

## Aula 22

Definições Formais de Rede de Fluxo, Fluxo, Valor de Fluxo, Fluxo Máximo e o Problema de Fluxo Máximo.
Discussão de Ideias para o Problema: Obtenção de um Fluxo por Caminhos Sucessivos, o Problema de Obter "Caminhos Ruins" (Longos ou Curtos) e a Ideia de devolver fluxo já enviado através de arestas (incluindo "arestas voltando" para lembrar dessa possibilidade).

- **Experimente a ideia ilustrada no final da aula (a de incluir arestas "voltando" para lembrar da possibilidade de "devolver fluxo", e do quanto devolver) em diferentes grafos concretos: você entendeu a proposta? Ela sempre funciona? Use grafos com arestas de diferentes pesos, para tornar os exemplos mais interessantes.**

- **(Apenas para depois do exercício anterior) Escreva um algoritmo implementando essa ideia. Uma opção é começar com uma versão em alto nível de abstração, e depois escrever outra mais detalhada.**

## Aula 23

Recapitulação da aula anterior.
"Arestas Voltando": capacidade e "combinação" com arestas existentes.
Definições formais: "capacidade sobrando", fluxo que "pode voltar", capacidade residual e rede residual.
Corolário: a rede residual também é uma rede de fluxo.

- **Prove o corolário enunciado no final da aula. (A argumentação deve ser trivial.)**

- **Considerando a rede de fluxo do 2º exemplo desenhado em sala (veja as fotos), desenhe a rede residual correspondente a cada um dos seguintes momentos: (a) no início (fluxo zero em todas as arestas); (b) após passar 1 unidade de fluxo pelo caminho o -> A -> B -> d; (c) após passar 2 unidades de fluxo pelo caminho o -> B -> A -> d; (d) após passar 1 unidade de fluxo novamente pelo caminho o -> A -> B -> d. Por fim: existe caminho de "o" a "d" na rede residual correspondente ao momento (d)?**

## Aula 24

Recapitulação das definições de Capacidade e Rede Residuais.
Exemplos de obtenção de fluxos através de caminhos aumentantes em redes residuais.

- **Para o exemplo "b" da aula de hoje, mostre os fluxos e redes residuais relativos a uma sequência diferente de caminhos aumentantes.**

## Aula 25

Recapitulação da definição formal de rede residual e auxiliares.
Formalização dialogada e exemplificada de noções discutidas na aula anterior: caminho aumentante, capacidade residual de caminho aumentante e fluxo aumentado a partir de caminho aumentante.

- **O que na aula de hoje nós chamamos de "função de fluxo aumentado" é, na realidade, um fluxo na rede original; entretanto, formalmente falando, é necessário provar que essa função atende às propriedades da definição de fluxo. Mostre então que esse é o caso, demonstrando que, se f' é a função de fluxo aumentado relativa a uma rede G, um fluxo "f" (em G) e um caminho aumentante "p" (relativo a G e f), então: (a) f'(u,v) >= 0, para toda aresta (u,v) ∈E; (b) (Restrição de) Capacidade: f'(u,v) <= c(u,v), para toda (u,v) ∈E; (c) Unidirecionalidade: se (u,v),(v,u) ∈E, e se f(u,v) > 0, então f(v,u) = 0; (d) Conservação: para todo vértice "u" diferente da origem e do destino, a soma do fluxo chegando em "u" é igual à soma do fluxo saindo de "u". Por fim, demonstre que (e) o valor do fluxo f' é igual ao valor do fluxo f mais a capacidade residual de "p".**

- **Usando as definições construídas nas últimas aulas (rede residual, caminho aumentante, fluxo aumentado, etc), escreva, em alto nível de abstração, um algoritmo que materialize a estratégia discutida até aqui para a obtenção de fluxos máximos.**

## Aula 26

Enunciado e explicação do teorema sobre fluxos aumentados a partir de caminhos aumentantes.
O método de Ford-Fulkerson para a obtenção de fluxos máximos.
Intuição e Definição de Corte em Redes de Fluxo.
Notação de Soma Implícita e para Fluxos e Capacidades.
Intuição, enunciado e demonstração de lema limitando o fluxo líquido cruzando um corte à capacidade do corte.
Intuição e enunciado de lema igualando o valor de um fluxo ao saldo de fluxo cruzando um corte qualquer.
Enunciado e intuição da demonstração de teorema sobre a maximalidade de fluxos para os quais não há caminhos aumentantes.

- **Prove os seguintes resultados simples (mas úteis) relativos à notação de soma implícita para fluxos (para cada resultado, pense primeiramente se ele faz sentido, e ganhe intuição a respeito):**

    - **f(X,X) = 0, para todo X ⊆ V.**
    - **f(X,Y) = -f(Y,X), para quaisquer X,Y ⊆ V.**
    - **f(X ∪ Y, Z) = f(X,Z) + f(Y,Z), para quaisquer X,Y,Z ⊆ V tais que X ∩ Y = ∅.**

- **Tente demonstrar o Lema 5 da aula de hoje, com base na intuição apresentada em sala.**

## Aula 27

Enunciado, Prova e Exemplo de Teorema: um fluxo é máximo sse não há caminhos aumentantes a ele relativos.
Observação sobre o Tempo de Execução de Ford-Fulkerson: pode ser proporcional às capacidades das arestas.
Algoritmo de Edmonds-Karp: Definição e Menção ao Tempo de Execução.

- **Para compreender os detalhes envolvidos na solução do problema de fluxo, escreva em detalhes o algoritmo de Edmonds-Karp, isto é, a versão particular do método de Ford-Fulkerson que usa a Busca em Largura para descobrir os caminhos aumentantes. Dê particular atenção a uma representação eficiente da rede residual, bem como a uma atualização eficiente da rede a cada novo caminho aumentante. (Você pode supor que, na rede de entrada, todos os vértices são atingíveis a partir da origem, ou seja, você não precisa incluir no algoritmo um passo de pré-processamento.)**