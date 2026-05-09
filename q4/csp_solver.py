import copy

VARIABLES = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
DOMAINS = {v: ['A', 'B', 'C', 'D'] for v in VARIABLES}

def is_consistent(var, val, assignment):
    # Verifica regras unárias, binárias e globais para uma atribuição proposta
    # 2. A não pode trabalhar em T3
    if var == 'T3' and val == 'A':
        return False
        
    temp_assignment = assignment.copy()
    temp_assignment[var] = val
    
    # 1. Não pode trabalhar em turnos consecutivos
    for i in range(1, 6):
        t_curr = f"T{i}"
        t_next = f"T{i+1}"
        if t_curr in temp_assignment and t_next in temp_assignment:
            if temp_assignment[t_curr] == temp_assignment[t_next]:
                return False
                
    # 3. B deve trabalhar em pelo menos um turno entre T1 e T2
    if 'T1' in temp_assignment and 'T2' in temp_assignment:
        if temp_assignment['T1'] != 'B' and temp_assignment['T2'] != 'B':
            return False
            
    # 4. C não pode trabalhar simultaneamente em T2 e T5
    if 'T2' in temp_assignment and 'T5' in temp_assignment:
        if temp_assignment['T2'] == 'C' and temp_assignment['T5'] == 'C':
            return False
            
    # 5. D pode trabalhar no máximo em dois turnos
    count_d = list(temp_assignment.values()).count('D')
    if count_d > 2:
        return False
        
    return True

# --- BACKTRACKING SIMPLES ---
bt_trace = []
bt_states_explored = 0
bt_backtracks = 0

def format_assignment(assignment):
    return "{" + ", ".join([f"{k}={v}" for k, v in assignment.items()]) + "}"

def backtracking(assignment):
    global bt_states_explored, bt_backtracks
    
    if len(assignment) == len(VARIABLES):
        return assignment
        
    unassigned = [v for v in VARIABLES if v not in assignment]
    var = unassigned[0] # Escolha estática
    
    for val in DOMAINS[var]:
        bt_states_explored += 1
        step = len(bt_trace) + 1
        
        if is_consistent(var, val, assignment):
            bt_trace.append((step, f"{var} = {val}", format_assignment({**assignment, var: val})))
            assignment[var] = val
            result = backtracking(assignment)
            if result:
                return result
            # Backtrack
            del assignment[var]
            bt_backtracks += 1
            # O log do backtrack costuma ser capturado quando voltamos, 
            # mas para a tabela focamos nas atribuições
        else:
            bt_trace.append((step, f"{var} = {val}", "conflito"))
            
    return None

# --- MRV + DEGREE HEURISTIC ---
def get_mrv_degree_var(assignment, current_domains):
    unassigned = [v for v in VARIABLES if v not in assignment]
    
    # 1. MRV
    mrv_val = min(len(current_domains[v]) for v in unassigned)
    mrv_vars = [v for v in unassigned if len(current_domains[v]) == mrv_val]
    
    if len(mrv_vars) == 1:
        return mrv_vars[0], "MRV"
        
    # 2. Degree Heuristic (nó com mais restrições sobre outras variáveis não atribuídas)
    # Grafo de restrições de T:
    # Consecutivos: T1-T2, T2-T3, T3-T4, T4-T5, T5-T6
    # Especiais: T1-T2 (já coberto), T2-T5 (C não pode em ambos)
    # Global D: Todos conectados a todos, mas tradicionalmente consideramos restrições binárias explícitas.
    # Vamos contar arestas explícitas (consecutivos + T2-T5)
    edges = {
        'T1': ['T2'],
        'T2': ['T1', 'T3', 'T5'],
        'T3': ['T2', 'T4'],
        'T4': ['T3', 'T5'],
        'T5': ['T4', 'T6', 'T2'],
        'T6': ['T5']
    }
    
    max_degree = -1
    best_var = None
    for v in mrv_vars:
        degree = sum(1 for neighbor in edges[v] if neighbor not in assignment)
        if degree > max_degree:
            max_degree = degree
            best_var = v
            
    return best_var, "Degree"

def update_domains_fc(var, val, assignment, current_domains):
    new_domains = copy.deepcopy(current_domains)
    new_domains[var] = [val]
    
    unassigned = [v for v in VARIABLES if v not in assignment and v != var]
    temp_assignment = assignment.copy()
    temp_assignment[var] = val
    
    for u_var in unassigned:
        to_remove = []
        for u_val in new_domains[u_var]:
            if not is_consistent(u_var, u_val, temp_assignment):
                to_remove.append(u_val)
        for rm in to_remove:
            new_domains[u_var].remove(rm)
            
    return new_domains

mrv_trace = []
def backtracking_mrv(assignment, current_domains):
    if len(assignment) == len(VARIABLES):
        return assignment
        
    var, reason = get_mrv_degree_var(assignment, current_domains)
    mrv_trace.append(f"Selecionado {var} via {reason}. Domínio atual: {current_domains[var]}")
    
    for val in current_domains[var]:
        if is_consistent(var, val, assignment):
            assignment[var] = val
            
            # Forward Checking opcional p/ reduzir domínios futuros no MRV
            # Aqui faremos apenas atribuição e check clássico ou com FC se desejar
            new_domains = update_domains_fc(var, val, assignment, current_domains)
            
            # Se algum domínio zerar, sabemos que falha
            if any(len(new_domains[v]) == 0 for v in VARIABLES if v not in assignment):
                del assignment[var]
                continue
                
            result = backtracking_mrv(assignment, new_domains)
            if result:
                return result
            del assignment[var]
            
    return None

