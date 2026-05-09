import math
import copy

class Node:
    def __init__(self, name, node_type, children=None, value=None):
        self.name = name
        self.node_type = node_type # 'MAX' ou 'MIN'
        self.children = children if children else []
        self.value = value

def build_tree(leaves):
    # leaves = [3, 5, 6, 9, 1, 2, 0, -1, 7, 4, 5, 6]
    C = Node('C', 'MAX', [Node('L1', 'LEAF', value=leaves[0]), Node('L2', 'LEAF', value=leaves[1])])
    D = Node('D', 'MAX', [Node('L3', 'LEAF', value=leaves[2]), Node('L4', 'LEAF', value=leaves[3])])
    B = Node('B', 'MIN', [C, D])
    
    F = Node('F', 'MAX', [Node('L5', 'LEAF', value=leaves[4]), Node('L6', 'LEAF', value=leaves[5])])
    G = Node('G', 'MAX', [Node('L7', 'LEAF', value=leaves[6]), Node('L8', 'LEAF', value=leaves[7])])
    E = Node('E', 'MIN', [F, G])
    
    I = Node('I', 'MAX', [Node('L9', 'LEAF', value=leaves[8]), Node('L10', 'LEAF', value=leaves[9])])
    J = Node('J', 'MAX', [Node('L11', 'LEAF', value=leaves[10]), Node('L12', 'LEAF', value=leaves[11])])
    H = Node('H', 'MIN', [I, J])
    
    A = Node('A', 'MAX', [B, E, H])
    return A

# --- MINIMAX ---
minimax_trace = []
mm_nodes_explored = 0

def minimax(node):
    global mm_nodes_explored
    mm_nodes_explored += 1
    
    if node.node_type == 'LEAF':
        return node.value
        
    if node.node_type == 'MAX':
        best_val = -math.inf
        for child in node.children:
            val = minimax(child)
            if val > best_val:
                best_val = val
        minimax_trace.append((node.name, node.node_type, best_val))
        return best_val
    else:
        best_val = math.inf
        for child in node.children:
            val = minimax(child)
            if val < best_val:
                best_val = val
        minimax_trace.append((node.name, node.node_type, best_val))
        return best_val

# --- ALPHA-BETA ---
ab_trace = []
ab_nodes_explored = 0
ab_prunings = 0

def alpha_beta(node, alpha, beta, step_ref):
    global ab_nodes_explored, ab_prunings
    ab_nodes_explored += 1
    
    if node.node_type == 'LEAF':
        return node.value
        
    if node.node_type == 'MAX':
        best_val = -math.inf
        for child in node.children:
            val = alpha_beta(child, alpha, beta, step_ref)
            best_val = max(best_val, val)
            
            # Log antes de possivelmente podar
            step_ref[0] += 1
            alpha = max(alpha, best_val)
            pruned = "sim" if best_val >= beta else "não"
            ab_trace.append((step_ref[0], node.name, alpha, beta, pruned))
            
            if best_val >= beta:
                ab_prunings += 1
                break
        return best_val
    else:
        best_val = math.inf
        for child in node.children:
            val = alpha_beta(child, alpha, beta, step_ref)
            best_val = min(best_val, val)
            
            step_ref[0] += 1
            beta = min(beta, best_val)
            pruned = "sim" if best_val <= alpha else "não"
            ab_trace.append((step_ref[0], node.name, alpha, beta, pruned))
            
            if best_val <= alpha:
                ab_prunings += 1
                break
        return best_val

# --- MINIMAX PROFUNDIDADE LIMITADA ---
def minimax_limitado(node, depth, current_depth, heuristics):
    if node.node_type == 'LEAF':
        return node.value # Na prática não deve chegar aqui se cortado antes
        
    if current_depth == depth:
        # Pega a heurística do nó
        return heuristics[node.name]
        
    if node.node_type == 'MAX':
        best_val = -math.inf
        for child in node.children:
            val = minimax_limitado(child, depth, current_depth + 1, heuristics)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = math.inf
        for child in node.children:
            val = minimax_limitado(child, depth, current_depth + 1, heuristics)
            best_val = min(best_val, val)
        return best_val


