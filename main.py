import argparse

from cities import cities
from functions import generate_initial_population, calculate_distance, fitness, select_best_half, crossover

population_size = None

parser = argparse.ArgumentParser()
parser.add_argument('--population')

args = parser.parse_args()

try:
    population_size = int(args.population or 100)
except Exception as exception:
    print("Invalid value given to a input parameter. Check the docs.")
    raise exception

population = generate_initial_population(cities, population_size)

for x in range(len(population)):
    population[x]['total_distance'] = calculate_distance(population[x]['initial_city'], population[x]['final_city'], population[x]['cities_list'])

population = fitness(population)
population = select_best_half(population)


i = 0
new_population = []
while i < len(population):
    new_population.append(crossover(population[i], population[i + 1]))
    new_population.append(crossover(population[i + 1], population[i]))
    i += 2

for x in range(len(new_population)):
    new_population[x]['total_distance'] = calculate_distance(new_population[x]['initial_city'], new_population[x]['final_city'], new_population[x]['cities_list'])

population = population + new_population
