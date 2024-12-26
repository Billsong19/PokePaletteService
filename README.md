## Routes

GET /palette/<pokemon_id OR pokemon_name>

response: list of object with attributes pokemonName, id, colors[].
colors is a sorted list of colors present in the sprite of the pokemon.

{
    colors: ["#222222", "000000"],
}
