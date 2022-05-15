######################
# Name: Kevin Bryniak
# Final Project
# Aggregate columns into a single row for each hotel.
######################

from pandas import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy
from aggregate.shared import (
    get_amenity_existence,
    get_mean_score,
    get_most_freq_stars,
    get_most_freq_rooms,
)
from consts.aggregate import NAME_COL, REVIEW_COUNT_COL, ROOM_COL, SCORE_COL, STARS_COL


def get_details(hotels_grouped: DataFrameGroupBy, amenities: set):
    details = DataFrame()
    if type(hotels_grouped) is DataFrameGroupBy:
        column_processors = {
            SCORE_COL: get_mean_score,
            STARS_COL: get_most_freq_stars,
            ROOM_COL: get_most_freq_rooms,
            REVIEW_COUNT_COL: len,
        }
        if type(amenities) is set:
            column_processors.update(
                {
                    amenity: get_amenity_existence
                    for amenity in amenities
                    if amenity != NAME_COL
                }
            )
        details = hotels_grouped.agg(column_processors)

    return details
