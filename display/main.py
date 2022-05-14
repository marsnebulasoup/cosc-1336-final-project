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
from consts.display import (
    GLOBAL_STATS_TITLE,
    INDIVIDUAL_STATS_TITLE,
    STATS_STYLE,
)
def generate_global_stats(hotel_info: DataFrame, amenities: set):
    pass
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
