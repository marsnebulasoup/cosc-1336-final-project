######################
# Name: Kevin Bryniak
# Final Project
# Generates individual hotel statistics.
######################

from pandas import Series
from consts.aggregate import (
    DEFAULT_UNKNOWN_MSG,
    REVIEW_COUNT_COL,
    ROOM_COL,
    SCORE_COL,
    STARS_COL,
)
from rich.panel import Panel
from rich.text import Text

from consts.display import SCORE_TEXT, STAR_TEXT


def get_key(hotel: Series, key: str):
    pass

def try_round(number, precision=None):
    pass
def generate_hotel_panel(hotel: Series):
    text = Text()

    if type(hotel) is Series:
        score = try_round(get_key(hotel, SCORE_COL), 2)
        review_count = try_round(get_key(hotel, REVIEW_COUNT_COL))
        stars = try_round(get_key(hotel, STARS_COL))
        rooms = try_round(get_key(hotel, ROOM_COL))

        text.append(f"{SCORE_COL}: {score}{SCORE_TEXT}")
        text.append(f"\n{STARS_COL}: {stars}{STAR_TEXT}")
        text.append(f"\n{REVIEW_COUNT_COL}: {review_count}")
        text.append(f"\n{ROOM_COL}: {rooms}")

    panel = Panel(text, title=str(hotel.name))

    return panel
