# Prova 1 de IA 2026 - Transcricao (Extraida do PDF)

## Observacoes
- Esta versao foi extraida automaticamente do PDF e pode conter pequenos ruidos de layout/OCR.
- Para itens com tabela/figura (grafo, heuristicas e tabuleiro), use o PDF como referencia visual oficial.

===== PAGINA 1 =====

Questo 01 -Busca em amplitude/largura, Busca em profundidade e Busca iterativa em profundi dade Um agente deve se deslocar entre salas de um prdio. Cada sala  repre sentada por uma letra. As conexes representam movimentos permitidos entre salas. Todas as aes posSuen custo unitrio. A tabela abaixo apresenta o grafo do problema. Sala Salas vizinhas (ordem obrigatria) A B C D
H
EJ
I J
G M
K
B, C, D
L
E, F G, H
K, L
Estado inichal: A
N, O P
Estado objetivo: S Formula o problema acima como um problema de busca em espa Os de estados. A resposta deve couater: a) defii o fot thal do cst ao b) estado inicial; c) teste de objetivo; d) funo seoa, e) fursao de custo; ) representao scolhida en Python. En segukia, tesola o problema utilizando os seguintes algoritmus: 1. Busca em amplitude/largura (Breith-First Search): 2. Busca em profundidade (Depth-Firnt Search): 3. Busca iterativa en profundidade (Iterative Deepening Search). Para cada algoritmo, apresent ar: a) ordem completa de expanso dos ns;
Prova Inteligncia Artificial Prof. Lus Alvaro --luisalvaro0inf.uf sm. br -Maio 2026
b) contedo da fronteira aps cada expanso; c) rvore parcial de busca d) caminho soluo encontrado; e) profundidade da soluo;
2
f) custo da soluo; g) quantidade de ns gerados; h) quantidade de ns expandidos. Preencher uma tabela semelhante ao nodelo abaixO. Passo| N expandido| Contedo da fronteira |B,C,D| B
Implementar os trs algoritmos em Python respeitando os seguintes cri trios: NO utilizar bibliotecas externas, bibliotecas prontas de grafos e implernentaes encontradas na internet. 'Todo o cdigo deve ser autoral. Experimento adicional: modicar a ordem dos sucessores de exatamente dois ns do grafo. Exernplo:
 alterar:
para:
Aps a modificao, 1) executar novamente os trs algoritmos; 2) compa rar os resultados obtidos; e 3) analisar o impacto da ordem dos sucessores. Responder as seguintes questes: a) O caminho soluo mudou...
1/4
b) A quantidade de ns expandidos mudou... c) Algumn algoritmo foi mais sensvel  ordem dos sucessores... d) Qual algoritmo apresentou maior consumo de memria... e) Qual algoritmo encontrou a soluo mais rapidamente... Por fm, comparar os algoritmos considerando: a) completude; b) otima lidade; c) complexidade de tempo; d) complexidade de espao; e) depen dncia da ordem dos sucessores; f) comportanento erm rvores profundas; g) adequao para problemas grandes. Questo 02  Busca Gulosa pela Melhor Escolha e A* Considerar o seguinte problema de navegao em um ambiente parcial mente bloqueado: um agente deve sair da posio Ae alcanar a posio T. Cada aresta possui um custo associado. Alm disso, cada estado pos sui um valor heurstico h(n), que representa uma estimativa da distncia restante at o objetivo. O grafo do problema  apreserntado abaixo.
Estado inicial: A
Apresentar:
A No Sucessores (custo) h(n)
F H J
C:G,H
K
C: H,G
L
Estado objetivo: T
P
R
B(2), C(4), D(3) E(3), F(5) G(4), H(6)
e) custo final da soluo;
I(2) J(4) K(3), L(5)
a) ordem de expanso dos ns;
M(6) N(3), O(4) P(5) Q4) R(3) S(2) T(5)
T(4) T(3)
f(n) = h(n)
c) valores heursticos utilizados; b) contedo da fronteira aps cada expanso; d) caminho soluo encontrado;
10 8 7 9 6 5
7
Modelar o problema como un problena de busca em espao de estados. Apreserntar: a) representao dos estados; b) estado inicial: c) teste de objetivo; d) funo sucessora; e) funo de custo; f) interpreta co da heurstica h(n). Em seguida, resolver o problema manualmente usando o algoritmo Greedy Best-First Search utilizando o valor heu rstico:
5 3 3 4 8 2 1

