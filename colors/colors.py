## given sprite link, get image data]
from typing import List
import requests
from PIL import Image
import colour

def processPalette(palette_raw: List[int]) -> List[str]:
    colourPalette = []
    i = 0
    while i+2 < len(palette_raw):
        # [x, y, z] in decimal -> to "#XYZ" in hex
        r = hex(palette_raw[i])
        g = hex(palette_raw[i+1])
        b = hex(palette_raw[i+2])
        HEX_PREFIX = "0x"
        h = f"#{r.removeprefix(HEX_PREFIX)}{g.removeprefix(HEX_PREFIX)}{b.removeprefix(HEX_PREFIX)}"
        colourPalette.append(h)
        i+=3
    return colourPalette
