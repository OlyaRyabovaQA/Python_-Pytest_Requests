import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_createpokemons = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_changepokemons = {
    "pokemon_id": "317594",
    "name": "Lilo",
    "photo_id": 1
}
body_addpokebol = {
    "pokemon_id": "317594"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_createpokemons)
print(response_create.text)
message = response_create.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changepokemons)
print(response_change.text)
message = response_change.json()['message']
print(message)

response_addpokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokebol)
print(response_addpokebol.text)
message = response_addpokebol.json()['message']
print(message)
