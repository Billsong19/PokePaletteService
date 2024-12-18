## Routes

GET /colors

response: list of object with attributes pokemonName, id, colors[].
colors is a sorted list of colors present in the sprite of the pokemon.

{
    pokemonName: "",
    id: "",
    colors: ["#222222", "000000"],
}
