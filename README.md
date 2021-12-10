# Common Cookie Finder

This is a simple tool for finding what cookie was logged the most times on a given date.

## Usage

* `python most_common_cookie.py COOKIE_LOG_PATH -d DATE`
    * Prints the most common cookie from the given file on the given date to `STDOUT`
* `python most_common_cookie.py -h` prints this usage statement.

## Testing

To test this, you will need `pytest-5.3.5`.

Run:
```
python -m pytest
```

Unfortunately pytest does not automatically update `sys.path` like the python interpreter, so running `pytest` on its own is causing problems at the moment.