===== PAGINA 2 =====

) quantidade de ns gerados; g) quantidade de ns expandidos. Resolver o mesno problema utilizando o algoritmo A* com:
onde:  gn): custo acumulado do caminho;  h(n): heurstica fornecida:  f(n): custo estimado total. Para cada expanso, apresentar: a) n expandido; b) valor de g(n); c) valor de h(n); d) valor de f(n); e) contebdo da fronteira ordenada:
f(n) = g(n) + h(n)
f) caminho parcial at o n. Preencher tabelas no seguinte formato: Passo| N6|g{n) h{n)| fin) 1
Implementar os algoritnos Busca Glosa peia Aeihor FExoAa e Busca A* em Python respeitando os seguintes cittim: NO utiluat bibicte cas externas, bibliotecas protitas de grafos e inlettsestaies etcontraias na internet, Todo o cdigo deve se sutoral
a) A soluo encontrada nudou...
Modificar os valores heursticos de exalamente trs ns do grasu Aps sso, 1) execute novamente os algortmos, 2) cxtpare os eeuitaos, e 3) analise o impacto da heuristica. Responder as seguintes questes: b) O custo da soluo mudou...
A B
d) O A* encont rou soluo otina... c) A busca gulosa encontrou solu o tittaa... e) Qual algoritmo expandiu henas ns ...
onde:
10
Exenplo:
) Qual algoritmo foi mais sensvel  heuristica...
signiica:
Por fim, comparar Greedy Best-First Searche A* onsiier ando: a) completude; b) otimalidade, c) consuno de nenria; d) dependncia da heurstica; e) custo comput acional; f) qualidade das solues; g) com portamento em grafos grandes.
10 10
Questo 03 -Busca Local em Problena das N Rainhas Considerar o problema das -Rainhas. O objetivo  posicionar 8 rai nhas em um tabuleiro 8 x 8 de forma que nenhuma rainha ataque outra. Duas rainhas entram em confito quando esto i) na mesma linha, ii) na mesma coluna e iii) na mesma diagonal. Nesta atividade, cada estado ser representado por um vetor:
 coluna 1  linha 4;  coluna 2  linha 2;
[S1, $2, $3, $4, 85, $6, 87, $8]
S; = linha da rainha na coluna 1
(4,2,7,3, 6, 8, 5, 1]
 coluna 8 linha 1 Iniciar a busca a partir do estado: [1, 1, 1, 1, 1, 1, 1, 1] Considerar a seguinte funo heurstica:
Objetivo:
2/4
h(s) = nmero total de pares de rainhas em conflito
Um estado soluo ocorre quando:
Modelar o problema como um problema de busca local. Apresen tar: a) representao do estado; b) defnio de vizinho; c) funo de avaliao; d) critrio de parada; e) interpretao da superficie de busca. Em seguida, resolver o problema manualmente utilizando o algoritmo Hill-Climbing, onde um vizinho  obtido movendo exatamente UMA rainha para outra linha da MESMA coluna. A soluo deve apresentar: a) estado atual; b) todos os vizinhos avaliados em cada iterao; d) estado escolhido; c) valor de h(s) para cada vizinho;
) nmero total de iteraes; e) explicao da escolha realizada; g) estado final encontrado. A tesponta deve conter tabelas semelhantes ao modelo:
min h(s)
Aln disao, para cada iterao, mostrar pelo menO8 Os 5 melhores vizi nhs gerados.
a) por que ocorreu;
Iterao| Estado |h(s) ||1,1,1,1,1,1,1,1|| 28
Duratste a execuao do Hill-Clinbing, identilicar se ocoreu mximo lo cal, plat, pico estreito ou soluo global. Caso algum desses itens ocorra, explicar: b) como isso afetou a busca;
h(s) = 0
e) cono poderia ser evitado. Inplernentar uma verso com Random Restart Hill-Clinbing;
 Registrar:  Executar o algoritmo 20 vezes;  Cada execuo deve iniciar em um estado aleatrio;
onde:
nmero de passOs; -valor final de hls): Apresentar a seguinte tabela: -se encontrou soluo ou no.
Execuo | Estado inicial | PassOs | h(s) final Implementar o algoritmo Simulated Annealing usando a seguinte fun o de aceitao:
 T: tenperatura atual.
