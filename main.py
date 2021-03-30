import argparse

from cities import cities
from functions import generate_initial_population

population_size = None

parser = argparse.ArgumentParser()
parser.add_argument('--population')

args = parser.parse_args()

try:
    population_size = int(args.population) or 100
except Exception as exception:
    print("Invalid value given to a input parameter. Check the docs.")
    raise exception

population = generate_initial_population(cities, population_size)
