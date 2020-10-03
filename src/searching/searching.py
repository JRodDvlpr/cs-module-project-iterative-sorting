def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    min_value = 0
    max_value = len(arr) - 1
    
    while min_value <= max_value:
        mid = (max_value + min_value) // 2
        if target < arr[mid]:
            max_value = mid - 1
        elif target > arr[mid]:
            min_value = mid + 1
        else:
            return mid

    return -1  # not found