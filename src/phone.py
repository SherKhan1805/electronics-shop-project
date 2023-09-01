from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)

        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Сравнивает значение кол-ва симкарт с положительным, целым числом
        """
        if value <= 0 or type(value) == float:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            return self._number_of_sim

    def __repr__(self):
        """
        Возвращает информацию об объекте
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return int(self.quantity) + int(other.quantity)





