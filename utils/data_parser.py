import os
import json
from textwrap import shorten

__data_per_year = {}

def __get_dictionary_per_month(year: int, month: int):
    __data_per_year[year][month] = {}
    for rank in range(1, 100):
        filepath = f"melon/monthly-chart/melon-{year}/melon-{year}-{str(month).zfill(2)}/melon-monthly_{year}-{str(month).zfill(2)}_{str(rank).zfill(2)}.json"
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data_string = f.read()
                __data_per_year[year][month][rank] = json.loads(data_string)
                

def get_dict(year: int) -> dict:
    '''Returns dictionary which corresponds to input year.
    If input year not exists in whole dataset, returns empty dictionary instead.'''
    __data_per_year[year] = {}
    [__get_dictionary_per_month(year, month) for month in range(1, 13)]
    data_per_year_ = __data_per_year.copy()
    __data_per_year.clear()
    return data_per_year_

