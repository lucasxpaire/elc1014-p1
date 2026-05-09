import random
import math

def h(state):
    """Calcula o número de pares de rainhas em conflito."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Conflito na mesma linha
            if state[i] == state[j]:
                conflicts += 1
            # Conflito na mesma diagonal
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(state):
    """Gera todos os vizinhos movendo uma rainha para outra linha na mesma coluna."""
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(1, 9):
            if state[col] != row:
                neighbor = list(state)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_state):
    """Executa o algoritmo Hill-Climbing."""
    current = initial_state
    current_h = h(current)
    
    iteration = 0
    print("=== Hill-Climbing ===")
    print(f"Iteração: {iteration} | Estado Atual: {current} | h(s): {current_h}")
    
    while True:
        neighbors = get_neighbors(current)
        # Avalia todos os vizinhos
        neighbors_eval = [(neighbor, h(neighbor)) for neighbor in neighbors]
        # Ordena para encontrar os melhores
        neighbors_eval.sort(key=lambda x: x[1])
        
        best_neighbor, best_h = neighbors_eval[0]
        
        print(f"\n--- Iteração {iteration + 1} ---")
        print("Top 5 vizinhos avaliados:")
        for i in range(5):
            print(f"{i+1}. Estado: {neighbors_eval[i][0]} | h(s): {neighbors_eval[i][1]}")
            
        if best_h >= current_h:
            print(f"\nParada: Melhor vizinho tem h(s) = {best_h}, que não é estritamente melhor que h(atual) = {current_h}.")
            if best_h == current_h:
                print("Motivo: Platô ou Ombro (Plateau / Shoulder) - Nenhuma melhoria estrita possível, mas existem estados iguais.")
            else:
                print("Motivo: Máximo/Mínimo Local - Todos os vizinhos são piores.")
            break
            
        print(f"Estado Escolhido: {best_neighbor} com h(s) = {best_h}")
        print("Explicação: Escolhido por ter o menor valor de pares em conflito entre todos os vizinhos.")
        
        current = best_neighbor
        current_h = best_h
        iteration += 1
        
    print(f"\nNúmero total de iterações (passos com melhoria): {iteration}")
    print(f"Estado final encontrado: {current} com h(s) = {current_h}")
    return current, current_h, iteration

def random_state():
    return [random.randint(1, 8) for _ in range(8)]

def random_restart_hill_climbing(restarts=20):
    print("\n=== Random Restart Hill-Climbing ===")
    print(f"{'Execução':<10} | {'Estado inicial':<30} | {'Passos':<8} | {'h(s) final':<10}")
    print("-" * 65)
    
    total_solutions = 0
    
    for i in range(1, restarts + 1):
        initial = random_state()
        
        current = initial
        current_h = h(current)
        steps = 0
        
        while True:
            neighbors = get_neighbors(current)
            best_neighbor = None
            best_h = current_h
            
            for neighbor in neighbors:
                nh = h(neighbor)
                if nh < best_h:
                    best_h = nh
                    best_neighbor = neighbor
                    
            if best_neighbor is None:
                break
                
            current = best_neighbor
            current_h = best_h
            steps += 1
            
        print(f"{i:<10} | {str(initial):<30} | {steps:<8} | {current_h:<10}")
        if current_h == 0:
            total_solutions += 1
            
    print(f"\nTotal de soluções globais válidas encontradas: {total_solutions} de {restarts}")

def simulated_annealing(initial_state, initial_temp=100.0, cooling_rate=0.99, max_iterations=10000):
    print("\n=== Simulated Annealing ===")
    print(f"Temperatura Inicial: {initial_temp}")
    print(f"Política de resfriamento: T = T * {cooling_rate} a cada iteração")
    
    current = initial_state
    current_h = h(current)
    best = current
    best_h = current_h
    
    T = initial_temp
    
    worse_accepted = []
    
    for t in range(max_iterations):
        if T < 1e-3 or current_h == 0:
            break
            
        neighbors = get_neighbors(current)
        next_state = random.choice(neighbors)
        next_h = h(next_state)
        
        deltaE = next_h - current_h
        
        if deltaE < 0:
            # Melhoria, aceita sempre
            current = next_state
            current_h = next_h
            if current_h < best_h:
                best = current
                best_h = current_h
        else:
            # Piora, aceita com probabilidade P
            prob = math.exp(-deltaE / T)
            if random.random() < prob:
                if len(worse_accepted) < 3:
                    worse_accepted.append((current_h, next_h, deltaE, prob, T))
                current = next_state
                current_h = next_h
                
        T *= cooling_rate
        
    print("\nExemplos de movimentos piores aceitos (Atual h -> Novo h, deltaE, Prob, Temp):")
    for ex in worse_accepted:
        print(f"h(s): {ex[0]} -> h(s'): {ex[1]} | deltaE: +{ex[2]} | P: {ex[3]:.4f} | T: {ex[4]:.2f}")
        
    print(f"\nEstado final encontrado: {best} com h(s) = {best_h}")
    return best, best_h

if __name__ == "__main__":
    initial_hc = [1, 1, 1, 1, 1, 1, 1, 1]
    hill_climbing(initial_hc)
    
    random.seed(42)  # Para reprodutibilidade
    random_restart_hill_climbing(20)
    
    print("\n--- Testando Simulated Annealing Múltiplas Vezes ---")
    sa_success = 0
    for i in range(20):
        _, h_val = simulated_annealing(random_state(), initial_temp=100.0, cooling_rate=0.99, max_iterations=10000)
        if h_val == 0:
            sa_success += 1
    print(f"\nQuantidade de soluções válidas encontradas pelo Simulated Annealing em 20 execuções: {sa_success}")
