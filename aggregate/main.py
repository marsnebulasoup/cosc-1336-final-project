######################
# Name: Kevin Bryniak
# Final Project
# Main aggregate function.
######################

from pandas import DataFrame, Index
from aggregate.aggregate import get_details

from consts.aggregate import MIN_REVIEWS, NAME_COL
from consts.errors import ERROR_COULD_NOT_FIND_NAME_COL, ERROR_TOO_LITTLE_DATA


def aggregate(
    hotels: DataFrame, columns: list, amenities: set, sortBy: str, ascending: bool
):
    details = DataFrame()

    if type(hotels) is DataFrame and type(columns) is list and type(amenities) is set:
        if NAME_COL not in hotels:
            raise KeyError(f"{ERROR_COULD_NOT_FIND_NAME_COL} '{NAME_COL}'.")

        all_columns = Index([*columns, *amenities])

        hotels_grouped = (
            hotels.reindex(columns=all_columns)  # type: ignore
            .groupby(NAME_COL, sort=False)
            .filter(lambda reviews: len(reviews) > MIN_REVIEWS)
            .groupby(NAME_COL, sort=False)
        )  # have to regroup as .filter combines the groups

        if hotels_grouped.obj.empty:
            raise ValueError(ERROR_TOO_LITTLE_DATA)

        details = get_details(hotels_grouped, amenities)

        details = details.sort_values(
            sortBy if sortBy in hotels and sortBy in details else NAME_COL,
            ascending=(ascending if type(ascending) is bool else True),
        )

    return details
