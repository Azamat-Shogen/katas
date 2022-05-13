def bubble_sort(arr):
    # outer pass
    for i in range(len(arr)):
        swapped = False
        # inner pass
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if not swapped:
                break

    return arr
