import datetime
import pandas as pd
import pytest

# import hw4 functions
from computing4dc_hw5.hw4 import count_simba, get_day_month_year, compute_distance, sum_general_int_list

# q1

def test_count_simba_normal():
    simba_test_data = [
    "Simba and Nala are lions.",
    "I laugh in the face of danger.",
    "Hakuna matata",
    "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
    assert count_simba(simba_test_data) == 3

def test_count_simba_substring():
    strings = ["SimbaSimba", "Simba123simba"]
    assert count_simba(strings) == 4

def test_count_simba_case():
    simba_test_data = ["Simba, simba, SIMBA", "simba", "SiMBa"]
    assert count_simba(simba_test_data) == 5

def test_count_simba_empty():
    assert count_simba([]) == 0
    
def test_count_simba_no_match():
    assert count_simba(["Nala", "Timon", "Pumba"]) == 0
    
# q2

def test_get_dmy_normal():
    test_dates = [
    datetime.date(2026, 10, 21),
    datetime.date(2025, 5, 14),
    datetime.date(2024, 12, 3),]
    
    expected = pd.DataFrame({
        "day": [21, 14, 3],
        "month": [10, 5, 12],
        "year": [2026, 2025, 2024],
    })

    result = get_day_month_year(test_dates)
    pd.testing.assert_frame_equal(result, expected)
    
def test_get_dmy_empty():
    result = get_day_month_year([])
    expected = pd.DataFrame(columns=["day", "month", "year"])
    pd.testing.assert_frame_equal(result, expected)
    
def test_get_dmy_wrong_type():
    dates = ["2026-10-21"]

    with pytest.raises(AttributeError):
        get_day_month_year(dates)
    
# q3

def test_compute_distance_normaL():
    coordinates = [((41.23, 23.5), (41.5, 23.4))]
    result = compute_distance(coordinates)
    assert  result[0] == pytest.approx(31.3, abs=1.0) 

    
def test_compute_distance_same_location():
    coordinates = [((41.0, 2.0), (41.0, 2.0))]

    result = compute_distance(coordinates)

    assert result[0] == pytest.approx(0)

# q4

def test_sum_general_int_list():
    numbers = [[2], 3, [[1, 2], 5]]
    assert sum_general_int_list(numbers) == 13

def test_sum_general_int_list_empty():
    assert sum_general_int_list([]) == 0


def test_sum_general_int_list_negative():
    numbers = [1, [-2, [3, -4]]]
    assert sum_general_int_list(numbers) == -2


def test_sum_general_int_list_invalid():
    with pytest.raises(TypeError):
        sum_general_int_list([1, "hello", 3])
    