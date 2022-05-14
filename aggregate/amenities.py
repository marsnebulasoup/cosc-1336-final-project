######################
# Name: Kevin Bryniak
# Final Project
# Aggregate amenity columns into a single row for each hotel.
######################

from pandas import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy
from aggregate.shared import get_amenity_existence
from consts.aggregate import NAME_COL



def get_amenity_details(hotels_grouped: DataFrameGroupBy, amenities: set):
    amenity_details = DataFrame()
    if type(hotels_grouped) is DataFrameGroupBy and type(amenities) is set and len(amenities):
      
      amenity_details = hotels_grouped.agg({
          amenity: get_amenity_existence for amenity in amenities if amenity != NAME_COL
      })

    return amenity_details
