######################
# Name: Kevin Bryniak
# Final Project
# Aggregate room column into a single row for each hotel.
######################

from pandas import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy
from aggregate.shared import get_most_freq_rooms
from consts.aggregate import ROOM_COL


def get_room_details(hotels_grouped: DataFrameGroupBy):
    room_details = DataFrame()

    if type(hotels_grouped) is DataFrameGroupBy:

        room_details = hotels_grouped.agg({ROOM_COL: get_most_freq_rooms})

    return room_details
