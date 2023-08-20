import csv


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Возвращает сущности объектов класса в виде списка
        self.all = Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        """
        Функция распаковывает csv файл в виде словаря.
        Создает экземпляры класса.
        """
        with open("C:/Users/irpro/PycharmProjects/electronics-shop-project/src/items.csv", newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                name, price, quantity = item['name'], item['price'], item['quantity']
                newItem = cls(name, price, quantity)
            return newItem

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        Проверяет,  что длина наименования товара не больше
        10 симвовов. В противном случае,
        обрезаеть строку (оставляет первые 10 символов).
        """
        if len(name) > 10:
            self.__name = name[:10]
            print(f'{self.__name} -> длина наименования товара больше 10 символов')
        else:
            self.__name = name
            print(f'{self.__name } -> длина наименования товара меньше 10 символов')

    @staticmethod
    def string_to_number(number):
        """
        Возвращает строку в формате int.
        """
        try:
            return int(number)
        except ValueError:
            return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price