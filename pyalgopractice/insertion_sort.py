def insertion_sort(a: list):
    for value, key in enumerate(a):
        j = value - 1
        while j > -1 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


a = [4, 1, 2, 67, 43, 23, 54, 55, 45, 12, 11, 32, 21, 90, 87, 89, 98, 22, 43]

insertion_sort(a)
print(a)
