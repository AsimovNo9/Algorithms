def check_leap_year(year: int) -> bool:
    """Function to determine if an input year is a leap year

    Args:
        int (year): Year, using the gregorian calendar

    Returns:
        bool: returns true if year is a leap year, and false if not
    """
    leap_bool = False

    if even_div(year, 4):
        leap_bool = True
        if even_div(year, 100):
            leap_bool = False
            if even_div(year, 400):
                leap_bool = True
            else:
                leap_bool = False
        else:
            leap_bool = True
    else:
        leap_bool = False
    return leap_bool


def even_div(year: int, stage: int) -> bool:
    """Function to check if a number is even

    Args:
        int (year): The number to determine if even
        int (stage): The number to be divided by

    Returns:
        bool: True if divisible with no remainder and False otherwise
    """
    if year % stage == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    test_cases = [2000, 2004, 2012, 2023, 2012, 1024, 2005]

    for x in test_cases:
        if check_leap_year(x):
            print("It's a leap year")
        else:
            print("not a leap year")

    print("Finished Running")
