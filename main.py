######################
# Name: Kevin Bryniak
# Final Project
# Processes CSV files with hotel reviews and outputs useful statistics for them.
######################

import sys
import argparse
from consts.aggregate import AMENITY_DETAILS_DEFAULT_COLUMNS, NAME_COL
from consts.main import (
    AMENITY_HELP,
    DECSENDING_HELP,
    DESCRIPTION,
    PATH_HELP,
    SORT_HELP,
)
from consts.errors import ERROR_COULD_NOT_FIND_NAME_COL
try:
    from pandas import DataFrame, read_csv
    import rich
    from rich.progress import Progress
except ImportError:
    print(ERROR_MODULES_NOT_FOUND)
    sys.exit()

def main():
  parser = argparse.ArgumentParser(description=DESCRIPTION)

  parser.add_argument("path", help=PATH_HELP)
  parser.add_argument(
      "-a",
      "--amenities",
      nargs="+",
      help=AMENITY_HELP,
      default=AMENITY_DETAILS_DEFAULT_COLUMNS,
  )
  parser.add_argument("-s", "--sort", help=SORT_HELP, default=NAME_COL, type=str)
  parser.add_argument("-desc", "--descending", help=DECSENDING_HELP, action="store_true")

  args = parser.parse_args()

main()