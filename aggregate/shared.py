######################
# Name: Kevin Bryniak
# Final Project
# Shared functions applicable to multiple columns.
######################

from pandas import Series

from consts.aggregate import (
    AMENITY_DOES_NOT_EXIST, 
    AMENITY_EXISTS,
    AMENITY_PATTERN,
    ROOM_PATTERN,
    SCORE_PATTERN,
    STAR_PATTERN,
)


def get_most_freq_acc(series: Series, pattern: str):
    most_freq = -1
    if type(series) is Series and type(pattern) is str and pattern:
        most_freq_vals = series.value_counts().filter(regex=pattern).index
        if len(most_freq_vals):
            most_freq = most_freq_vals[0]

    return most_freq


def get_amenity_existence(series: Series):
    exists = -1

    if type(series) is Series:
        series = series.astype(str).str.upper()
        most_freq = get_most_freq_acc(series, AMENITY_PATTERN)
        if most_freq == AMENITY_EXISTS:
            exists = 1
        elif most_freq == AMENITY_DOES_NOT_EXIST:
            exists = 0

    return exists


def get_most_freq_stars(series: Series):
    return int(get_most_freq_acc(series, STAR_PATTERN))


def get_most_freq_rooms(series: Series):
    return int(get_most_freq_acc(series, ROOM_PATTERN))


def get_mean_score(series: Series):
    mean_score = -1

    if type(series) is Series:
        filtered_series = series[
            series.astype(str).str.fullmatch(SCORE_PATTERN, na=False)  # type: ignore
        ]
        if len(filtered_series):
            mean_score = filtered_series.astype(int).mean()

    return mean_score
