import pytest
from utils import *
import utils

"""Проверка всех функций (покрытие 93%) """


def test_data_perfect():
    assert data_perfect(1) == '07.12.2019'
    assert data_perfect(2) == '19.11.2019'
    assert data_perfect(3) == '13.11.2019'


def test_description_():
    assert description_(1) == 'Перевод организации'
    assert description_(2) == 'Перевод организации'
    assert description_(3) == 'Перевод со счета на счет'


def test_from_():
    assert from_(1) == 'Visa Classic 2842 87** **** 9012'
    assert from_(2) == 'Maestro 7810 84** **** 5568'
    assert from_(3) == 'Счет **9794'


def test_to_():
    assert to_(1) == 'Счет **3655'
    assert to_(2) == 'Счет **2869'
    assert to_(3) == 'Счет **8125'


def test_amount_():
    assert amount_(1) == '48150.39'
    assert amount_(2) == '30153.72'
    assert amount_(3) == '62814.53'


def test_utils():
    assert name_(1) == 'USD'
    assert name_(2) == 'руб.'
    assert name_(3) == 'руб.'
