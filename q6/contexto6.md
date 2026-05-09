Atue como um especialista em Inteligência Artificial e LaTeX. Sua tarefa é resolver a "Questão 06" de uma prova de IA e formatar a resposta inteiramente em código LaTeX.

O código gerado será incluído em um projeto modular (através de um \input{q6.tex} em um main.tex). Portanto, NÃO inclua o preâmbulo (\documentclass, \begin{document}, \end{document}). Comece diretamente com \section*{Questão 06 - Monte Carlo Tree Search (MCTS)}.

Aqui estão as regras estritas para a formatação do LaTeX:
1. Modularidade: O código deve estar pronto para ser colado no arquivo `q6.tex`.
2. Tabelas: Reproduza as tabelas de iterações e o tabuleiro usando o ambiente `table` e `tabular`.
3. Destaque Visual: No tabuleiro, destaque a última jogada ou peças vencedoras se necessário.
4. Fórmulas: Use o ambiente matemático para demonstrar o cálculo do UCT: $UCT = \frac{w_i}{n_i} + C \sqrt{\frac{\ln N}{n_i}}$.
5. Código Python: Todo o código autoral solicitado deve ser formatado usando o pacote `listings`.

Abaixo está o texto da questão e os dados do problema:

[INÍCIO DO TEXTO DA QUESTÃO]
Considerar o jogo Connect-4 simplificado. O jogador Vermelho (V) deve decidir qual coluna jogar. O estado atual é:

|   |   | | | 
|   |   | | |
| A | V | | |
| V | A | | |
|   | | | | |

Legenda V: vermelho e A: amarelo. As ações possíveis são: c1, c2, c3 e c4

Para MCST, explicar detalhadamento:

a) seleção;
b) expansão;
c) simulação (rollout);
d) retropropagação.

Explicar também:
e) papel do número de visitas;
f) papel do número de vitórias;
g) diferença entre exploração e explotação.
Executar 10 iteraçõcs do algoritmo MCTS. Em cada iteraçåo apresentar:
a) caminho selecionado;
b) nó expandido;
c) resultado do rollout;
d) atualização de: N(s), W(s)
e) árvore parcial construída.

Utilizar:
UCT(j) = (wj / nj) + C * sqrt(ln N / nj)
com:
C = 1.4
e calcular:
a) valor de UCT para cada ilho;
b) nỏ selecionado;
c) intuencia do termo de exploração;
d) influềncia do ternmo de explotação.
Apresentar a seguinte tabela:
| Jogada | Visitas | Vitórias | UCT |
| c1 | 3 | 2 | ...
| c2 | 5 | 4 | ...
| c5 | 1 | 1 | ...

Executar novanente o algoritno utilizando C= (0.1 e depois C= 3.0 e comparar:

a) quanticdade de exploração;
b) diversidade de jogadas;
c) estabilidade das decisões;
d) qualidade das jogadas encontradas.

Implementar dois tipos de rollout:

1. rollout totalnente aleatório;
2. rollout semi-guloso:
    • priorizar jogadas centrais;
    • bloquear vitória imediata do adversário.
e comparar:
a) qualidade das decisões;
b) velocidade de convergência;
c) número de simulações necessárias.

Implementar seleção, erpansão, rollout, retropropagação e cálculo de
UCT em Python respeitando os seguintes critérios: NÃO utilizar bi
bliotecas externas, bibliotecas prontas de jogos e implementações encon
tradas na internet. Todo o código deve ser autoral.
Por fim, comparar: a) rollout aleatório vs semi-guloso; b) diferentes va
lores de C; c) número de iterações; d) estabilidade das decisöes

[FIM DO TEXTO DA QUESTÃO]
