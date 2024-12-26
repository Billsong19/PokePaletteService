## fetch from poke-api
import logging
import requests


def getPokemonSpriteUrl(pokemon_id: str) -> str:
    logger = logging.getLogger(__name__)
    # Make the API call to PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    try: 
        # logger.info("BLAH")
        # print("BLSH"    )
        response = requests.get(url)
        # print(url)
        if response.status_code == 200:
            data = response.json()
            sprite_url = data['sprites']['front_default']  # Get the front sprite URL
            print(f"got sprite URL: {sprite_url}")
            return sprite_url
        # else:
            # print(f"pokeapi request returned error: {response.status_code}:\n{response.raw}")
    except Exception as e:
        logger.error(e)
