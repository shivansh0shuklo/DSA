#multiple histogram in a matrix form 
#example -
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0 
import numpy as np
from maximum_area_histogram import max_area_of_histogram as mx
def max_area_of_binary_matrix(arr,m,n):
    vec = []
    for j in range(0,m,1):
        vec.append(arr[0][j])
    max_area = mx(vec)
    for i in range(1,n,1):
        for j in range(0,m,1):
            if(arr[i][j] == 0):
                vec.insert(j,0)
            else:
                vec.insert(j,vec[j]+arr[i][j])
        if(mx(vec)>max_area):
            max_area = mx(vec)
    return max_area

arr = [[0,1,1,0],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,0,0]]
print(max_area_of_binary_matrix(arr,4,4))

"""NOTES"""
#first important thing is to write hoe to calculate the max area of a histogram 
# split the 2d matrix each row(horizontal layers) in to individual histogram
#above arr taken as a example it would be first hitoram of [0,1,1,0] next be [1,2,2,1] and so on 
# 1 means plus in previous hitogram
# 0 mean the vector imidiatly becomes zero for that perticular coloum
#just calculate max area in each steps
