import os
import json
from textwrap import shorten

__data_per_year = {}
__col = ['year', 'month', 'rank', 'song_id', 'song_name', 'album', 'released_year', 'released_month', 'released_day', 'artist', 'genre', 'lyric_writer', 'composer', 'arranger', 'lyrics_row', 'lyrics']


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


def get_df(year_from: int, year_to: int):
    import pandas
    df_list = []

    '''Returns pandas.DataFrame which contains all data from year_from to year_to.'''
    for year in range(year_from, year_to + 1):
        data_per_year = get_dict(year)
        for month in data_per_year[year].keys():
            print(f"\r[data_parser] Parsing data from {month}, {year}. please wait...", end="")
            for rank in data_per_year[year][month].keys():
                data_ = data_per_year[year][month][rank]
                if data_['song_id'] != None:
                    song_id = data_['song_id']
                else:
                    song_id = None
                song_name = data_['song_name'].strip()
                album = data_['album'].strip()

                date = data_['release_date'].split(".")
                if date[0].isdecimal():
                    released_year = int(date[0])
                else:
                    released_year = None

                if len(date) >= 2:
                    released_month = int(data_['release_date'].split(".")[1])
                else:
                    released_month = None

                if len(date) >= 3:
                    released_day = int(data_['release_date'].split(".")[2])
                else:
                    released_day = None

                artist = data_['artist'].strip()
                genre = data_['genre'].strip()

                lyric_writer = data_['lyric_writer'].strip()
                composer = data_['composer'].strip()
                arranger = data_['arranger'].strip()
                lyrics_row = int(data_['lyrics']['row_num'])
                lyrics = data_['lyrics']['lines']

                df_list.append([year, month, rank, song_id, song_name, album, released_year, released_month, released_day, artist, genre, lyric_writer, composer, arranger, lyrics_row, lyrics])

    print(f"\r[data_parser] Parsed data to DataFrame: {year_from} >> {year_to}.")
    df = pandas.DataFrame(data=df_list)
    df.columns = __col
    return df



