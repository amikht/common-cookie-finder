def parse_timestamp(timestamp: str):
    """
    Parses a timestamp string into a dictionary for easy access to the
    year, month, day, hour, etc... of the timestamp.
    If a value is absent from the input string, its value will be None.
    Available values:
        "year"
        "month"
        "day"
        "hour"
        "minute"
        "second"
        "timezone" -> timezone offsets are not automatically applied to the hour.

    return: dict
    """
    pass


def parse_cookies(cookies: list):
    """
    Parses a list of cookie strings into a dictionary. The dictionary takes
    the cookie's name as the key, and consolidates all timestamps associated
    with the cookie into a list for the value.

    return: dict
    """
    pass

def find_most_common_cookie(cookies: dict, date: str):
    """
    Determines which cookie occurred the most times on a given date.
    If multiple cookies are the most common, they are all returned in a list.
    List format:
        index 0: number of cookies returned
        index 1..i: cookie id

    return: list
    """
    # Cookie champion algorithm. Iterate through each cookie key
    print("Cookies!~\n")


if __name__ == "__main__":
    
    # TMP INPUT FOR TESTING - REPLACE W/ COMMAND LINE ARGS
    cookie_input = input()

    cookies = parse_cookies(cookie_input)
    