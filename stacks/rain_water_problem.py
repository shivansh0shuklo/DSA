def rain_water_harvesring(arr):
    size = len(arr)
    maxl = [0] *size
    maxr = [0] *size
    water = [0] *size
    maxl[0]= arr[0] 
    sum_water = 0
    maxr[size-1] = arr[size-1] 
    for i in range(1,size,1):
        maxl[i] = max(maxl[i-1],arr[i])
    for i in range(size-2,-1,-1):
        maxr[i] = max(maxr[i+1],arr[i])
    for i in range(0,size,1):
        water[i] = min(maxr[i],maxl[i]) - arr[i]
    for i in range(0,size):
        sum_water += water[i]
    return sum_water
print(rain_water_harvesring([1,0,2,1,0,1,3,2,1,2,1]))