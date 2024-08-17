def merge(A, left, right):
    l = 0
    r = 0
    k = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            A[k] = left[l]
            l += 1
            k += 1
        else:
            A[k] = right[r]
            r += 1
            k += 1

    while l < len(left):
        A[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        A[k] = right[r]
        r += 1
        k += 1


def merge_sort(A):
    if len(A) <= 1:
        return

    q = int(len(A)/2)
    left_list = A[0:q]
    right_list = A[q:]
    merge_sort(left_list)
    merge_sort(right_list)
    merge(A, left_list, right_list)


a = [4, 1, 2, 67, 43, 23, 54, 55, 45, 12, 11, 32, 21, 90, 87, 89, 98, 22, 43]

merge_sort(a)
print(a)
