## fetch from poke-api

import requests

def getPokemonSpriteUrl(pokemon_id):
    # Make the API call to PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/${pokemon_id.lower()}"
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        sprite_url = data['sprites']['front_default']  # Get the front sprite URL
        return sprite_url
    else:
        print("Pokémon not found. Please check the name and try again.")
