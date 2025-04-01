# correct_date.py

"""
GSWEP Homework Mar 24, 2025

Write a function to get a string and return a boolean if the given string is a
correct date (YYYY-MM-DD) (keep in mind leap years!)

Questions:
    1. Are there any space constraints?
    2. Are there any time constraints?
    3. Are we guaranteed to get the format YYYY-MM-DD?
    4. Are we guaranteed to get each char (digit) to be between ASCII '0'-'9'?
    5. Am I allowed to use any built in functions such as isnumeric()?
    6. Is the empty string an input?
    7. Is an incomplete date an input?
    8. Is there a limit on the earliest year and/or the latest year considered
    valid?
    9. Will the years that are <1000 and months and days <10 have leading
    zeroes?

Notes:
    1. need to check for leap year
    2. each month has a different number of days
    3. make sure the number of days is correct for the month and for the year
    for february
    4. use helper functions to check the conditionals
    5. tokenize the input string -> check year -> check month -> check day
    based on year and month
    6. a data structure to hold the possible months and possible days; a
    hashmap would useful since we would have O(1) lookup but also constant
    space because if we just use it to store the possible days and months

    TIME: O(1)
    SPACE: O(1)
"""

months_and_days = dict(
    [
        ("01", 31),
        ("02", 28),  # 29 for leap years
        ("03", 31),
        ("04", 30),
        ("05", 31),
        ("06", 30),
        ("07", 31),
        ("08", 31),
        ("09", 30),
        ("10", 31),
        ("11", 30),
        ("12", 31),
    ]
)


# DONE
def string_to_int(input_str: str) -> int:
    """
    keep a running sum
    iterate through the string and subtract '0'  from each char, then multiply
    running sum by 10 and add current char
    """
    running_sum = 0
    for i in range(len(input_str)):
        running_sum *= 10
        running_sum += (int)(input_str[i]) - (int)("0")
    return running_sum


# DONE
def check_month(input_month: str) -> bool:
    if input_month in months_and_days:
        return True
    return False


def get_month(input_month: str) -> int:
    return string_to_int(input_month)


def get_month_max_day(input_month: str) -> int:
    return months_and_days[input_month]


def get_day(input_day: str) -> int:
    return string_to_int(input_day)


def leap_year(input_year: int) -> bool:
    """
    https://www.cs.usfca.edu/~cruse/cs336s09/leapyear.bob

    Rules:

        1) years divisible by 400 ARE leap years (so, for example,
        2000 will indeed be a leap year),

        2) years divisible by 100 but not by 400 are NOT leap years
        (so, for example, 1700, 1800, and 1900 were NOT leap years, NOR will
        2100 be a leap year),

        3) years divisible by 4 but not by 100 ARE leap years
        (e.g., 1988, 1992, 1996),

        4) years not divisible by 4 are NOT leap years.

    True: 2020, 2000, 2400, 1988, 2016, 0000
    False: 2019, 1900, 2100, 2021, 1800, "", [a-zA-Z]
    """
    if input_year % 400 == 0:
        return True
    elif input_year % 100 == 0 and input_year % 400 != 0:
        return False
    elif input_year % 4 == 0 and input_year % 100 != 0:
        return True
    elif input_year % 4 != 0:
        return False
    return False


def correct_date(input_date: str) -> bool:
    """
    [0-4]-[5-7]-[8-10]
    [0123]4[56]7[89]
    YYYY-MM-DD
    1. check for leap year
        - pass year to string_to_int() function
        - pass return value to leap_year()
    2. check for valid month
        - pass string to check_month()
    3. check for valid day (if leap year, then february gets an extra day)
        - check return value from leap_year() and check_month()
        - if leap_year() == True and month == '02', add 1 to the day
    """
    year = string_to_int(input_date[0:4])
    is_leap = leap_year(year)
    is_month = check_month(input_date[5:7])
    if not is_month:
        return False
    month = get_month(input_date[5:7])
    day = get_day(input_date[8:10])
    max_day = get_month_max_day(input_date[5:7])
    if is_leap and month == 2 and day >= 1 and day <= 29:
        return True
    else:
        return day >= 1 and day <= max_day

    return False


def main():
    print(correct_date("2024-03-31"), "2024-03-31 == True")
    print(correct_date("2000-02-29"), "2000-02-29 == True")
    print(correct_date("1999-12-01"), "1999-12-01 == True")
    print(correct_date("2023-06-15"), "2023-06-15 == True")
    print(correct_date("2022-11-30"), "2022-11-30 == True")
    print(correct_date("2024-02-30"), "2024-02-30 == False")
    print(correct_date("2023-04-31"), "2023-04-31 == False")
    print(correct_date("2021-13-10"), "2021-13-10 == False")
    print(correct_date("2019-00-10"), "2019-00-10 == False")
    print(correct_date("2018-06-00"), "2018-06-00 == False")
    print(correct_date("2015-02-29"), "2015-02-29 == False")
    return 0


if __name__ == "__main__":
    main()
