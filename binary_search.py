def binary_search(arr: list, target: int):
    low = 0
    high = len(arr) - 1
    counter = 1
    while low <= high:
        counter += 1
        mid = (high + low) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

