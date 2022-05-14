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
    PROCESSING_TEXT,
    SORT_HELP,
)
from consts.errors import (
    ERROR_COULD_NOT_FIND_NAME_COL,
    ERROR_FILE_NOT_FOUND,
    ERROR_INVALID_FILE,
    ERROR_MODULES_NOT_FOUND,
    ERROR_TOO_LITTLE_DATA,
)

try:
    from pandas import DataFrame, read_csv
    import rich
    from rich.progress import Progress
except ImportError:
    print(ERROR_MODULES_NOT_FOUND)
    sys.exit()

from aggregate.main import aggregate


from display.main import display

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

  try:
      hotels: DataFrame = read_csv(args.path, dtype=str)
  except FileNotFoundError:
      rich.print(f"[red]{ERROR_FILE_NOT_FOUND} '{args.path}'.")
  except:
      rich.print(f"[red]{ERROR_INVALID_FILE}")
  else:
      amenities = set(args.amenities)

      with Progress(transient=True) as progress:
          progress.add_task(PROCESSING_TEXT, total=None)
          try:
              hotel_details = aggregate(
                  hotels, set(args.amenities), args.sort, not args.descending
              )
          except KeyError:
              rich.print(f"[red]{ERROR_COULD_NOT_FIND_NAME_COL} '{NAME_COL}'.")
              sys.exit()
          except ValueError:
              rich.print(f"[red]{ERROR_TOO_LITTLE_DATA}")
              sys.exit()

      display(hotel_details, amenities)

main()