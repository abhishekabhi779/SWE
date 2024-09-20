import sys
import random

def score_zone(mine, left, right):
    gold_cnt = 0
    element_cnt = {'g': 0, 'o': 0, 'l': 0, 'd': 0}
    rock_cnt = 0
    
    i = left
    while i <= right:
        if mine[i:i+4] == "gold" or mine[i:i+4] == "dlog":
            gold_cnt += 1
            i += 4
        else:
            if mine[i] in element_cnt:
                element_cnt[mine[i]] += 1
            elif mine[i] == '-':
                rock_cnt += 1
            i += 1
    
    size = right - left + 1
    zone_scalar = 1 + (1200 * 2.718281828 ** (-size / 20000)) / 100
    
    return zone_scalar * ((4 * gold_cnt) + (4 * min(element_cnt.values())) - rock_cnt)

def generate_initial_population(mine, population_size, window_size):
    n = len(mine)
    population = []
    for _ in range(population_size):
        individual = []
        for _ in range(5):
            left = random.randint(0, n - window_size)
            right = left + window_size - 1
            if right >= n:
                right = n - 1
            individual.append((left, right))
        population.append(individual)
    return population

def evaluate_individual(mine, individual):
    return sum(score_zone(mine, left, right) for left, right in individual)

def select_parents(population, fitness, num_parents):
    parents = random.choices(population, weights=fitness, k=num_parents)
    return parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 4)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mine_length, window_size, mutation_rate):
    for i in range(5):
        if random.random() < mutation_rate:
            left = random.randint(0, mine_length - window_size)
            right = left + window_size - 1
            if right >= mine_length:
                right = mine_length - 1
            individual[i] = (left, right)
    return individual

def genetic_algorithm(mine, population_size, window_size, num_generations, mutation_rate):
    population = generate_initial_population(mine, population_size, window_size)
    for _ in range(num_generations):
        fitness = [evaluate_individual(mine, individual) for individual in population]
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitness, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, len(mine), window_size, mutation_rate)
            child2 = mutate(child2, len(mine), window_size, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
    best_individual = max(population, key=lambda ind: evaluate_individual(mine, ind))
    return best_individual

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    with open(file_path, 'r') as file:
        mine = file.read().strip()
    
    population_size = 50
    window_size = 1500
    num_generations = 100
    mutation_rate = 0.1
    
    best_zones = genetic_algorithm(mine, population_size, window_size, num_generations, mutation_rate)
    
    if len(best_zones) != 5:
        print(-1)
    else:
        output = ' '.join(f"{left} {right}" for left, right in best_zones)
        print(output)
