Atue como um especialista em Inteligência Artificial e LaTeX. Sua tarefa é resolver a "Questão 01" de uma prova de IA e formatar a resposta inteiramente em código LaTeX.

O código gerado será incluído em um projeto modular (através de um \input{q1.tex} em um main.tex). Portanto, NÃO inclua o preâmbulo (\documentclass, \begin{document}, \end{document}). Comece diretamente com \section*{Questão 01 - Busca em Espaço de Estados}.

Aqui estão as regras estritas para a formatação do LaTeX:
1. Modularidade: O código deve estar pronto para ser colado no arquivo `q1.tex`.
2. Árvores e Grafos: Use o pacote `tikz` para desenhar a árvore parcial de busca solicitada. 
3. Destaque Visual (CRÍTICO): Ao desenhar as árvores ou listar as ordens de expansão, os nós que já foram VISITADOS/EXPANDIDOS devem obrigatoriamente estar em uma cor diferente (por exemplo, preenchidos com \node[fill=blue!20] no tikz ou usando \textcolor{blue}{Nó} no texto). Crie uma legenda rápida explicando a cor.
4. Tabelas: Reproduza as tabelas solicitadas (Passo | Nó expandido | Conteúdo da fronteira) usando o ambiente `table` e `tabular`, mantendo a formatação limpa.
5. Código Python: Todo o código autoral solicitado deve ser formatado usando o pacote `listings` (\begin{lstlisting}[language=Python]) ou `minted`, garantindo indentação correta.
6. Organização: Use \subsection*{} e \subsubsection*{} para separar claramente cada item da questão (Modelagem, Execução dos Algoritmos, Implementação e Experimento Adicional).

Abaixo está o texto da questão que você deve resolver e formatar:

[INÍCIO DO TEXTO DA QUESTÃO]
Questão 01 - Busca em amplitude/largura, Busca em profundidade e Busca iterativa em profundidade.
Um agente deve se deslocar entre salas de um prédio. Cada sala é representada por uma letra. As conexões representam movimentos permitidos entre salas. Todas as ações possuem custo unitário. 
Grafo do problema (Sala -> Salas vizinhas em ordem obrigatória):
A -> B, C, D
B -> E, F
C -> G, H
D -> I, J
E -> K, L
H -> M
G -> N, O
J -> P

Estado inicial: A
Estado objetivo: S (Nota: Se o nó S não existe nas conexões descritas ou não é alcançável, declare isso na sua resposta de forma clara e lide com a busca até esgotar a fronteira ou atingir os limites do algoritmo).

A) Formule o problema como um problema de busca em espaço de estados: defina representação do estado, estado inicial, teste de objetivo, função sucessora, função de custo e representação em Python.
B) Resolva utilizando Busca em Amplitude (BFS), Busca em Profundidade (DFS) e Busca Iterativa em Profundidade (IDS). Para cada um, apresente: a ordem completa de expansão, conteúdo da fronteira após cada expansão, árvore parcial de busca, caminho solução, profundidade, custo, nós gerados e nós expandidos. Preencha a tabela de passos exigida.
C) Implemente os três algoritmos em Python (sem libs externas).
D) Experimento: modifique a ordem dos sucessores de dois nós, execute os algoritmos novamente, compare os resultados e analise o impacto. Responda as perguntas a-e da prova sobre o experimento.
E) Por fim, compare os algoritmos considerando completude, otimalidade, complexidades e adequação.
[FIM DO TEXTO DA QUESTÃO]

Entregue APENAS o código LaTeX formatado.