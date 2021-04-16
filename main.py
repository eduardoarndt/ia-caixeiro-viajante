import argparse
import time

from cities import cities
from functions import generate_initial_population, calculate_distance, sort_best_to_worst_distance, select_best_half, crossover, \
    mutate_population

population_size = 100
eras = 5000
initial_city = "PORTO_ALEGRE"

parser = argparse.ArgumentParser()
parser.add_argument('--population')
parser.add_argument('--city')
parser.add_argument('--eras')

args = parser.parse_args()

try:
    population_size = int(args.population or population_size)
    initial_city = str(args.city or initial_city)
    eras = int(args.eras or eras)
except Exception as exception:
    print("Invalid value given to a input parameter. Check the docs.")
    raise exception

start_time = time.time()

population = generate_initial_population(cities, population_size, initial_city)

for x in range(len(population)):
    population[x]['total_distance'] = calculate_distance(population[x]['initial_city'], population[x]['final_city'],
                                                         population[x]['cities_list'])

counter = 0
while counter < eras:
    population = sort_best_to_worst_distance(population)
    population = select_best_half(population)

    i = 0
    new_population = []
    while i < len(population) // 2:
        population_copy = list(population)
        population_copy.reverse()

        new_population.append(crossover(population[i], population_copy[i]))
        new_population.append(crossover(population_copy[i], population[i]))
        i += 1

    mutate_population(new_population)

    for x in range(len(new_population)):
        new_population[x]['total_distance'] = calculate_distance(new_population[x]['initial_city'],
                                                                 new_population[x]['final_city'],
                                                                 new_population[x]['cities_list'])

    population = list(population) + list(new_population)

    counter = counter + 1

population = sort_best_to_worst_distance(population)

print("--- %s seconds ---" % (time.time() - start_time))
