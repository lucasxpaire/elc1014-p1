Atue como um especialista em Inteligência Artificial e LaTeX. Sua tarefa é resolver a "Questão 01" de uma prova de IA e formatar a resposta inteiramente em código LaTeX.

O código gerado será incluído em um projeto modular (através de um \input{q2.tex} em um main.tex). Portanto, NÃO inclua o preâmbulo (\documentclass, \begin{document}, \end{document}). Comece diretamente com \section*{Questão 02 - Busca Gulosa pela Melhor Escolha e A*}.

Aqui estão as regras estritas para a formatação do LaTeX:
1. Modularidade: O código deve estar pronto para ser colado no arquivo `q2.tex`.
2. Árvores e Grafos: Use o pacote `tikz` para desenhar a árvore parcial de busca solicitada. 
3. Destaque Visual (CRÍTICO): Ao desenhar as árvores ou listar as ordens de expansão, os nós que já foram VISITADOS/EXPANDIDOS devem obrigatoriamente estar em uma cor diferente (por exemplo, preenchidos com \node[fill=blue!20] no tikz ou usando \textcolor{blue}{Nó} no texto). Crie uma legenda rápida explicando a cor.
4. Tabelas: Reproduza as tabelas solicitadas usando o ambiente `table` e `tabular`, mantendo a formatação limpa.
5. Código Python: Todo o código autoral solicitado deve ser formatado usando o pacote `listings` (\begin{lstlisting}[language=Python]) ou `minted`, garantindo indentação correta.
6. Organização: Use \subsection*{} e \subsubsection*{} para separar claramente cada item da questão (Modelagem, Execução dos Algoritmos, Implementação e Experimento Adicional).

Abaixo está o texto da questão que você deve resolver e formatar:

[INÍCIO DO TEXTO DA QUESTÃO]
Considerar o seguinte problema de navegação em um ambiente parcialmente bloqueado: um agente deve sair da posição A e alcançar a posição T. Cada aresta possui um custo associado. Além disso, cada estado possui um valor heurística h(n), que representa uma estimativa da distância restante até o objetivo. O grafo do problema é apresentado abaixo:

[INÍCIO DO GRAFO DO PROBLEMA]
Colunas: Nó | Sucessores (custo) | h(n)
A | B(2), C(4), D(3) | 10
B | E(3), F(5) | 8
C | G(4), H(6) | 7
D | I(2) | 9
E | J(4) | 6
F | K(3), L(5) | 5
G | M(6) | 6
H | N(3), O(4) | 4
I | P(5) | 7
J | Q(4) | 5
K | R(3) | 3
L | - | 6
M | S(2) | 3
N | - | 4
O | T(5) | 1
P | - | 8
Q | - | 4
R | T(4) | 2
S | T(3) | 1
T | - | 0
[FIM DO GRAFO DO PROBLEMA]
Estado inicial: A
Estado objetivo: T

Modelar o problema como um problema de busca em espaço de estados. Apresentar: a) representação dos estados; b) estado inicial; c) teste de objetivo; d) função sucessora; e) função de custo; f) interpretação da heurística h(n).
Em seguida, resolver o problema usando algoritmo Greedy Best-First Search utilizando o valor heurístico:
f(n) = h(n)
Apresentar:
a) ordem de expansão dos nós;
b) conteúdo da fronteira após cada expansão;
c) valores heurísticos utilizados;
d) caminho solução encontrado;
e) custo final da solução;
f) quantidade de nós gerados;
g) quantidade de nós expandidos.

Resolver o mesmo problema utilizando o algoritmo A* com:
f(n) = g(n) + h(n)
onde:
g(n): custo acumulado do caminho;
h(n): heurística fornecida;
f(n): custo estimado total.

Para cada expansão, apresentar:
a) nó expandido;
b) valor de g(n);
c) valor de h(n);
d) valor de f(n);
e) conteúdo da fronteira ordenada;
f) caminho parcial até o nó.

Preencher tabelas no seguinte formato:
[INÍCIO DO EXEMPLO DE TABELA]
Colunas: Passo | Nó | g(n) | h(n) | f(n)
Exemplo de linha: 1 | A | 0 | 10 | 10
[FIM DO EXEMPLO DE TABELA]

Implementar os algoritmos Busca Gulosa pela Melhor Escolha e Busca A* em Python respeitando os seguintes critérios: Não utilizar bibliotecas externas.

Modificar os valores heurísticos de exatamente três nós do grafo. Após isso, 1) execute novamente os algoritmos; 2) compare os resultados; 3) analise o impacto da heurística.

Responder as seguintes questões:
a) A solução encontrada mudou?
b) O custo da solução mudou?
c) A busca gulosa encontrou solução ótima?
d) O A* encontrou solução ótima?
e) Qual algoritmo expandiu menos nós?
f) Qual algoritmo foi mais sensível à heurística?

Por fim, comparar Greedy Best-First Search e A* considerando: a) completude; b) otimalidade; c) consumo de memória; d) dependência da heurística; e) custo computacional; f) qualidade das soluções; g) comportamento em grafos grandes.

[FIM DO TEXTO DA QUESTÃO]

Entregue o código LaTeX formatado, bem como os scripts do Python.