import heapq

class Graph:
    def __init__(self):
        self.nodes = {}
        self.heuristics = {}

    def add_node(self, name, successors, h):
        self.nodes[name] = successors
        self.heuristics[name] = h

def get_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        for neighbor, cost in graph.nodes[path[i]]:
            if neighbor == path[i+1]:
                total_cost += cost
                break
    return total_cost

def greedy_best_first_search(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (graph.heuristics[start], start))
    came_from = {}
    expanded = []
    generated_count = 1
    
    while frontier:
        h_val, current = heapq.heappop(frontier)
        expanded.append(current)
        
        if current == goal:
            path = get_path(came_from, current)
            cost = calculate_path_cost(graph, path)
            return path, cost, expanded, generated_count

        for neighbor, cost in graph.nodes.get(current, []):
            if neighbor not in expanded and not any(neighbor == n for h, n in frontier):
                generated_count += 1
                came_from[neighbor] = current
                heapq.heappush(frontier, (graph.heuristics[neighbor], neighbor))
    return None

def a_star_search(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (graph.heuristics[start], start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: graph.heuristics[start]}
    expanded = []
    generated_count = 1
    
    while frontier:
        f_val, current = heapq.heappop(frontier)
        expanded.append(current)
        
        if current == goal:
            path = get_path(came_from, current)
            return path, g_score[current], expanded, generated_count

        for neighbor, cost in graph.nodes.get(current, []):
            tentative_g_score = g_score[current] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                generated_count += 1
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + graph.heuristics[neighbor]
                if not any(neighbor == n for f, n in frontier):
                    heapq.heappush(frontier, (f_score[neighbor], neighbor))
    return None

def main():
    # Original Heuristics
    # A:10, B:8, C:7, D:9, E:6, F:5, G:6, H:4, I:7, J:5, K:3, L:6, M:3, N:4, O:1, P:8, Q:4, R:2, S:1, T:0
    
    # Modified Heuristics: D:1, I:0, B:20
    h_mod = {
        'A':10, 'B':20, 'C':7, 'D':1, 'E':6, 'F':5, 'G':6, 'H':4, 'I':0, 'J':5, 'K':3, 'L':6, 'M':3, 'N':4, 'O':1, 'P':8, 'Q':4, 'R':2, 'S':1, 'T':0
    }
    
    g = Graph()
    nodes_data = {
        'A': [('B', 2), ('C', 4), ('D', 3)],
        'B': [('E', 3), ('F', 5)],
        'C': [('G', 4), ('H', 6)],
        'D': [('I', 2)],
        'E': [('J', 4)],
        'F': [('K', 3), ('L', 5)],
        'G': [('M', 6)],
        'H': [('N', 3), ('O', 4)],
        'I': [('P', 5)],
        'J': [('Q', 4)],
        'K': [('R', 3)],
        'L': [],
        'M': [('S', 2)],
        'H': [('N', 3), ('O', 4)],
        'O': [('T', 5)],
        'P': [], 'Q': [], 'R': [('T', 4)], 'S': [('T', 3)], 'T': [],
        'N': []
    }
    
    # Fill graph with modified heuristics
    for node, successors in nodes_data.items():
        g.add_node(node, successors, h_mod[node])

    # Re-run algorithms
    print("--- Experimento: Heursticas Modificadas (D:1, I:0, B:20) ---")
    
    res_g = greedy_best_first_search(g, 'A', 'T')
    if res_g:
        path, cost, expanded, gen = res_g
        print(f"\nGreedy (Modificado):")
        print(f"Caminho: {' -> '.join(path)}")
        print(f"Custo: {cost}")
        print(f"Expandidos: {len(expanded)} ({', '.join(expanded)})")
    
    res_a = a_star_search(g, 'A', 'T')
    if res_a:
        path, cost, expanded, gen = res_a
        print(f"\nA* (Modificado):")
        print(f"Caminho: {' -> '.join(path)}")
        print(f"Custo: {cost}")
        print(f"Expandidos: {len(expanded)} ({', '.join(expanded)})")

if __name__ == "__main__":
    main()
