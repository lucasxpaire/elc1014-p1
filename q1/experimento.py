import copy
from busca import bfs, dfs, ids, print_solution

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['H', 'G'], # Modified here: C -> H, G
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
    
    print("EXPERIMENTO COM ORDEM C -> H, G")
    
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
