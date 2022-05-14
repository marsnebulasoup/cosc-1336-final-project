######################
# Name: Kevin Bryniak
# Final Project
# Processes CSV files with hotel reviews and outputs useful statistics for them.
######################

import sys
from consts.errors import ERROR_COULD_NOT_FIND_NAME_COL 
try:
    from pandas import DataFrame, read_csv
    import rich
    from rich.progress import Progress
except ImportError:
    print(ERROR_MODULES_NOT_FOUND)
    sys.exit()