P=e-AE/T  AE: aumento do nmero de conflitos;
..

===== PAGINA 3 =====

Apresentar: a) valor inicial da temperatura; b) poltica de resfriamento utilizada; c) exemplos de movimentos piores aceitos; d) comparao com Hill-Climbing simples: e) guantidade de solues vlidas encontradas. Implementar os algoritmos Hill-Climbing, Random Restart Hill-Climbing e Simulated Annealing em Python respeitando os seguintes critrios: NO utilizar bibliotecas externas, bibliotecas prontas de otimizao e implementaes encontradas na internet. Todo o cdigo deve ser auto ral. Por fm, comparar os algoritmos considerando: a) qualidade das solu ces; b) velocidade de convergncia; c) sensibilidade ao estado inicial: d) capacidade de escapar de mximos locais; e) custo computacional: f) estabilidade dos resultados. Questo 04  CSP e Otimizaes de Busca Um hospital precisa montar automaticamente a escala de plantes de um pequeno grupo de mdicos. Os turnos so:
Os mdicos disponveis so:
Cada turno deve possuir exatamente um mdico. Restries que devem ser consideradas: 1, O mesmo mdico NO pode trabalhar emn turnos consecutivos. 2. O mdico A no pode trabalhar em:
T1,T2, T3, T4, T5,T6
3. O mdico B deve trabalhar em pelo menos um turno entre:
{A, B,C, D}
4. O mdico C no pode trabalhar simultaneamente em:
a) rvore parcial da busca;
5. O mdico D pode trabalhar no mximo dois turnos.
c) conflitos encontrados; d) estados descartados;
Modelar o problema como um Constraint Satisfaction Problem (CSP). Apresentar: a) conjunto de variveis; b) domnio de cada va rivel; c) restries unrias; d) restries binrias; e) restries globais; f) representao do grafo de restries. Em seguida, resolver o problema manualmente utilizando Backtracking e apresentar:
e) retrocessos realizados:
b) ordem de atribuio das variveis;
Apresentar a tabela: f) soluo final encontrada.
2 3
T3
T1,T2
Passo | Varivel atribufda| Estado parcial T1-A T2--A
T2 e Ts
T2-B
b) por que ela foi escolhida,
Resolver o problena utilizando MRV (Minimum Remaining Va lues) e Degree Heuristic e explicar:
{Tl-A} conflito (T1-A,T2-B}
a) qual varivel foi escolhida erm cada passo; c) como MRV reduziu o espao de busca; d) cono Degree influenciou a busca.
Implementar Forward Checking e apresentar: a) reduo dos domnios aps cada atribuo; b) domnios elirminados; c) momento em que inconsistncias foram detectadas; d) comparao com backtracking simples. Implementar Backjurnping e apresentar: a) variveis responsveis pelos conflitos; b) saltos realizados; c) diferenas para backtracking tradicional; d) reduo observada na rvore de busca. Implementar os algoritmos Backtracking, Backtracking + MRV, Back tracking + MRV + Degree, Forward Checking e Backjumping em Python respeitando os seguintes critrios: NO utilizar bibliotecas externas, bi bliotecas prontas de CSP, OR-Tools e implementaes encontradas na internet. Todo o cdigo deve ser autoral. Por fim, comparar os algoritmos considerando: a) nmero de estados explorados; b) nmero de retrocessos; c) velocidade de execuo; d) con sumo de memria; e) facilidade de implernentao; f) eficincia prtica. Questo 05 -Minimax e Poda Alpha-Beta Considerar a seguinte rvore de jogo para um jogo determinstico de dois jogadores. O jogador MAX realiza a primeira jogada na raiz da rvore. Os valores nas folhas representam a utilidade final do jogo.
3/4
Os valores terminais so apresentados abaixo, da esquerda para a direita: [3, 5,6, 9, 1,2,0, -1, 7,4, 5, 6] A ordem de expanso dos filhos deve seguir obrigatoriamente da csquerda para a direita. Explicar: a) objetivo do algoritmo Minimax; b) diferena entre ns MAX e MIN; c) conceito de utilidade; d) propagao de valores na rvore; hiptese de adversrio perfeito; f) objetivo da poda Alpha-Beta. Executar passo a passo o algoritmo Minimax na rvore apresentada e apresentar: a) valores calculados em cada n; b) ordem de expanso; c) propagao dos valores; d) deciso tomada por MAX; e) caminho esco lhido pelo algoritmo; f) rvore parcialmente preenchida. Apresentar a tabela: Nj Tipo | Valor Minimax A |MAX| BMIN | CMAX| Executar a Poda Alpha-Beta utilizando a MESMA ordem de expan so. Apresentar: a) valores de ae Bem cada passo; b) monento em que ocorreran podas;
MIN
c) quais ramos foram podados; d) motivo matentico da poda; Apresentar a tabela: e) quantidade de ns NO explorados.

