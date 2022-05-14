######################
# Name: Kevin Bryniak
# Final Project
# Shared functions applicable to multiple columns.
######################

from pandas import Series
def get_most_freq_acc(series: Series, pattern: str):
    most_freq = -1
    if type(series) is Series and type(pattern) is str and pattern:
        most_freq_vals = series.value_counts().filter(regex=pattern).index
        if len(most_freq_vals):
            most_freq = most_freq_vals[0]

    return most_freq
