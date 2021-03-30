import random

def generate_initial_population(cities_list):
    population = []
    attributes = {
        'cities_list': [],
        'initial_city': None,
        'final_city': None
    }

    for x in range(200):
        cities_list_copy = list(cities_list)
        attributes_copy = dict(attributes)

        random.shuffle(cities_list)
        attributes_copy['initial_city'] = cities_list_copy.pop(0)
        attributes_copy['final_city'] = attributes_copy['initial_city']
        attributes_copy['cities_list'] = cities_list_copy
        population.append(attributes_copy)

    return population
