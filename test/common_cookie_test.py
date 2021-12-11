import pytest
from src import most_common_cookie as mcc


def test_cookie_parser():
    """
    Validates that the cookie csv parser returns the correct format.
    Also validates parse_timestamp by checking that total formatting is correct.
    """
    cookies = mcc.parse_cookies_csv("./test/data/test_cookies.csv")

    expected_result = {
        "AtY0laUfhglK3lC7" : [
            {"date": "2018-12-09", "hour":"14", "minute":"19", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-09", "hour":"06", "minute":"19", "second":"00", "timezone":"00:00"}
        ],
        "SAZuXPGUrfbcn5UA" : [
            {"date": "2018-12-09", "hour":"10", "minute":"13", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-08", "hour":"22", "minute":"03", "second":"00", "timezone":"00:00"}
        ],
        "5UAVanZf6UtGyKVS" : [
            {"date": "2018-12-09", "hour":"07", "minute":"25", "second":"00", "timezone":"00:00"}
        ],
        "4sMM2LxV07bPJzwf" : [
            {"date": "2018-12-08", "hour":"21", "minute":"30", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-07", "hour":"23", "minute":"30", "second":"00", "timezone":"00:00"}
        ],
        "fbcn5UAVanZf6UtG" : [
            {"date": "2018-12-08", "hour":"09", "minute":"30", "second":"00", "timezone":"00:00"}
        ]
    }

    assert cookies == expected_result


def test_most_common_cookie_one_cookie():
    """
    Validates find_most_common_cookie() with an example of just one cookie.
    
    Expected result -> [1, "AtY0laUfhglK3lC7"]
    """
    
    result = mcc.find_most_common_cookie({
        "AtY0laUfhglK3lC7" : [
            {"date": "2018-12-09", "hour":"14", "minute":"19", "second":"00", "timezone":"00:00"}
        ]
    }, "2018-12-09")

    assert result == [1, "AtY0laUfhglK3lC7"]


def test_most_common_cookie_one_common():
    """
    Validates find_most_common_cookie() where there is 1 most common cookie on the given date

    Expected result -> [1, "AtY0laUfhglK3lC7"]
    """
    result = mcc.find_most_common_cookie({
        "AtY0laUfhglK3lC7" : [
            {"date": "2018-12-09", "hour":"14", "minute":"19", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-09", "hour":"06", "minute":"19", "second":"00", "timezone":"00:00"}
        ],
        "SAZuXPGUrfbcn5UA" : [
            {"date": "2018-12-09", "hour":"10", "minute":"13", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-08", "hour":"22", "minute":"03", "second":"00", "timezone":"00:00"}
        ],
        "5UAVanZf6UtGyKVS" : [
            {"date": "2018-12-09", "hour":"07", "minute":"25", "second":"00", "timezone":"00:00"}
        ],
        "4sMM2LxV07bPJzwf" : [
            {"date": "2018-12-08", "hour":"21", "minute":"30", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-07", "hour":"23", "minute":"30", "second":"00", "timezone":"00:00"}
        ],
        "fbcn5UAVanZf6UtG" : [
            {"date": "2018-12-08", "hour":"09", "minute":"30", "second":"00", "timezone":"00:00"}
        ]
    }, "2018-12-09")

    assert result == [1, "AtY0laUfhglK3lC7"]


def test_most_common_cookie_date_not_present():
    """
    Validates find_most_common_cookie() where there are no cookies on the given date.
    
    Expected result -> [0]
    """
    result = mcc.find_most_common_cookie({
        "AtY0laUfhglK3lC7" : [
            {"date": "2018-12-09", "hour":"14", "minute":"19", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-09", "hour":"06", "minute":"19", "second":"00", "timezone":"00:00"}
        ],
        "SAZuXPGUrfbcn5UA" : [
            {"date": "2018-12-09", "hour":"10", "minute":"13", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-08", "hour":"22", "minute":"03", "second":"00", "timezone":"00:00"}
        ],
        "5UAVanZf6UtGyKVS" : [
            {"date": "2018-12-09", "hour":"07", "minute":"25", "second":"00", "timezone":"00:00"}
        ],
        "4sMM2LxV07bPJzwf" : [
            {"date": "2018-12-08", "hour":"21", "minute":"30", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-07", "hour":"23", "minute":"30", "second":"00", "timezone":"00:00"}
        ],
        "fbcn5UAVanZf6UtG" : [
            {"date": "2018-12-08", "hour":"09", "minute":"30", "second":"00", "timezone":"00:00"}
        ]
    }, "2000-12-08")

    assert result == [0]


def test_most_common_cookie_multiple_common():
    """
    Validates find_most_common_cookie() when multiple cookies are most common
    
    Expected result -> [3, "SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
    """
    result = mcc.find_most_common_cookie({
        "AtY0laUfhglK3lC7" : [
            {"date": "2018-12-09", "hour":"14", "minute":"19", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-09", "hour":"06", "minute":"19", "second":"00", "timezone":"00:00"}
        ],
        "SAZuXPGUrfbcn5UA" : [
            {"date": "2018-12-09", "hour":"10", "minute":"13", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-08", "hour":"22", "minute":"03", "second":"00", "timezone":"00:00"}
        ],
        "5UAVanZf6UtGyKVS" : [
            {"date": "2018-12-09", "hour":"07", "minute":"25", "second":"00", "timezone":"00:00"}
        ],
        "4sMM2LxV07bPJzwf" : [
            {"date": "2018-12-08", "hour":"21", "minute":"30", "second":"00", "timezone":"00:00"},
            {"date": "2018-12-07", "hour":"23", "minute":"30", "second":"00", "timezone":"00:00"}
        ],
        "fbcn5UAVanZf6UtG" : [
            {"date": "2018-12-08", "hour":"09", "minute":"30", "second":"00", "timezone":"00:00"}
        ]
    }, "2018-12-08")

    assert result == [3, "SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]


def test_most_common_cookie_no_cookies():
    """
    Validates find_most_common_cookie() when the provided cookie dict is empty
    
    Expected result -> [0]
    """
    result = mcc.find_most_common_cookie({}, "2018-12-12")
    assert result == [0]