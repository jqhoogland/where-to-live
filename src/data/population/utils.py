import os
from enum import Enum

import pandas


class CityType(Enum):
    MEGA = "MEGA"
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
    TINY = "TINY"
    TOWN = "TOWN"


MEGA_CITIES = pandas.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaned/mega.csv"))
LARGE_CITIES = pandas.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaned/large.csv"))
MEDIUM_CITIES = pandas.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaned/medium.csv"))
SMALL_CITIES = pandas.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaned/small.csv"))
# TINY_CITIES = pandas.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaned/tiny.csv"))
# TOWNS = pandas.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaned/towns.csv"))

CITIES = {
        CityType.MEGA: MEGA_CITIES,
        CityType.LARGE: LARGE_CITIES,
        CityType.MEDIUM: MEDIUM_CITIES,
        CityType.SMALL: SMALL_CITIES,
        # CityType.TINY: TINY_CITIES,
        # CityType.TOWN: TOWNS,
}


list_intersection = lambda xs, ys: [x for x in xs if x in ys]
list_intersection_indices = lambda xs, ys: [i for i, x in enumerate(xs) if x in ys]


def filter_by_type(cities_list, type_: CityType):
    ref_cities = CITIES[type_]

    return list_intersection(cities_list, ref_cities.loc[:,"Name"].tolist())


def get_indices_matching_type(cities_list, type_: CityType):
    ref_cities = CITIES[type_]

    return list_intersection_indices(cities_list, ref_cities.loc[:,"Name"].tolist())



def test_city_filtering():
    cities_list = ["Kinshasa", "Pyongyang", "Lisbon", "Padang", "Tokyo", "Hong Kong", "Odesa", "Nanping"]

    assert filter_by_type(cities_list, CityType.MEGA) == ["Kinshasa", "Tokyo"]
    assert filter_by_type(cities_list, CityType.LARGE) == ["Pyongyang", "Hong Kong"]
    assert filter_by_type(cities_list, CityType.MEDIUM) == ["Lisbon", "Odesa"]
    assert filter_by_type(cities_list, CityType.SMALL) == ["Padang", "Nanping"]



def test_get_correct_indices():
    cities_list = ["Kinshasa", "Pyongyang", "Lisbon", "Padang", "Tokyo", "Hong Kong", "Odesa", "Nanping"]

    assert get_indices_matching_type(cities_list, CityType.MEGA) == [0, 4]
    assert get_indices_matching_type(cities_list, CityType.LARGE) == [1, 5]
    assert get_indices_matching_type(cities_list, CityType.MEDIUM) == [2, 6]
    assert get_indices_matching_type(cities_list, CityType.SMALL) == [3, 7]
