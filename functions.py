import random

def generate_initial_population(cities_list):
    population = []

    for x in range(200):
        random.shuffle(cities_list)
        population.append(cities_list)

    return population
