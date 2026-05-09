Atue como um especialista em Inteligência Artificial e LaTeX. Sua tarefa é resolver a "Questão 04" de uma prova de IA e formatar a resposta inteiramente em código LaTeX.

O código gerado será incluído em um projeto modular (através de um \input{q4.tex} em um main.tex). Portanto, NÃO inclua o preâmbulo (\documentclass, \begin{document}, \end{document}). Comece diretamente com \section*{Questão 04 - CSP e Otimizações de Busca}.

Aqui estão as regras estritas para a formatação do LaTeX:
1. Modularidade: O código deve estar pronto para ser colado no arquivo `q2.tex`.
2. Árvores e Grafos: Use o pacote `tikz` para desenhar a árvore parcial de busca solicitada. 
3. Destaque Visual (CRÍTICO): Ao desenhar as árvores ou listar as ordens de expansão, os nós que já foram VISITADOS/EXPANDIDOS devem obrigatoriamente estar em uma cor diferente (por exemplo, preenchidos com \node[fill=blue!20] no tikz ou usando \textcolor{blue}{Nó} no texto). Crie uma legenda rápida explicando a cor.
4. Tabelas: Reproduza as tabelas solicitadas usando o ambiente `table` e `tabular`, mantendo a formatação limpa.
5. Código Python: Todo o código autoral solicitado deve ser formatado usando o pacote `listings` (\begin{lstlisting}[language=Python]) ou `minted`, garantindo indentação correta.
6. Organização: Use \subsection*{} e \subsubsection*{} para separar claramente cada item da questão (Modelagem, Execução dos Algoritmos, Implementação e Experimento Adicional).

Abaixo está o texto da questão que você deve resolver e formatar:

[INÍCIO DO TEXTO DA QUESTÃO]
Um hospital precisa montar automaticamente a escala de plantões de um pequeno grupo de médicos. Os turnos são T1, T2, T3, T4, T5, T6.
Os médicos disponíveis são {A, B, C, D}
Cada turno deve possuir exatamente um médico.
Restrições que devem ser consideradas:
1. O mesmo médico não pode trabalhar em turnos consecutivos.
2. O médico A não pode trabalhar em T3.
3. O médico B deve trabalhar em pelo menos um turno entre T1, T2.
4. O médico C não pode trabalhar simultaneamente em T2 e T5.
5. O médico D pode trabalhar no máximo em dois turnos.

Modelar o problema como um Constraint Satisfaction Problem (CSP). Apresentar:
a) conjunto de variáveis
b) domínio de cada variável
c) restrições unárias
d) restrições binárias
e) restrições globais
f) representação do grafo de restrições

Em seguida, resolver o problema utilizando Backtracking e apresentar:
a) árvore parcial da busca
b) ordem de atribuição das variáveis
c) conflitos encontrados
d) estados descartados
e) retrocessos realizados
f) solução final encontrada

Apresentar a tabela:
[INÍCIO DO EXEMPLO DA TABELA]
Colunas: Passo | Variável atribuída | Estado Parcial
Linha: 1 | T1 = A | {T1 = A}
Linha: 2 | T2 = A | conflito
Linha: 3 | T2 = B | {T1 = A, T2 = B}
[FIM DO EXEMPLO DA TABELA]
Resolver o problema utilizando MRV (Minimum Remaining Values) e Degree Heuristic e explicar:
a) qual variável foi escolhida em cada passo
b) por que ela foi escolhida
c) como MRV reduziu o espaço de busca
d) como Degree influenciou a busca

Implementar Forward Checking e apresentar:
a) redução dos domínios após cada atribuição
b) domínios eliminados
c) momento em que inconsistências foram detectadas
d) comparação com backtracking simples

Implementar Backjumping e apresentar:
a) variáveis responsáveis pelos conflitos
b) saltos realizados
c) diferenças para backtracking tradicional
d) redução observada na árvore de busca

IMplementar os algoritmos Backtracking, Backtracking + MRV, Backtracking + MRV + Degree, Forward Checking e Backjumping em Python sem utilizar bibliotecas externas.

Por fim, comparar os algoritmos considerando:
a) número de estados explorados
b) número de retrocessos
c) velocidade de execução
d) consumo de memória
e) facilidade de implementação

[FIM DO TEXTO DA QUESTÃO]

Entregue o código LaTeX formatado, bem como os scripts do Python.