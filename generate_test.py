from utils import generate_csv
from utils import generate_city

cities = generate_city.generate_random_cities(20)
generate_csv.generate_normal_csv(5, cities)
generate_csv.generate_sus_csv(5,cities)