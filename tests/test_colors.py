import pytest
from colors.colors import processPalette

def test_process_palette_one_color():
    palette_raw = [255, 0, 128]
    expected_output = ["#FF0080"]
    result = processPalette(palette_raw)
    assert result == expected_output

def test_process_palette_empty():
    with pytest.raises(ValueError, match="Empty palette input"):
        processPalette([])

def test_process_palette_invalid_length():
    palette_raw = [255, 0, 128, 0]
    with pytest.raises(ValueError, match="Invalid palette length"):
        processPalette(palette_raw)

def test_process_palette_multiple_colors():
    palette_raw = [255, 0, 0, 0, 255, 0, 0, 0, 255]
    expected_output = ["#0000FF", "#00FF00", "#FF0000"]
    result = processPalette(palette_raw)
    assert result == expected_output

def test_process_palette_single_digit_hex():
    palette_raw = [15, 7, 1]
    expected_output = ["#0F0701"]
    result = processPalette(palette_raw)
    assert result == expected_output

def test_process_palette_value_greater_than_255():
    palette_raw = [0, 0, 0, 256, 0, 0]
    with pytest.raises(ValueError, match="Invalid color value: must be between 0 and 255"):
        processPalette(palette_raw)

def test_process_palette_max_values():
    palette_raw = [255, 255, 255]
    expected_output = ["#FFFFFF"]
    result = processPalette(palette_raw)
    assert result == expected_output

def test_process_palette_large():
    palette_raw = [i % 256 for i in range(300)]  # 100 colors
    expected_output = [
        f"#{(i)%256:02X}{(i+1)%256:02X}{(i+2)%256:02X}"
        for i in range(297, -1, -3)
    ]
    result = processPalette(palette_raw)
    assert result == expected_output
    assert len(result) == 100

def test_process_palette_leading_zeros():
    palette_raw = [0, 15, 7]
    expected_output = ["#000F07"]
    result = processPalette(palette_raw)
    assert result == expected_output

def test_process_palette_negative_values():
    palette_raw = [0, 0, -1]
    with pytest.raises(ValueError, match="Invalid color value: must be between 0 and 255"):
        processPalette(palette_raw)

def test_process_palette_repeating_colors():
    palette_raw = [255, 0, 0, 0, 255, 0, 255, 0, 0]
    expected_output = ["#FF0000", "#00FF00", "#FF0000"]
    result = processPalette(palette_raw)
    assert result == expected_output
