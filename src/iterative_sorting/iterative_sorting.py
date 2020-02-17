# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print(arr)
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        print(f"i: {i}")
        print(f"smallest: {smallest_index}")

        for j in range(0, len(arr)):
            if arr[j] > arr[smallest_index]:
                smallest_index = j
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap
        print(f'{arr}\n\n')
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
