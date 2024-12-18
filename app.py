from flask import Flask
from markupsafe import escape
from colors.colors import processPalette  
from poke_api.poke_api import getPokemonSpriteUrl
from requests import get
from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

@app.route("/palette/<pokemon_id>")
def getColors(pokemon_id):
   url = getPokemonSpriteUrl(pokemon_id)
   data = get(url, stream=True).raw()
   img = Image.open(data)
   palette = processPalette(img.getpalette())
   return palette
