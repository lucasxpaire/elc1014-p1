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

def greedy_best_first_search(graph, start, goal):
    print("\n--- Greedy Best-First Search ---")
    frontier = []
    # Priority queue: (h, name)
    heapq.heappush(frontier, (graph.heuristics[start], start))
    came_from = {}
    expanded = []
    generated_count = 1
    
    step = 0
    while frontier:
        step += 1
        h_val, current = heapq.heappop(frontier)
        expanded.append(current)
        
        # Current frontier before expanding (for display)
        frontier_display = [(n, graph.heuristics[n]) for h, n in frontier]
        
        if current == goal:
            path = get_path(came_from, current)
            cost = calculate_path_cost(graph, path)
            print(f"Passo: {step} | Expandido: {current} | Fronteira: {frontier_display}")
            return path, cost, expanded, generated_count

        for neighbor, cost in graph.nodes.get(current, []):
            if neighbor not in expanded and not any(neighbor == n for h, n in frontier):
                generated_count += 1
                came_from[neighbor] = current
                heapq.heappush(frontier, (graph.heuristics[neighbor], neighbor))
        
        print(f"Passo: {step} | Expandido: {current} | Fronteira: {[(n, graph.heuristics[n]) for h, n in frontier]}")

def a_star_search(graph, start, goal):
    print("\n--- A* Search ---")
    # Priority queue: (f, name)
    frontier = []
    heapq.heappush(frontier, (graph.heuristics[start], start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: graph.heuristics[start]}
    
    expanded = []
    generated_count = 1
    
    step = 0
    while frontier:
        step += 1
        f_val, current = heapq.heappop(frontier)
        expanded.append(current)
        
        if current == goal:
            path = get_path(came_from, current)
            print(f"Passo: {step} | Nó: {current} | g: {g_score[current]} | h: {graph.heuristics[current]} | f: {f_score[current]} | Fronteira: {[(n, f_score[n]) for f, n in frontier]}")
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
        
        print(f"Passo: {step} | Nó: {current} | g: {g_score[current]} | h: {graph.heuristics[current]} | f: {f_score[current]} | Fronteira: {sorted([(n, f_score[n]) for f, n in frontier], key=lambda x: x[1])}")

def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        for neighbor, cost in graph.nodes[path[i]]:
            if neighbor == path[i+1]:
                total_cost += cost
                break
    return total_cost

def main():
    g = Graph()
    g.add_node('A', [('B', 2), ('C', 4), ('D', 3)], 10)
    g.add_node('B', [('E', 3), ('F', 5)], 8)
    g.add_node('C', [('G', 4), ('H', 6)], 7)
    g.add_node('D', [('I', 2)], 9)
    g.add_node('E', [('J', 4)], 6)
    g.add_node('F', [('K', 3), ('L', 5)], 5)
    g.add_node('G', [('M', 6)], 6)
    g.add_node('H', [('N', 3), ('O', 4)], 4)
    g.add_node('I', [('P', 5)], 7)
    g.add_node('J', [('Q', 4)], 5)
    g.add_node('K', [('R', 3)], 3)
    g.add_node('L', [], 6)
    g.add_node('M', [('S', 2)], 3)
    g.add_node('N', [], 4)
    g.add_node('O', [('T', 5)], 1)
    g.add_node('P', [], 8)
    g.add_node('Q', [], 4)
    g.add_node('R', [('T', 4)], 2)
    g.add_node('S', [('T', 3)], 1)
    g.add_node('T', [], 0)

    # Greedy
    path_g, cost_g, expanded_g, gen_g = greedy_best_first_search(g, 'A', 'T')
    print(f"\nResultado Greedy:")
    print(f"Caminho: {' -> '.join(path_g)}")
    print(f"Custo: {cost_g}")
    print(f"Expandidos: {len(expanded_g)} ({', '.join(expanded_g)})")
    print(f"Gerados: {gen_g}")

    # A*
    path_a, cost_a, expanded_a, gen_a = a_star_search(g, 'A', 'T')
    print(f"\nResultado A*:")
    print(f"Caminho: {' -> '.join(path_a)}")
    print(f"Custo: {cost_a}")
    print(f"Expandidos: {len(expanded_a)} ({', '.join(expanded_a)})")
    print(f"Gerados: {gen_a}")

if __name__ == "__main__":
    main()
