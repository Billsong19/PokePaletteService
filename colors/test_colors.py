from typing import List
from colors import processPalette


def test_process_palette_empty_input():
    palette_raw = []
    result = processPalette(palette_raw)
    assert result == []

def test_process_palette_single_color():
    palette_raw = [255, 0, 0]  # Red color
    result = processPalette(palette_raw)
    assert result == ["#0xff0x00x0"]


def test_process_palette_less_than_three_elements():
    palette_raw = [255, 0]
    result = processPalette(palette_raw)
    assert result == []

def test_process_palette_non_divisible_length():
    palette_raw = [255, 0, 0, 0, 255, 0, 0, 0]  # Red, Green, incomplete Blue
    result = processPalette(palette_raw)
    assert result == ["#0xff0x00x0", "#0x00xff0x0"]

def test_process_palette_multiple_colors():
    palette_raw = [255, 0, 0, 0, 255, 0, 0, 0, 255]  # Red, Green, Blue
    result = processPalette(palette_raw)
    assert result == ["#0xff0x00x0", "#0x00xff0x0", "#0x00x00xff"]

def test_process_palette_maximum_colors():
    max_colors = 256  # Maximum number of colors in a palette
    palette_raw = [i % 256 for i in range(max_colors * 3)]  # Generate 256 unique colors
    result = processPalette(palette_raw)
    assert len(result) == max_colors
    assert result[0] == "#0x00x10x2"
    assert result[-1] == "#0xfd0xfe0xff"
    print(result)
    assert all(color.startswith("#") and len(color) == 14 for color in result)


def test_process_palette_negative_values():
    palette_raw = [-10, 20, -30, 40, -50, 60]
    result = processPalette(palette_raw)
    assert result == ["#-0xa0x14-0x1e", "#0x28-0x320x3c"]
def test_process_palette_small_values():
    palette_raw = [0, 0, 0, 1, 1, 1]  # Black and very dark gray
    result = processPalette(palette_raw)
    assert result == ["#0x00x00x0", "#0x10x10x1"]


def test_process_palette_maintain_order():
    palette_raw = [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]  # Red, Green, Blue, Yellow
    result = processPalette(palette_raw)
    assert result == ["#0xff0x00x0", "#0x00xff0x0", "#0x00x00xff", "#0xff0xff0x0"]
def test_process_palette_large_rgb_values():
    palette_raw = [255, 255, 255]  # White color
    result = processPalette(palette_raw)
    assert result == ["#0xff0xff0xff"]
