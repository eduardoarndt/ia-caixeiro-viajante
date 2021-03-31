import random

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