# --- FORWARD CHECKING ---
fc_trace = []
fc_states = 0
fc_backtracks = 0

def forward_checking(assignment, current_domains):
    global fc_states, fc_backtracks
    
    if len(assignment) == len(VARIABLES):
        return assignment
        
    unassigned = [v for v in VARIABLES if v not in assignment]
    var = unassigned[0]
    
    for val in current_domains[var]:
        fc_states += 1
        assignment[var] = val
        
        # Propagação (FC)
        new_domains = update_domains_fc(var, val, assignment, current_domains)
        
        domain_failed = None
        for v in unassigned:
            if v != var and len(new_domains[v]) == 0:
                domain_failed = v
                break
                
        if domain_failed:
            fc_trace.append(f"Atribuir {var}={val} causou domínio vazio em {domain_failed}. Backtrack!")
            fc_backtracks += 1
            del assignment[var]
            continue
            
        fc_trace.append(f"Atribuído {var}={val}. Novos domínios: {new_domains}")
        result = forward_checking(assignment, new_domains)
        if result:
            return result
            
        del assignment[var]
        fc_backtracks += 1
        
    return None

# --- BACKJUMPING ---
bj_states = 0
bj_backtracks = 0
bj_trace = []

def backjumping(assignment, unassigned, conflict_set):
    global bj_states, bj_backtracks
    
    if not unassigned:
        return assignment, None
        
    var = unassigned[0]
    local_conflict = set()
    
    for val in DOMAINS[var]:
        bj_states += 1
        # Verifica consistência e acha os culpados
        conflict_with = set()
        
        # Simula is_consistent detalhado para achar culpados
        temp_assignment = assignment.copy()
        temp_assignment[var] = val
        
        valid = True
        
        if var == 'T3' and val == 'A':
            valid = False # Unária não adiciona culpados de variáveis anteriores
            
        # Consecutivos
        prev_idx = int(var[1]) - 1
        if prev_idx >= 1:
            prev_var = f"T{prev_idx}"
            if prev_var in assignment and assignment[prev_var] == val:
                valid = False
                conflict_with.add(prev_var)
                
        next_idx = int(var[1]) + 1
        if next_idx <= 6:
            next_var = f"T{next_idx}"
            if next_var in assignment and assignment[next_var] == val:
                valid = False
                conflict_with.add(next_var)
                
        # Regra B
        if 'T1' in temp_assignment and 'T2' in temp_assignment:
            if temp_assignment['T1'] != 'B' and temp_assignment['T2'] != 'B':
                valid = False
                if var == 'T1': conflict_with.add('T2')
                elif var == 'T2': conflict_with.add('T1')
                
        # Regra C
        if 'T2' in temp_assignment and 'T5' in temp_assignment:
            if temp_assignment['T2'] == 'C' and temp_assignment['T5'] == 'C':
                valid = False
                if var == 'T2': conflict_with.add('T5')
                elif var == 'T5': conflict_with.add('T2')
                
        # Regra D
        if list(temp_assignment.values()).count('D') > 2:
            valid = False
            for k, v in assignment.items():
                if v == 'D':
                    conflict_with.add(k)
                    
        if not valid:
            local_conflict.update(conflict_with)
            continue
            
        assignment[var] = val
        result, jump_to = backjumping(assignment, unassigned[1:], conflict_set)
        
        if result:
            return result, None
            
        bj_backtracks += 1
        del assignment[var]
        
        if jump_to and jump_to != var:
            return None, jump_to # Continua saltando
            
    # Se esgotou os valores, atualiza o conflict set do pai
    conflict_set.update(local_conflict)
    
    if not conflict_set:
        return None, None
        
    # Identifica para onde pular (a variável mais recente no conflict set)
    # A ordem das variáveis é T1, T2...
    ordered_conflicts = [v for v in VARIABLES if v in conflict_set]
    if ordered_conflicts:
        jump_target = ordered_conflicts[-1] # mais profunda
        conflict_set.remove(jump_target)
        bj_trace.append(f"Falha em {var}. Saltando para culpado: {jump_target} (Conflict Set: {conflict_set})")
        return None, jump_target
        
    return None, None

if __name__ == "__main__":
    print("--- BACKTRACKING ---")
    sol_bt = backtracking({})
    print("Solução BT:", sol_bt)
    print(f"Estados Explorados: {bt_states_explored}")
    print(f"Retrocessos: {bt_backtracks}")
    print("\nTrace BT (Primeiros 20):")
    for t in bt_trace[:20]:
        print(t)
        
    print("\n--- MRV + DEGREE ---")
    init_domains = copy.deepcopy(DOMAINS)
    # Aplicando unária previamente para ajudar
    init_domains['T3'].remove('A')
    sol_mrv = backtracking_mrv({}, init_domains)
    print("Solução MRV:", sol_mrv)
    for t in mrv_trace:
        print(t)
        
    print("\n--- FORWARD CHECKING ---")
    sol_fc = forward_checking({}, copy.deepcopy(DOMAINS))
    print("Solução FC:", sol_fc)
    print(f"Estados Explorados: {fc_states}")
    print(f"Retrocessos: {fc_backtracks}")
    for t in fc_trace[:5]:
        print(t)
        
    print("\n--- BACKJUMPING ---")
    sol_bj, _ = backjumping({}, VARIABLES, set())
    print("Solução BJ:", sol_bj)
    print(f"Estados Explorados: {bj_states}")
    print(f"Retrocessos: {bj_backtracks}")
    for t in bj_trace:
        print(t)
