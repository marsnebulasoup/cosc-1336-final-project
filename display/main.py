######################
# Name: Kevin Bryniak
# Final Project
# Generates and displays hotel statistics.
######################

from pandas import DataFrame
from rich.console import Console
from rich.table import Table, Column
from rich.text import Text
from rich.padding import Padding

from display.amenities import generate_global_amenity_stats
from consts.display import (
    GLOBAL_STATS_TITLE,
    INDIVIDUAL_STATS_TITLE,
    STATS_STYLE,
    UNIQUE_HOTELS_TEXT,
)
from display.ratings import generate_global_rating_stats


def generate_global_stats(hotel_info: DataFrame, amenities: set):
    text = Text()

    if type(hotel_info) is DataFrame and type(amenities) is set:
        if not hotel_info.empty:
            text.append(f"{len(hotel_info)} {UNIQUE_HOTELS_TEXT}\n\n")
            text.append_text(generate_global_rating_stats(hotel_info))

            if len(amenities):
                text.append("\n\n")
                text.append_text(generate_global_amenity_stats(hotel_info, amenities))

    panel = Panel(text, expand=False)
    return panel


def generate_individual_stats(hotel_info: DataFrame, amenities: set):
    pass
def display(hotel_info: DataFrame, amenities: set):
    if type(hotel_info) is DataFrame and type(amenities) is set:
        global_stats = generate_global_stats(hotel_info, amenities)
        individual_stats = generate_individual_stats(hotel_info, amenities)

        grid = Table.grid(
            Column(),
            Column(justify="right"),
            expand=True,
            padding=(0, 2, 0, 2),
            pad_edge=True,
        )

        grid.add_row(
            Padding(Text(GLOBAL_STATS_TITLE), (1)),
            Padding(Text(INDIVIDUAL_STATS_TITLE, justify="left"), (1)),
            style=STATS_STYLE,
        )
        grid.add_row(global_stats, individual_stats)

        console = Console()
        console.print(grid)
