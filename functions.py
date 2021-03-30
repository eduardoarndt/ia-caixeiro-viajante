import random

def generate_initial_population(cities_list):
    population = []
    model = {
        'cities_list': [],
        'initial_city': None,
        'final_city': None
    }

    for x in range(200):
        cities_list_copy = list(cities_list)
        model_copy = dict(model)

        random.shuffle(cities_list)
        model_copy['initial_city'] = cities_list_copy.pop(0)
        model_copy['final_city'] = model_copy['initial_city']
        model_copy['cities_list'] = cities_list_copy
        population.append(model_copy)

    return population
