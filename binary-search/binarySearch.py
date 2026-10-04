def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left = 0, 
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1