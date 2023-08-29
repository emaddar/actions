# python -m pytest functions_pytest.py

from functions import calculate_sum
import pytest

def test_calculate_sum_empty_list():
    assert calculate_sum([]) == 0

def test_calculate_sum_positive_integers():
    assert calculate_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_sum_negative_integers():
    assert calculate_sum([-1, -2, -3, -4, -5]) == -15

def test_calculate_sum_floating_point_numbers():
    assert calculate_sum([1.5, 2.5, 3.5]) == 7.5

def test_calculate_sum_single_element():
    assert calculate_sum([10]) == 10

def test_calculate_sum_large_number_of_elements():
    assert calculate_sum(list(range(1, 10001))) == 50005000

def test_calculate_sum_mixed_data_types():
    with pytest.raises(TypeError):
        calculate_sum([1, 2, '3', 4, 5])