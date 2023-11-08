import random

def generate_random_cities(number_of_cities):
    turkish_cities = [
    "Adana", "Adapazari", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", 
    "Amasra", "Amasya", "Ankara", "Antakya", "Antalya", "Ardahan", "Artvin", 
    "Aydin", "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", 
    "Bitlis", "Bolu", "Burdur", "Bursa", "Canakkale", "Cankiri", "Corum", 
    "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig", "Erzincan", "Erzurum", 
    "Eskisehir", "Fethiye", "Gaziantep", "Giresun", "Gumushane", "Hakkari", 
    "Hatay", "Igdir", "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", 
    "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kirikkale", "Kirklareli", 
    "Kirsehir", "Kocaeli", "Konya", "Kutahya", "Luleburgaz", "Malatya", "Manisa", 
    "Mardin", "Mersin", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", 
    "Sakarya", "Samsun", "Sanliurfa", "Siirt", "Sinop", "Sirnak", "Sivas", 
    "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak", "Van", "Yalova", "Yozgat", 
    "Zonguldak"
]

    if number_of_cities > len(turkish_cities):
        print("Error: Requested number of cities exceeds the available cities.")
        return None

    random_cities = random.sample(turkish_cities, number_of_cities)
    return random_cities