===== PAGINA 4 =====

Alterar a ordem de expanso dos filhos de forma a maximizar o nmero de podas. Em seguida, discutir: a) Quantas podas ocorreram antes... b) Quantas podas ocorreram depois...
Passo | N| a | 3| Poda...
c) Por que a nova ordem melhora a eficincia...
Responder:
d) Qual a relao entre ordenao e desempenho...
1
Considerar agora que a rvore  muito grande e que a busca deve parar na profundidade 2. Os seguintes valores heursticos devem ser usados nos ns no-terminais da profundidade limite:
a) executar Minimax limitado: b) utilizar os valores heursticos; c) comparar a deciso com Minimax completo:
decises.
d) discutir possveis erros causados pela heurstica.
(4,7,2, 5,6, 1]
Implementar os algoritmos Minimaz, Alpha-Beta e Minimar con pro fundidade limitada, em Python respeitando os seguints critrics: NO utilizar bibliotecas externas, bibliotecas pront.as de jogos, e implementa es encontradas na internet. Todo o odigo deve scr autoral. Comparar Minimax e Alpha-Beta considerando: a) nmeto de ns ex plorados; b) quantidade de podas; c) custo compautaciosal, d) couno de memria; e) impacto da ordenao dos movinentos; f) qualkiacje das Em um experimento adicional, modificar os valores de exatamente 3 f Ihas da rvore, Aps isso: 1, executar novamente Mininax; 2. executar novamente Alpha-Beta; 3. verificar se a deciso final mudou;
no sim
4. analisar a sensibilidade do algoritmo s utilidades.
a) seleo;
Questo 06-Monte Carlo Tree Search (MCTS) Considerar o jogo Connect-4 simplificado abaixo. O jogador vernelho deve decidir qual coluna jogar. O estado atual :
b) expanso;
Legenda: V: vermelho e A: amarelo. As aes possveis so:
c) simulao (rollout); d) retropropagao.
Para MCST, explicar detalhadamente:
Explicar tambm:
A
C1, C2, C3, C4
e) papel do nmero de visitas:
4/4
f) papel do nmero de vitrias; g) diferena entre explorao e explotao. Executar 10 iteracs do algoritmo MCTS. Em cada iterao apresentar: a) caminho selecionado; b) n expandido; c) resultado do rollout; d) atualizao de: e) rvore parcial construda. Utilizar:
Com:
e calcular:
UCTU) = +Cn
a) valor de UCT para cada ilho; b) n selecionado; c) intuencia do termo de explorao; d) influncia do ternmo de explotao. Apresentar a seguinte tabela:
cl c2 Jogada| Visitas| Vitrias| UCT
c3
a) quanticdade de explorao; b) diversidade de jogadas; c) estabilidade das decises;
N(s), W(s)
C=l4
Executar novanente o algoritno utilizando C= (0.1 e depois C= 3.0 e cotnpaar:
e cornparar:
3
2. rollout semi-guloso:
n
5
d) qualidade das jogadas encontradas. Implementar dois tipos de rollout: 1. rollout totalnente aleatrio;
a) qualidade das decises;
 priorizar jogadas centrais;  bloquear vitria imediata do adversrio.
b) velocidade de convergncia; c) nmero de simulaes necessrias. Implementar seleo, erpanso, rollout, retropropagao e clculo de UCT em Python respeitando os seguintes critrios: NO utilizar bi bliotecas externas, bibliotecas prontas de jogos e implementaes encon tradas na internet. Todo o cdigo deve ser autoral. Por fim, comparar: a) rollout aleatrio vs semi-guloso; b) diferentes va lores de C; c) nmero de iteraes; d) estabilidade das decises.
