######################
# Name: Kevin Bryniak
# Final Project
# Aggregate rating columns into a single row for each hotel.
######################

from pandas import DataFrame, Index
from pandas.core.groupby.generic import DataFrameGroupBy
from aggregate.shared import get_mean_score, get_most_freq_stars
from consts.aggregate import REVIEW_COUNT_COL, SCORE_COL, STARS_COL


def get_rating_details(hotels_grouped: DataFrameGroupBy):
    rating_details = DataFrame()

    if type(hotels_grouped) is DataFrameGroupBy:

        rating_details = hotels_grouped.agg(
            {
                SCORE_COL: get_mean_score,
                STARS_COL: get_most_freq_stars,
                REVIEW_COUNT_COL: len,
            }
        )

    return rating_details
