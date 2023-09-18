from utils._01_text_utils import display_random_text_block

def test_display_random_text_block():
    output = display_random_text_block("00_input_text.txt")
    assert isinstance(output, str)
