Atue como um especialista em Inteligência Artificial e LaTeX. Sua tarefa é resolver a "Questão 03" de uma prova de IA e formatar a resposta inteiramente em código LaTeX.

O código gerado será incluído em um projeto modular (através de um \input{q3.tex} em um main.tex). Portanto, NÃO inclua o preâmbulo (\documentclass, \begin{document}, \end{document}). Comece diretamente com \section*{Questão 03 - Busca Local em Problema das N-Rainhas}.

Aqui estão as regras estritas para a formatação do LaTeX:
1. Modularidade: O código deve estar pronto para ser colado no arquivo `q2.tex`.
2. Árvores e Grafos: Use o pacote `tikz` para desenhar a árvore parcial de busca solicitada. 
3. Destaque Visual (CRÍTICO): Ao desenhar as árvores ou listar as ordens de expansão, os nós que já foram VISITADOS/EXPANDIDOS devem obrigatoriamente estar em uma cor diferente (por exemplo, preenchidos com \node[fill=blue!20] no tikz ou usando \textcolor{blue}{Nó} no texto). Crie uma legenda rápida explicando a cor.
4. Tabelas: Reproduza as tabelas solicitadas usando o ambiente `table` e `tabular`, mantendo a formatação limpa.
5. Código Python: Todo o código autoral solicitado deve ser formatado usando o pacote `listings` (\begin{lstlisting}[language=Python]) ou `minted`, garantindo indentação correta.
6. Organização: Use \subsection*{} e \subsubsection*{} para separar claramente cada item da questão (Modelagem, Execução dos Algoritmos, Implementação e Experimento Adicional).

Abaixo está o texto da questão que você deve resolver e formatar:

[INÍCIO DO TEXTO DA QUESTÃO]
Considerar o problema das 8-Rainhas. O objetivo é posicionar 8 rainhas em um tabuleiro 8x8 de forma que nenhuma rainha ataque outra. Duas rainhas entram em conflito quando estão i) na mesma linha; ii) na mesma coluna; e iii) na mesma diagonal. Nesta atividade, cada estado será representado por um vetor:
[INÍCIO DA REPRESENTAÇÃO DO VETOR]
[s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8]
[FIM DA REPRESENTAÇÃO DO VETOR]

onde:

s_i = linha da rainha na coluna i

Exemplo:

[4, 2, 7, 3, 6, 8, 5, 1]

significa:
- coluna 1 -> linha 4;
- coluna 2 -> linha 2;

Iniciar a busca a partir do estado [1, 1, 1, 1, 1, 1, 1, 1]

Considerar a seguinte função heurística:

h(s) = número total de pares de rainhas em conflito
Objetivo: min h(s)
Um estado solução ocorre quando h(s) = 0
Modelar o problema como um problema de busca local. Apresentar:
a) representação do estado
b) definição de vizinho
c) função de avaliação
d) critério de parada
e) interpretação da superfície de busca

Em seguida, resolver o problema utilizando o algoritmo Hill-Climbing, onde um vizinho é obtido movendo exatamente UMA rainha para outra linha da mesma coluna. A solução deve apresentar:
a) estado atual;
b) todos os vizinhos avaliados em cada iteração;
c) valor de h(s) para cada vizinho;
d) estado escolhido;
e) explicação da escolha realizada;
f) número total de iterações;
g) estado final encontrado.

A resposta deve conter tabelas semelhantes ao modelo:
[INÍCIO DO MODELO DE TABELA]
Colunas: Iteração | Estado | h(s)
Linha: 0 | [1, 1, 1, 1, 1, 1, 1, 1] | 28
[FIM DO MODELO DE TABELA]
Além disso, para cada iteração, mostrar pelo menos os 5 melhores vizinhos gerados.

Durante a execução do Hill-Climbing, identificar se ocorreu máximo local, platô, pico estreito ou solução global. Caso algum desses itens ocorra, explicar:
a) por que ocorreu
b) como isso afetou a busca
c) como poderia ser evitado

Implementar uma versão com Random Restart Hill-Climbing
- Executar o algoritmo 20 vezes
- Cada execução deve iniciar em um estado aleatório
- Registrar:
    - número de passos
    - valor final de h(s)
    - se encontrou solução ou não

Apresentar a seguinte tabela
[INÍCIO DO MODELO DE TABELA]
Colunas: Execução | Estado inicial | Passos | h(s) final
[FIM DO MODELO DE TABELA]

Implementar o algoritmo Simulated Annealing usando a seguinte função de aceitação:

P = e ^ (-deltaE/T)
onde e = número de Euler
deltaE = aumento do número de conflitos
T = temperatura atual

Apresentar:
a) valor inicial da temperatura
b) política de resfriamento utilizada
c) exemplos de movimentos piores aceitos
d) comparação com Hill-Climbing simples
e) quantidade de soluções válidas encontradas

Implementar os algoritmos Hill-Climbing, Random Restart Hill-Climbing e Simulated Annealing em Python respeitando os seguintes critérios: Não utilizar bibliotecas externas.

Por fim, comparar os algoritmos considerando: a) qualidade das soluções; b) velocidade de convergência; c) sensibilidade ao estado incial; d) capacidade de escapar de máximos locais; e) custo computacional; f) estabilidade dos resultados.

[FIM DO TEXTO DA QUESTÃO]

Entregue o código LaTeX formatado, bem como os scripts do Python.