def max_area(arr):
    max_a = 0
    for i in range(len(arr)):
        current_area = arr[i]
        if(current_area>max_a):
            max_a = current_area
    return max_a