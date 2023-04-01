#include <iostream>

bool is_even(const int &year, const int &stage)
{
    /*
        This function returns true if the year is divisible without a remainder,
        and False if otherwise

        Parameters:
            int (year): year from the gregorian calendar
            int(stage): the division stages for lack of better wording
        Returns:
            bool: true or false depending on evenly divisible or not
    */
    if (year % stage == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool is_leap_year(const int &year)
{
    /*
        Function returns true or false depending on
        if the input is a leap year

        Parameter:
            int(year): year from the gregorian calendar
        Returns:
            bool: true or false depending on leap year or not
    */
    bool leap_year = false;
    int stages[3] = {4, 100, 400};

    if (is_even(year, stages[0]))
    {
        leap_year = true;
        if (is_even(year, stages[1]))
        {
            leap_year = false;
            if (is_even(year, stages[2]))
            {
                leap_year = true;
            }
            else
            {
                leap_year = false;
            }
        }
    }
    else
    {
        leap_year = false;
    }
    return leap_year;
}

int main()
{

    int test_cases[8] = {2000, 2004, 2012, 2023, 2012, 1024, 2005}; // Instantiating test cases

    for (auto i : test_cases)
    {
        if (is_leap_year(i))
            std::cout << "This is a leap year \n ";
        else
            std::cout << "This is not a leap year \n";
    }

    return 0;
}
