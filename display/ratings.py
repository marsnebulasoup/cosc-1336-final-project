######################
# Name: Kevin Bryniak
# Final Project
# Generates global rating statistics.
######################

from pandas import DataFrame
from rich.text import Text

from consts.aggregate import SCORE_COL, STARS_COL
from consts.display import FIVE_STAR_TEXT, HIGHEST_RATED_TEXT


def generate_global_rating_stats(hotel_info: DataFrame):
    text = Text()

    if type(hotel_info) is DataFrame:
        if not hotel_info.empty:
            if SCORE_COL in hotel_info:
                highest_rated_hotels = hotel_info.query(
                    f"`{SCORE_COL}` == `{SCORE_COL}`.max() and `{SCORE_COL}` != -1"
                ).index.to_list()
                if len(highest_rated_hotels):
                    highest_rated_hotels_str = ",\n\t".join(highest_rated_hotels)
                    text.append(
                        f"{HIGHEST_RATED_TEXT}\n\t{highest_rated_hotels_str}\n\n"
                    )
            if STARS_COL in hotel_info:
                five_star_hotels = len(hotel_info.query(f"`{STARS_COL}` == 5"))
                text.append(f"{FIVE_STAR_TEXT}{five_star_hotels}")

    return text
