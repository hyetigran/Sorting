# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arr, arrA, arrB):
    # TO-DO

    left_counter = 0
    right_counter = 0
    sorted_counter = 0

    while left_counter < len(arrA) and right_counter < len(arrB):
        if arrA[left_counter] < arrB[right_counter]:
            arr[sorted_counter] = arrA[left_counter]
            left_counter += 1
        else:
            arr[sorted_counter] = arrB[right_counter]
            right_counter += 1
        sorted_counter += 1

    while left_counter < len(arrA):
        arr[sorted_counter] = arrA[left_counter]
        left_counter += 1
        sorted_counter += 1

    while right_counter < len(arrB):
        arr[sorted_counter] = arrB[right_counter]
        right_counter += 1
        sorted_counter += 1

    return arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        merge(arr, left_arr, right_arr)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
