######################
# Name: Kevin Bryniak
# Final Project
# Generates global amenity statistics.
######################

from pandas import DataFrame
from rich.text import Text
from consts.display import AMENITY_TEXT


def get_hotels_with_amenity(hotel_info: DataFrame, amenity: str):
    pass


def generate_global_amenity_stats(hotel_info: DataFrame, amenities: set):
    text = Text()

    if type(hotel_info) is DataFrame and type(amenities) is set:
        if not hotel_info.empty and len(amenities):
            text.append(AMENITY_TEXT)

            sorted_amenities = sorted(amenities)
            for amenity in sorted_amenities:
                with_amenity = get_hotels_with_amenity(hotel_info, amenity)
                text.append(f"\n\t{amenity}: {with_amenity}")

    return text
