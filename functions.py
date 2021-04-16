import random

from distances import distances

attributes = {
    'cities_list': [],
    'initial_city': None,
    'final_city': None,
    'total_distance': None
}


def generate_initial_population(cities_list, population_size, initial_city):
    population = []

    for x in range(population_size):
        cities_list_copy = list(cities_list)
        attributes_copy = dict(attributes)

        random.shuffle(cities_list_copy)
        attributes_copy['initial_city'] = initial_city
        attributes_copy['final_city'] = initial_city
        attributes_copy['cities_list'] = cities_list_copy
        attributes_copy['cities_list'].remove(initial_city)
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


def sort_best_to_worst_distance(population):
    return sorted(population, key=lambda k: k['total_distance'])


def select_best_half(population):
    return population[: len(population) // 2]


def crossover(population_a, population_b):
    attributes_copy = dict(attributes)

    population_a_copy = dict(population_a)

    a = list(population_a['cities_list'])
    b = list(population_b['cities_list'])

    attributes_copy['initial_city'] = population_a_copy['initial_city']
    attributes_copy['final_city'] = population_a_copy['final_city']

    child = [None for x in range(25)]
    for x in range(8, 16):
        child[x] = a[x]

    b1 = b[0:8]
    b2 = b[8:16]
    b3 = b[16:25]

    part = b3 + b1 + b2

    for x in child:
        if x in part:
            part.remove(x)

    child[16:25] = part[0:9]
    child[0:8] = part[9:19]

    attributes_copy['cities_list'] = child

    return attributes_copy


def mutate_population(population):
    random_numbers = random.sample(range(0, len(population)-1), int(len(population) * 0.75))

    # for y in range(3):
    for x in range(len(random_numbers)):
        pos_a = random.randrange(len(population[x]['cities_list']))
        pos_b = random.randrange(len(population[x]['cities_list']))

        temp = population[x]['cities_list'][pos_a]
        population[x]['cities_list'][pos_a] = population[x]['cities_list'][pos_b]
        population[x]['cities_list'][pos_b] = temp
