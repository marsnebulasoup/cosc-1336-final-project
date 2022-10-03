# Hotel Parser

## About
Simple command-line application to processes CSV files with hotel reviews and output useful statistics for them.

## Dependencies
Requires `rich` and `pandas`, and their respective dependencies.

Install with:
```
pip install rich pandas
```

## Usage
```
main.py [-h] [-a AMENITIES [AMENITIES ...]] [-s SORT] [-desc] path
```

### Positional arguments:
  - `path`: Path to the CSV file to process. Use quotes "" if it contains spaces.

### Options:
  - `-h`, `--help`: Show a help message
  - `-a`, `--amenities`: List of amenities to display information about. Separate each amenity with spaces and surround with quotes if necessary, e.g.: `-a Casino "Free internet" Pool`.
  - `-s`, `--sort`: Name of a column to sort by. Will sort in ascending order by default. If column is not found, it'll sort by name.
  - `-desc`, `--descending`: Sorts in descending order. Without this, it'll sort in ascending order.
