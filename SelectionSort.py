def findSmallest(arr):
    """Function to find the smallest number in an array

    Args:
        arr (array): a list of homogenous numbers (array)

    Returns:
        int: The smallest number available in the array arr
    """

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """Function that sorts a given array

    Args:
        arr (array): The array that needs to be sorted

    Returns:
        array: A new sorted array in increasing order
    """
    newArr = []

    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == "__main__":
    print(selectionSort([1, 5, 3, 6, 7, 8, 4, 3]))
