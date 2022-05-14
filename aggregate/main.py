######################
# Name: Kevin Bryniak
# Final Project
# Main aggregate function.
######################

from pandas import DataFrame, Index
from aggregate.amenities import get_amenity_details
from aggregate.ratings import get_rating_details
from aggregate.rooms import get_room_details

from consts.aggregate import (
    MIN_REVIEWS,
    NAME_COL,
    RATING_DETAILS_DEFAULT_COLUMNS,
    ROOM_DETAILS_DEFAULT_COLUMNS,
)
from consts.errors import ERROR_COULD_NOT_FIND_NAME_COL


def aggregate(hotels: DataFrame, amenities: set, sortBy: str, ascending: bool):
    merged = DataFrame()

    if type(hotels) is DataFrame and type(amenities) is set:
        amenities = {amenity for amenity in amenities if amenity != NAME_COL}

        if NAME_COL not in hotels:
            raise KeyError(f"{ERROR_COULD_NOT_FIND_NAME_COL} '{NAME_COL}'.")

        all_columns = Index(
            [
                NAME_COL,
                *amenities,
                *RATING_DETAILS_DEFAULT_COLUMNS,
                *ROOM_DETAILS_DEFAULT_COLUMNS,
            ]
        )

        hotels_grouped = (
            hotels.reindex(columns=all_columns)  # type: ignore
            .groupby(NAME_COL, sort=False)
            .filter(lambda reviews: len(reviews) > MIN_REVIEWS)
            .groupby(NAME_COL, sort=False)
        )  # have to regroup as .filter combines the groups

        amenity_details = get_amenity_details(hotels_grouped, amenities)
        rating_details = get_rating_details(hotels_grouped)
        room_details = get_room_details(hotels_grouped)

        merged = rating_details.merge(room_details, how="left", on=NAME_COL)

        if not amenity_details.empty:
            merged = merged.merge(amenity_details, how="left", on=NAME_COL)

        merged = merged.sort_values(
            sortBy if sortBy in hotels and sortBy in merged else NAME_COL,
            ascending=(ascending if type(ascending) is bool else True),
        )

    return merged
