import argparse

def parse_timestamp(timestamp: str):
    """
    Expected format: YYYY-mm-ddThh:mm:ss+hh:mm
    Parses a timestamp string into a dictionary for easy access to the
    date, hour, etc... of the timestamp.
    If a value is absent from the input string, its value will be None.
    Available values:
        "date" -> YYYY-mm-dd
        "hour"
        "minute"
        "second"
        "timezone" -> timezone offsets are not automatically applied to the hour.

    return: dict
    """
    if timestamp == "":
        return
    timestamp = timestamp.strip("\n").split("T") # Separate date from time
    result = {}
    result["date"] = timestamp[0]
    time = timestamp[1].split("+") # Separate timezone from time
    result["timezone"] = time[1]
    time = time[0].split(":") # Separate each component of the time
    result["hour"] = time[0]
    result["minute"] = time[1]
    result["second"] = time[2]

    return result


def parse_cookies_csv(cookies_path: str):
    """
    Parses the contents of a .csv containing cookie data into a list
    which is usable by parse_cookies(), then returns the output of
    parse_cookies().
    """

    # For now I am ignoring the csv header for the sake of quickly finishing
    # this coding task. However, it would be simple in the future to extend
    # this function to take headers into account and fish out the relevant
    # data this program needs.
    # TODO: Parse headers
    cookies_dict = {}
    with open(cookies_path) as cookies_file:
        cookies_arr = cookies_file.readlines()[1:] # Ignore first line with headers
        for cookie in cookies_arr:
            cookie = cookie.split(",")
            id = cookie[0]
            timestamp = parse_timestamp(cookie[1])
            if cookie[0] in cookies_dict:
                cookies_dict[id].append(timestamp)
            else:
                cookies_dict[id] = [timestamp]

    return cookies_dict


def find_most_common_cookie(cookies: dict, date: str):
    """
    Determines which cookie occurred the most times on a given date.
    If multiple cookies are the most common, they are all returned in a list.
    List format:
        index 0: number of cookies returned
        index 1..i: cookie id

    return: list
    """
    most_common_cookies = [0]
    cookie_count = 0 # Champion cookie count
    current_count = 0 # Current cookie

    # Cookie champion algorithm. Iterate through each cookie key
    for cookie in cookies:
        #print("Testing [" + cookie + "]")
        current_count = 0
        timestamps = cookies[cookie]
        for timestamp in timestamps:
            if timestamp["date"] == date:
                current_count += 1

        if current_count > cookie_count:
            cookie_count = current_count
            most_common_cookies = [1, cookie]
        elif current_count == cookie_count and cookie_count != 0:
            most_common_cookies[0] += 1
            most_common_cookies.append(cookie)

    return most_common_cookies


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Utility to find the most common cookie logged on a given date.")

    parser.add_argument('cookie_csv', metavar="CSV_PATH", help="Filepath to a cookie csv to analyze.")
    parser.add_argument("-d", dest="date", type=str, help="Date to search for cookies.", required=True)
    args = parser.parse_args()

    cookies = parse_cookies_csv(args.cookie_csv)
    common_cookies = find_most_common_cookie(cookies, args.date)
    #print(common_cookies)

    # Cookie printing routine
    for i in range(1, common_cookies[0] + 1): # Index 0 holds number of cookies returned
        print(common_cookies[i])