import pytest

""" 
Импорт класса
"""
from src.phone import Phone


def test_repr():
    """
    Проверяет магический метод repr по заданным параметрам
    """
    phone1 = Phone("Xiaomi", 15000, 120, 3)
    assert repr(phone1) == "Phone('Xiaomi', 15000, 120, 3)"

def test_number_of_sim():
    """
    Проверяем, чтобы кол-во сим-карт было целым, неотрицательным числом
    """

    phone3 = Phone("Супермегафон", 1000000, 2, 6)
    assert phone3.number_of_sim == 6
