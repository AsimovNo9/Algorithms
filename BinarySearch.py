def binary_search(list, item):

    """Takes in a list and a searched for item, and returns the index of the item in that list

    Args:
        list (list): The list of different items to be searched through
        item (int): The integer being searched for in the list

    Returns:
        mid (int): The index of the searched for item
    """

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]  # Random list of integers

    print(binary_search(my_list, 9))  # Example using the number 9
