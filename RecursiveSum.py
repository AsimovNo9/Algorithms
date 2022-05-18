def sum(array):
    """Recursive function to sum all the elements in a list

    Args:
        array (list): List of numbers to be summed up

    Returns:
        int: Sum of the numbers in the input list
    """

    array_new = array.copy()
    if len(array_new) == 1:
        return array_new[0]
    else:
        return array_new.pop(0) + sum(array_new)


def count(array):
    """Recursive fucntion to count the number of items in a list

    Args:
        array (list): List with items to be counted

    Returns:
        int: Number of items in the list
    """

    array_new = array.copy()
    if len(array_new) == 1:
        return 1
    else:
        array_new.pop(0)
        return 1 + count(array_new)


def rbs(list, item):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = int((high - low) / 2)
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            return mid - rbs(list[:mid], item)
        elif list[mid] < item:
            return mid + rbs(list[mid:], item)


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(rbs(list, 4))

    # count(list)
