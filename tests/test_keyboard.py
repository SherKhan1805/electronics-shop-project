from src.keyboard import Keyboard

def test_change_lang():
    """
    Тест клавиатуры и смены языка
    """
    kb = Keyboard('Razor x5000', 50000, 10)
    assert str(kb) == "Razor x5000"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    kb.change_lang()
    assert str(kb.language) == "RU"

    # kb.language = 'TK'