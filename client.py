import requests

# API base URL
BASE_URL = 'http://127.0.0.1:5000'

# Add a new perfume
def add_perfume(name, description, price):
    payload = {"name": name, "description": description, "price": price}
    response = requests.post(f'{BASE_URL}/products', json=payload)
    print(f"Response: {response.status_code}, {response.json()}")

# Retrieve all perfumes
def get_perfumes():
    response = requests.get(f'{BASE_URL}/products')
    print(f"Perfumes: {response.json()}")

if __name__ == '__main__':
    # Example perfumes with name, description, and price
    add_perfume("Chanel No. 5", "Top notes: Aldehydes, Neroli, Ylang-ylang", 15000)
    add_perfume("Dior Sauvage", "Notes of Bergamot, Ambroxan, and Sichuan Pepper", 12000)
    add_perfume("Tom Ford Black Orchid", "Notes of Black Truffle, Ylang-ylang, and Bergamot", 17000)
    get_perfumes()
