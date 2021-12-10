# Common Cookie Finder

This is a simple tool for finding what cookie was logged the most times on a given date. It was written using `python 3.8.3`, `pytest 5.3.5`, and `argparse 1.1`.

## Usage

The main script is at `src/most_common_cookie.py`.

usage: most_common_cookie.py [-h] -d DATE CSV_PATH

positional arguments:
  CSV_PATH    Filepath to a cookie csv to analyze.

optional arguments:
  -h, --help  show this help message and exit.
  -d DATE     Date to search for cookies.


## Testing

To test this, you will need `pytest-5.3.5`. (Your milage may vary on different versions)

Run:
```
python -m pytest
```

Unfortunately pytest does not automatically update `sys.path` like the python interpreter, so running `pytest` on its own is causing problems at the moment.