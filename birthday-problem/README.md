# O Problema do Aniversário

## 1. Definição do Problema
[cite_start]O problema consiste em verificar se, num grupo de estudantes, existe algum par que partilhe exatamente a mesma data de nascimento[cite: 34]. [cite_start]Formalmente, um problema é uma relação abstrata e matemática entre um conjunto de inputs e um conjunto de outputs válidos[cite: 7]. O input é uma lista de aniversários e o output esperado é o par correspondente (se existir) ou a indicação de que não há correspondência.

## 2. Descrição do Algoritmo
[cite_start]O algoritmo determinístico concebido para resolver este problema segue os seguintes passos[cite: 34, 35]:
1. [cite_start]Manter um registro em memória[cite: 35].
2. [cite_start]Entrevistar os estudantes um por um, em uma determinada ordem[cite: 36].
3. [cite_start]Checar se o aniversário do estudante atual já se encontra no registro[cite: 37].
4. [cite_start]Caso o aniversário já esteja lá, retornar o par encontrado e interromper a busca[cite: 38].
5. [cite_start]Caso contrário, adicionar o estudante ao registro e passar para a próxima pessoa[cite: 39].
6. [cite_start]Se o processo analisar todos os estudantes e não encontrar nenhuma correspondência, retornar que não existe par[cite: 40].

## 3. Prova de Correção
[cite_start]Para provar que o algoritmo funcionará de forma consistente, independentemente da escala dos dados que recebe, dependemos da indução matemática[cite: 24]. 

* [cite_start]**Hipótese Indutiva:** Se os primeiros $k$ estudantes contêm uma correspondência, o algoritmo retorna um par antes de entrevistar o estudante $k+1$[cite: 209].
* **Caso Base ($k=0$):** Após entrevistar 0 estudantes, é impossível haver uma correspondência. [cite_start]O predicado é falso, logo a afirmação mantém-se verdadeira trivialmente[cite: 218, 219].
* [cite_start]**Passo Indutivo:** Assumindo que a hipótese é verdadeira para os primeiros $k'$ estudantes, avaliamos o estudante $k'+1$[cite: 221, 222]. [cite_start]Existem dois casos possíveis[cite: 223]:
  1. [cite_start]A correspondência já existia nos primeiros $k'$ estudantes e, pela hipótese indutiva, já foi retornada[cite: 227].
  2. A correspondência envolve o estudante $k'+1$. [cite_start]O algoritmo verifica se o aniversário deste estudante está no registo[cite: 230]. [cite_start]Se estiver, retorna a correspondência [cite: 231][cite_start]; caso contrário, adiciona-o ao registo, restabelecendo a hipótese indutiva[cite: 232].

## 4. Análise Assintótica
[cite_start]A eficiência é medida contando o número de operações fundamentais em função do tamanho do input ($n$), usando análise assintótica, e isolando o algoritmo do poder físico da máquina[cite: 12, 26]. [cite_start]Assumimos o modelo Word RAM, que permite acesso aleatório à memória num instante de tempo constante ($\Theta(1)$)[cite: 25].

[cite_start]A estrutura de dados escolhida para o registo afeta drasticamente a eficiência do nosso algoritmo[cite: 45]:
* [cite_start]**Usando uma Lista:** Verificar se o aniversário já está no registo obrigaria a ler os elementos inseridos um a um, consumindo tempo linear[cite: 47]. [cite_start]Como fazemos isso iterativamente para cada um dos $n$ estudantes, o tempo total do algoritmo cresceria de forma vertiginosa, resultando num tempo de execução quadrático, ou $\Theta(n^2)$[cite: 48].
* [cite_start]**Usando um Conjunto (Set):** O tempo médio para verificar se um elemento existe dentro de um conjunto (implementado como Hash Table) é constante, ou seja, $\Theta(1)$[cite: 49, 50]. [cite_start]Assim, se gastamos tempo constante para cada um dos $n$ estudantes, o tempo total do nosso algoritmo cai para um nível incrivelmente eficiente e linear, ou $\Theta(n)$[cite: 51].