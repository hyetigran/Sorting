# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print(arr)
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        print(f"i: {i}")
        print(f"smallest: {smallest_index}")

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        print(f'{arr}\n\n')
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        for j in range(0, len(arr)):
            if arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
