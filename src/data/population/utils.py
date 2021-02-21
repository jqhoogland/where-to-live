from enum import Enum

import pandas


class CityType(Enum):
    MEGA = "MEGA"
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
    TINY = "TINY"
    TOWN = "TOWN"


MEGA_CITIES = pandas.read_csv("./cleaned/mega.csv")
LARGE_CITIES = pandas.read_csv("./cleaned/large.csv")
MEDIUM_CITIES = pandas.read_csv("./cleaned/medium.csv")
SMALL_CITIES = pandas.read_csv("./cleaned/small.csv")
# TINY_CITIES = pandas.read_csv("./cleaned/tiny.csv")
# TOWNS = pandas.read_csv("./cleaned/towns.csv")


list_intersection = lambda xs, ys: [x for x in xs if x in ys]


def filter_by_type(cities_list, type_: CityType):
    ref_cities = None

    ref_cities = {
        CityType.MEGA: MEGA_CITIES,
        CityType.LARGE: LARGE_CITIES,
        CityType.MEDIUM: MEDIUM_CITIES,
        CityType.SMALL: SMALL_CITIES,
        # CityType.TINY: TINY_CITIES,
        # CityType.TOWN: TOWNS,
    }[type_]

    return list_intersection(cities_list, ref_cities.loc[:,"Name"].tolist())


def test_city_filtering():
    cities_list = ["Kinshasa", "Pyongyang", "Lisbon", "Padang", "Tokyo", "Hong Kong", "Odesa", "Nanping"]

    assert filter_by_type(cities_list, CityType.MEGA) == ["Kinshasa", "Tokyo"]
    assert filter_by_type(cities_list, CityType.LARGE) == ["Pyongyang", "Hong Kong"]
    assert filter_by_type(cities_list, CityType.MEDIUM) == ["Lisbon", "Odesa"]
    assert filter_by_type(cities_list, CityType.SMALL) == ["Padang", "Nanping"]
