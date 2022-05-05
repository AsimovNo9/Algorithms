def sum(array):
    """Recursive function to sum all the elements in a list

    Args:
        array (list): List of numbers to be summed up

    Returns:
        int: Sum of the numbers in the input list
    """

    if len(array) == 1:
        return array[0]
    else:
        return array.pop(0) + sum(array)


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    sum(list)
