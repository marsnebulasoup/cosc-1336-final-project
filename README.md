# Hotel Parser

## About
Simple command-line application to processes CSV files with hotel reviews and output useful statistics for them.

```

   Global Statistics                  Individual Statistics

  ╭───────────────────────────────╮  ╭─────── Bellagio ───────╮ ╭────── Caesars Palace ───────╮ ╭── Circus Circus ───╮
  │ 20 unique hotel(s)            │  │ Score: 4.17/5          │ │ Score: 4.1/5                │ │ Score: 3.23/5      │
  │                               │  │ Stars: 5/5             │ │ Stars: 5/5                  │ │ Stars: 3/5         │
  │ Highest rated hotel(s):       │  │ Reviews: 23            │ │ Reviews: 22                 │ │ Reviews: 22        │
  │         Wynn                  │  │ Rooms: 3933            │ │ Rooms: 3348                 │ │ Rooms: 3773        │
  │                               │  ╰────────────────────────╯ ╰─────────────────────────────╯ ╰────────────────────╯
  │ Number of five-star hotels: 7 │  ╭──────── Encore ────────╮ ╭───────── Excalibur ─────────╮ ╭───── Flamingo ─────╮
  │                               │  │ Score: 4.54/5          │ │ Score: 3.75/5               │ │ Score: 3.96/5      │
  │ Number of hotels w/(a)        │  │ Stars: 5/5             │ │ Stars: 3/5                  │ │ Stars: 3/5         │
  │         Casino: 18            │  │ Reviews: 24            │ │ Reviews: 20                 │ │ Reviews: 24        │
  │         Free internet: 19     │  │ Rooms: 2034            │ │ Rooms: 3981                 │ │ Rooms: 315         │
  │         Gym: 19               │  ╰────────────────────────╯ ╰─────────────────────────────╯ ╰────────────────────╯
  │         Pool: 19              │  ╭───── Hilton Grand ─────╮ ╭───────── Marriott ──────────╮ ╭─── Monte Carlo ────╮
  │         Spa: 15               │  │ Score: 4.17/5          │ │ Score: 4.54/5               │ │ Score: 3.35/5      │
  │         Tennis court: 5       │  │ Stars: 3/5             │ │ Stars: 3/5                  │ │ Stars: 4/5         │
  ╰───────────────────────────────╯  │ Reviews: 24            │ │ Reviews: 24                 │ │ Reviews: 23        │
                                     │ Rooms: 5               │ │ Rooms: 5                    │ │ Rooms: 3003        │
                                     ╰────────────────────────╯ ╰─────────────────────────────╯ ╰────────────────────╯
                                     ╭──────── Paris ─────────╮ ╭───── The Cosmopolitan ──────╮ ╭─── The Cromwell ───╮
                                     │ Score: 4.1/5           │ │ Score: 4.39/5               │ │ Score: 4.08/5      │
                                     │ Stars: 4/5             │ │ Stars: 5/5                  │ │ Stars: 4/5         │
                                     │ Reviews: 21            │ │ Reviews: 23                 │ │ Reviews: 24        │
                                     │ Rooms: 2916            │ │ Rooms: 2959                 │ │ Rooms: 5           │
                                     ╰────────────────────────╯ ╰─────────────────────────────╯ ╰────────────────────╯
                                     ╭───── The Palazzo ──────╮ ╭─────── The Venetian ────────╮ ╭──── The Westin ────╮
                                     │ Score: 4.37/5          │ │ Score: 4.58/5               │ │ Score: 4.05/5      │
                                     │ Stars: 5/5             │ │ Stars: 5/5                  │ │ Stars: 4/5         │
                                     │ Reviews: 19            │ │ Reviews: 24                 │ │ Reviews: 21        │
                                     │ Rooms: 3025            │ │ Rooms: 4027                 │ │ Rooms: 826         │
                                     ╰────────────────────────╯ ╰─────────────────────────────╯ ╰────────────────────╯
                                     ╭─── Treasure Island ────╮ ╭──── Tropicana Las Vegas ────╮ ╭───── Tuscany ──────╮
                                     │ Score: 3.96/5          │ │ Score: 3.9/5                │ │ Score: 4.21/5      │
                                     │ Stars: 4/5             │ │ Stars: 4/5                  │ │ Stars: 3/5         │
                                     │ Reviews: 23            │ │ Reviews: 21                 │ │ Reviews: 24        │
                                     │ Rooms: 2884            │ │ Rooms: 1467                 │ │ Rooms: 716         │
                                     ╰────────────────────────╯ ╰─────────────────────────────╯ ╰────────────────────╯
                                     ╭─────── Wyndham ────────╮ ╭─────────── Wynn ────────────╮
                                     │ Score: 4.38/5          │ │ Score: 4.73/5               │
                                     │ Stars: 3/5             │ │ Stars: 5/5                  │
                                     │ Reviews: 24            │ │ Reviews: 22                 │
                                     │ Rooms: 5               │ │ Rooms: 2700                 │
                                     ╰────────────────────────╯ ╰─────────────────────────────╯
```

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
