import pytest


""" 
Импорт класса
"""
from src.item import Item
from src.phone import Phone
import csv


def test_count_object():
    """
    Тест счетчика количества объектов экземпляров класса
     Item и корректность хранения объектов
    """
    Item("Телевизор", 12500, 220)
    Item("Ноутбук", 70000, 15)
    assert len(Item.all) == 2


def test_calculate_total_price():
    """
    Тест метода класса на правильный
    расчет общей стоимости конкретного товара в магазине.
    """
    item = Item("Смартфон", 100.0, 5)
    assert item.price * item.quantity == 500.0


def test_apply_discount():
    """
    Тест метода класса на корректное приминение
    скидки.
    """
    item = Item("Клавиатура", 100.0, 5)
    Item.pay_rate = 0.8
    assert item.price * item.pay_rate == 80.0


def test_name():
    """
    Тест метода класса на проверку
    длинны товара
    """
    item = Item("Клавиатура", 100.0, 5)
    item.name = 'СуперСмартфон'
    assert len(item.name) == 10


def test_string_to_number():
    """
    Тест статического метода,
    возвращающий число из числа-строки.
    """
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5') == 5

def test_repr():
    """
    Проверяет магический метод repr по заданным параметрам
    """
    item = Item("Холодильник", 25000, 10)
    assert repr(item) == "Item('Холодильник', 25000, 10)"

def test_str():
    """
    Проверяет магический метод str по заданным параметрам
    """
    item = Item("Холодильник", 25000, 10)
    assert str(item) == 'Холодильник'

def test__add__():
    phone1 = Phone("Телефон", 32, 1, 2)
    item1 = Item("Смартфон", 34, 2)
    assert phone1 + item1 == 3