class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

def bfs(graph, initial_state, goal_state):
    node = Node(initial_state)
    if node.state == goal_state:
        return node, 0, 1
    
    frontier = [node]
    frontier_states = [initial_state]
    explored = set()
    
    nodes_generated = 1
    nodes_expanded = 0
    
    step = 1
    print("\n--- BFS ---")
    
    while frontier:
        node = frontier.pop(0)
        frontier_states.pop(0)
        explored.add(node.state)
        
        print(f"Passo: {step} | Nó Expandido: {node.state} | Fronteira após expansão: {frontier_states}")
        step += 1
        nodes_expanded += 1
        
        for action in graph.get(node.state, []):
            child_state = action
            child = Node(child_state, node, action, node.path_cost + 1, node.depth + 1)
            nodes_generated += 1
            
            if child_state not in explored and child_state not in frontier_states:
                if child_state == goal_state:
                    print(f"Passo: {step} | Nó Gerado e Alcançado: {child_state} (Objetivo)")
                    return child, nodes_expanded, nodes_generated
                frontier.append(child)
                frontier_states.append(child_state)

    return None, nodes_expanded, nodes_generated

def dfs(graph, initial_state, goal_state):
    node = Node(initial_state)
    frontier = [node]
    frontier_states = [initial_state]
    explored = set()
    
    nodes_generated = 1
    nodes_expanded = 0
    
    step = 1
    print("\n--- DFS ---")
    
    while frontier:
        node = frontier.pop() # LIFO
        frontier_states.pop()
        
        if node.state == goal_state:
            print(f"Passo: {step} | Nó Expandido: {node.state} (Objetivo Alcançado)")
            return node, nodes_expanded, nodes_generated
            
        explored.add(node.state)
        
        print(f"Passo: {step} | Nó Expandido: {node.state} | Fronteira (antes de adicionar sucessores): {frontier_states}")
        step += 1
        nodes_expanded += 1
        
        # Inserindo os nós na ordem reversa na pilha para que sejam visitados na ordem correta
        for action in reversed(graph.get(node.state, [])):
            child_state = action
            child = Node(child_state, node, action, node.path_cost + 1, node.depth + 1)
            nodes_generated += 1
            
            # Busca em grafo para evitar ciclos
            if child_state not in explored and child_state not in frontier_states:
                frontier.append(child)
                frontier_states.append(child_state)
                
        print(f"    Fronteira após adicionar sucessores: {frontier_states}")

    return None, nodes_expanded, nodes_generated


def dls(graph, initial_state, goal_state, limit):
    node = Node(initial_state)
    frontier = [node]
    frontier_states = [initial_state]
    
    # Em busca de profundidade iterativa, tipicamente usamos busca em árvore para completude em espaços cíclicos limitados,
    # ou podemos usar um explored set sensível à profundidade. 
    # Aqui, para árvores, simplificaremos, mas como é grafo e não queremos loops, controlamos o caminho.
    
    nodes_generated = 1
    nodes_expanded = 0
    
    step = 1
    print(f"\n--- DLS (Limit={limit}) ---")
    
    while frontier:
        node = frontier.pop()
        frontier_states.pop()
        
        if node.state == goal_state:
            print(f"Passo: {step} | Nó Expandido: {node.state} (Objetivo Alcançado)")
            return node, nodes_expanded, nodes_generated, "solution"
            
        print(f"Passo: {step} | Nó Expandido: {node.state} | Profundidade: {node.depth}")
        step += 1
        
        if node.depth < limit:
            nodes_expanded += 1
            for action in reversed(graph.get(node.state, [])):
                child_state = action
                # Evitando loops no mesmo caminho (busca em árvore com verificação de caminho)
                path = []
                curr = node
                while curr:
                    path.append(curr.state)
                    curr = curr.parent
                
                if child_state not in path:
                    child = Node(child_state, node, action, node.path_cost + 1, node.depth + 1)
                    nodes_generated += 1
                    frontier.append(child)
                    frontier_states.append(child_state)
            print(f"    Fronteira após expansão: {frontier_states}")
        else:
            print(f"    Nó atingiu limite de profundidade. Fronteira: {frontier_states}")

    return None, nodes_expanded, nodes_generated, "cutoff"

def ids(graph, initial_state, goal_state):
    total_nodes_expanded = 0
    total_nodes_generated = 0
    depth = 0
    print("\n--- IDS ---")
    while True:
        result, expanded, generated, status = dls(graph, initial_state, goal_state, depth)
        total_nodes_expanded += expanded
        total_nodes_generated += generated
        if status == "solution":
            return result, total_nodes_expanded, total_nodes_generated
        depth += 1

def print_solution(node):
    if not node:
        print("Nenhuma solução encontrada.")
        return
    path = []
    curr = node
    while curr:
        path.append(curr.state)
        curr = curr.parent
    path.reverse()
    print(f"Caminho Solução: {' -> '.join(path)}")
    print(f"Custo: {node.path_cost}")
    print(f"Profundidade: {node.depth}")

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G', 'H'],
        'D': ['I'],
        'E': ['J'],
        'F': ['K', 'L'],
        'G': ['M'],
        'H': ['N', 'O'],
        'I': ['P'],
        'J': [],
        'K': ['Q'],
        'L': [],
        'M': ['R'],
        'N': [],
        'O': ['S'],
        'P': [],
        'Q': [],
        'R': [],
        'S': []
    }
    
    initial_state = 'A'
    goal_state = 'S'
    
    print("================== BFS ==================")
    sol_bfs, exp_bfs, gen_bfs = bfs(graph, initial_state, goal_state)
    print_solution(sol_bfs)
    print(f"Nós Expandidos: {exp_bfs}")
    print(f"Nós Gerados: {gen_bfs}")
    
    print("\n================== DFS ==================")
    sol_dfs, exp_dfs, gen_dfs = dfs(graph, initial_state, goal_state)
    print_solution(sol_dfs)
    print(f"Nós Expandidos: {exp_dfs}")
    print(f"Nós Gerados: {gen_dfs}")
    
    print("\n================== IDS ==================")
    sol_ids, exp_ids, gen_ids = ids(graph, initial_state, goal_state)
    print_solution(sol_ids)
    print(f"Nós Expandidos: {exp_ids}")
    print(f"Nós Gerados: {gen_ids}")
