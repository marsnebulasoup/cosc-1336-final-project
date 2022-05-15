######################
# Name: Kevin Bryniak
# Final Project
# Constants used mainly with aggregate functions
######################

NAME_COL = "Name"
SCORE_COL = "Score"
STARS_COL = "Stars"
REVIEW_COUNT_COL = "Reviews"
ROOM_COL = "Rooms"

MIN_REVIEWS = 1  # will keep hotels w/ review count > MIN_REVIEWS (not >=)

AMENITY_PATTERN = "^(YES|NO)$"
SCORE_PATTERN = STAR_PATTERN = "^[1-5]$"
ROOM_PATTERN = "^\d+$"

AMENITY_DETAILS_DEFAULT_COLUMNS = [
    "Pool",
    "Gym",
    "Tennis court",
    "Spa",
    "Casino",
    "Free internet",
]

AMENITY_EXISTS = "YES"
AMENITY_DOES_NOT_EXIST = "NO"

DEFAULT_UNKNOWN_MSG = "Unknown"