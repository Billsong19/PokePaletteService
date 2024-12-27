from typing import List
from collections import deque
from logging import getLogger

## palette_raw: List of colors value in format [r1, g1, b1, r2, g2, b2 ....] where rx, gx, bx, are decimal integers from 0 to 255
## strips grayscale colors TODO: implement
## returns: List of colors in format ["#RRGGBB", "#RRGGBB", ...]
def processPalette(palette_raw: List[int]) -> List[str]:
    if len(palette_raw) == 0:
        raise ValueError("Empty palette input")
    if len(palette_raw) % 3 != 0:
        raise ValueError("Invalid palette length")
    colourPalette = deque()
    while len(palette_raw) > 0 :
        print(palette_raw)
        # [x, y, z] in decimal -> to "#XYZ" in hex
        r = palette_raw[0]
        g = palette_raw[1]
        b = palette_raw[2]
        if not ((0 <= r < 0x100) & (0 <= g < 0x100) & (0 <= b < 0x100)):
            raise ValueError("Invalid color value: must be between 0 and 255")
        h = f"#{hex(r)[2:].zfill(2).upper()}\
{hex(g)[2:].zfill(2).upper()}\
{hex(b)[2:].zfill(2).upper()}"
        colourPalette.appendleft(h)
        palette_raw = palette_raw[3:]
    print(colourPalette)
    return list(deque(colourPalette))