if __name__ == "__main__":
    leaves = [3, 5, 6, 9, 1, 2, 0, -1, 7, 4, 5, 6]
    
    # 1. MINIMAX
    tree1 = build_tree(leaves)
    res_mm = minimax(tree1)
    print("=== MINIMAX ===")
    print(f"Resultado Raiz: {res_mm}")
    print(f"Nós Explorados: {mm_nodes_explored}")
    print("Trace Minimax (Nó, Tipo, Valor):")
    for t in minimax_trace:
        print(t)
        
    # 2. ALPHA-BETA
    tree2 = build_tree(leaves)
    step = [0]
    res_ab = alpha_beta(tree2, -math.inf, math.inf, step)
    print("\n=== ALPHA-BETA ===")
    print(f"Resultado Raiz: {res_ab}")
    print(f"Nós Explorados: {ab_nodes_explored}")
    print(f"Podas: {ab_prunings}")
    print("Trace Alpha-Beta (Passo, Nó, alpha, beta, Poda):")
    for t in ab_trace:
        print(t)
        
    # 3. PROFUNDIDADE LIMITADA
    tree3 = build_tree(leaves)
    # Valores heurísticos para [B, E, H, C, D, F, G, I, J]...
    # A questão diz: "nos nós não-terminais da profundidade limite: [4,7,2,5,6,1]"
    # Nível 0 = A, Nível 1 = B,E,H, Nível 2 = C,D,F,G,I,J (os 6 nós MAX)
    # Então profundidade limite 2 significa parar nos 6 nós MAX e usar a heurística.
    # [C=4, D=7, F=2, G=5, I=6, J=1]
    heuristics = {'C': 4, 'D': 7, 'F': 2, 'G': 5, 'I': 6, 'J': 1}
    res_limitado = minimax_limitado(tree3, depth=2, current_depth=0, heuristics=heuristics)
    print("\n=== MINIMAX LIMITADO ===")
    print(f"Resultado Raiz (Profundidade 2): {res_limitado}")
    
    # 4. ORDENAÇÃO IDEAL
    print("\n=== ALPHA-BETA (ORDENAÇÃO IDEAL) ===")
    # Construindo a árvore com a melhor ordem:
    # A -> H(J(6,5), I(7,4)), B(C(5,3), D(9,6)), E(G(0,-1), F(2,1))
    # Para as folhas mudamos a ordem para refletir o maior primeiro nos nós MAX
    J_opt = Node('J', 'MAX', [Node('L12', 'LEAF', value=6), Node('L11', 'LEAF', value=5)])
    I_opt = Node('I', 'MAX', [Node('L9', 'LEAF', value=7), Node('L10', 'LEAF', value=4)])
    H_opt = Node('H', 'MIN', [J_opt, I_opt])
    
    C_opt = Node('C', 'MAX', [Node('L2', 'LEAF', value=5), Node('L1', 'LEAF', value=3)])
    D_opt = Node('D', 'MAX', [Node('L4', 'LEAF', value=9), Node('L3', 'LEAF', value=6)])
    B_opt = Node('B', 'MIN', [C_opt, D_opt])
    
    G_opt = Node('G', 'MAX', [Node('L7', 'LEAF', value=0), Node('L8', 'LEAF', value=-1)])
    F_opt = Node('F', 'MAX', [Node('L6', 'LEAF', value=2), Node('L5', 'LEAF', value=1)])
    E_opt = Node('E', 'MIN', [G_opt, F_opt])
    
    A_opt = Node('A', 'MAX', [H_opt, B_opt, E_opt])
    
    ab_trace.clear()
    ab_nodes_explored = 0
    ab_prunings = 0
    step[0] = 0
    res_opt = alpha_beta(A_opt, -math.inf, math.inf, step)
    print(f"Resultado Raiz: {res_opt}")
    print(f"Nós Explorados: {ab_nodes_explored}")
    print(f"Podas: {ab_prunings}")
    print("Trace Alpha-Beta (Ordenação Ideal):")
    for t in ab_trace:
        print(t)
        
    # 5. EXPERIMENTO (Mudar 3 folhas)
    print("\n=== EXPERIMENTO ===")
    leaves_exp = [3, 5, 6, 9, 10, 15, 0, -1, -5, 4, 5, 6]
    tree_exp1 = build_tree(leaves_exp)
    mm_trace = minimax_trace.copy()
    minimax_trace.clear()
    mm_nodes_explored = 0
    res_exp_mm = minimax(tree_exp1)
    print(f"Novo Resultado Minimax: {res_exp_mm}")
    print("Trace Minimax Experimento:")
    for t in minimax_trace:
        print(t)
        
    tree_exp2 = build_tree(leaves_exp)
    ab_trace.clear()
    ab_nodes_explored = 0
    ab_prunings = 0
    step[0] = 0
    res_exp_ab = alpha_beta(tree_exp2, -math.inf, math.inf, step)
    print(f"\nNovo Resultado Alpha-Beta: {res_exp_ab}")
    print("Trace Alpha-Beta Experimento:")
    for t in ab_trace:
        print(t)
