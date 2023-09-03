from src.item import Item


"""
Создаем MixinKeyboard, который выполняет смену языка клавиатуры,
выполняет проверку на недопустимый язык и возвращает язык клавиатуры
"""
class MixinKeyboard:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
            return self._language

        if self._language == 'RU':
            self._language = 'EN'
            return self._language


"""
Создаем класс Keyboard, наследованный от Item и MixinKeyboard,
который возвращает название бренда/модель
"""
class Keyboard(Item, MixinKeyboard):
    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)

        self._language = language

    def __str__(self):
        return f"{self.name}"
