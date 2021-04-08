import random
from distances import distances

attributes = {
    'cities_list': [],
    'initial_city': None,
    'final_city': None,
    'total_distance': None
}


def generate_initial_population(cities_list, population_size):
    population = []

    for x in range(population_size):
        cities_list_copy = list(cities_list)
        attributes_copy = dict(attributes)

        random.shuffle(cities_list_copy)
        attributes_copy['initial_city'] = cities_list_copy.pop(0)
        attributes_copy['final_city'] = attributes_copy['initial_city']
        attributes_copy['cities_list'] = cities_list_copy
        population.append(attributes_copy)

    return population


def calculate_distance(initial_city, final_city, cities_list):
    total_distance = 0

    for x in range(len(cities_list) - 1):
        try:
            total_distance = total_distance + distances[cities_list[x]][cities_list[x + 1]]
        except:
            total_distance = total_distance + distances[cities_list[x + 1]][cities_list[x]]

    try:
        total_distance = total_distance + distances[initial_city][cities_list[0]]
    except:
        total_distance = total_distance + distances[cities_list[0]][initial_city]

    try:
        total_distance = total_distance + distances[final_city][cities_list[len(cities_list) - 1]]
    except:
        total_distance = total_distance + distances[cities_list[len(cities_list) - 1]][final_city]

    return total_distance


def fitness(population):
    return sorted(population, key=lambda k: k['total_distance'])


def select_best_half(population):
    return population[: (len(population) - 1) // 2]

def crossover(a, b):
    child = [None for x in range(25)]
    for x in range(8, 16):
        child[x] = a[x]

    a1 = a[0:8]
    a2 = a[8:16]
    a3 = a[16:25]

    b1 = b[0:8]
    b2 = b[8:16]
    b3 = b[16:25]

    part = b2 + b3 + b1

    for x in child:
        if x in part:
            part.remove(x)

    child[16:25] = part[0:9]
    child[0:8] = part[9:18]

    child
