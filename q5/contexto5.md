Atue como um especialista em Inteligência Artificial e LaTeX. Sua tarefa é resolver a "Questão 05" de uma prova de IA e formatar a resposta inteiramente em código LaTeX.

O código gerado será incluído em um projeto modular (através de um \input{q5.tex} em um main.tex). Portanto, NÃO inclua o preâmbulo (\documentclass, \begin{document}, \end{document}). Comece diretamente com \section*{Questão 05 - Minimax e Poda Alpha-Beta}.

Aqui estão as regras estritas para a formatação do LaTeX:
1. Modularidade: O código deve estar pronto para ser colado no arquivo `q5.tex`.
2. Árvores e Grafos: Use o pacote `tikz` para desenhar a árvore parcial de busca solicitada. 
3. Destaque Visual (CRÍTICO): Ao desenhar as árvores ou listar as ordens de expansão, os nós que já foram VISITADOS/EXPANDIDOS devem obrigatoriamente estar em uma cor diferente (por exemplo, preenchidos com \node[fill=blue!20] no tikz ou usando \textcolor{blue}{Nó} no texto). Crie uma legenda rápida explicando a cor.
4. Tabelas: Reproduza as tabelas solicitadas usando o ambiente `table` e `tabular`, mantendo a formatação limpa.
5. Código Python: Todo o código autoral solicitado deve ser formatado usando o pacote `listings` (\begin{lstlisting}[language=Python]) ou `minted`, garantindo indentação correta.
6. Organização: Use \subsection*{} e \subsubsection*{} para separar claramente cada item da questão (Modelagem, Execução dos Algoritmos, Implementação e Experimento Adicional).

Abaixo está o texto da questão que você deve resolver e formatar:

[INÍCIO DO TEXTO DA QUESTÃO]
Considerar a seguinte árvore de jogo para um jogo determinístico de dois
jogadores. O jogador MAX realiza a primeira jogada na raiz da árvore.
Os valores nas folhas representam a utilidade final do jogo.

[INÍCIO DA ÁRVORE DO PROBLEMA]
A árvore é composta por 4 níveis (0 a 3):
- Nível 0 (Raiz): MAX
- Nível 1: 3 nós MIN (Filhos da Raiz)
- Nível 2: Cada nó MIN possui 2 filhos MAX (Total: 6 nós MAX)
- Nível 3 (Folhas): Cada nó MAX possui 2 valores terminais.

Sequência de Valores Terminais (da esquerda para a direita):
`[3, 5, 6, 9, 1, 2, 0, -1, 7, 4, 5, 6]`

Estrutura de ramos:
1. MIN 1: [MAX(3, 5), MAX(6, 9)]
2. MIN 2: [MAX(1, 2), MAX(0, -1)]
3. MIN 3: [MAX(7, 4), MAX(5, 6)]
[FIM DA ÁRVORE DO PROBLEMA]

A ordem de expansão dos filhos deve seguir obrigatoriamente da esquerda
para a direita. Explicar:
a) objetivo do algoritmo Minimax;
b) diferença entre nós MAX e MIN;
c) conceito de utilidade;
d) propagação de valores na árvore;
e) hipótese de adversário perfeito;
f) objetivo da poda Alpha-Beta.

Executar passo a passo o algoritmo Minimax na árvore apresentada e
apresentar: a) valores calculados em cada nó; b) ordem de expansão; c)
propagação dos valores; d) decisão tomada por MAX; e) caminho esco
lhido pelo algoritmo; f) árvore parcialmente preenchida.
Apresentar a tabela:
Colunas: Nó | Tipo | Valor Minimax

Linha: A | MAX | ...
Linha: B | MIN | ...
Linha: C | MAX | ...

Executar a Poda Alpha-Beta utilizando a MESMA ordem de expansão. Apresentar:
a) valores de alfa e beta em cada passo;
b) momento em que ocorreram podas;
c) quais ramos foram podados;
d) motivo matemático da poda;
e) quantidade de nós NÃO explorados.

Apresentar a tabela:
Colunas: Passo | Nó | alfa | beta | Poda?
Linha: 1 | A | ... | ... | não
Linha: 2 | B | ... | ... | não

Alterar a ordem de expansão dos filhos de forma a maximizar o número
de podas. Em seguida, discutir:

a) Quantas podas ocorreram antes?
b) Quantas podas ocorreram depois?
c) Por que a nova ordem melhora a eficiência?
d) Qual a relação entre ordenação e desempenho?

Considerar agora que a árvore é muito grande e que a busca deve parar
na profundidade 2. Os seguintes valores heurísticos devem ser usados
nos nós não-terminais da profundidade limite:
[4,7,2,5,6,1]

Responder:

a) executar Minimax limitado:
b) utilizar os valores heurísticos;
c) comparar a decisão com Minimax completo;
d) discutir possíveis erros causados pela heurística.

Implementar os algoritmos Minimax, Alpha-Beta e Minimax com profundidade limitada, em Python respeitando os seguints critérios: NÃO utilizar bibliotecas externas.

Comparar Minimax e Alpha-Beta considerando: a) número de nós explorados; b) quantidade de podas; c) custo compautacional, d) custo de memória; e) impacto da ordenação dos movimentos; f) qualidade das decisões.
Em um experimento adicional, modificar os valores de exatamente 3 folhas da árvore, Após isso:
1, executar novamente Mininax;
2. executar novamente Alpha-Beta;
3. verificar se a decisão final mudou;
4. analisar a sensibilidade do algoritmo às utilidades.

[FIM DO TEXTO DA QUESTÃO]