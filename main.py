from utils import generate_csv
from utils import generate_city

for k in range(5):
    cities = generate_city.generate_random_cities(20)
    generate_csv.generate_sus_csv(k, cities)

for j in range(20):
    cities = generate_city.generate_random_cities(20)
    generate_csv.generate_normal_csv(j, cities)
