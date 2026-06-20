from NSL import nsl_index as left
from nsr import nsr_index as right
def max_area_of_histogram(arr):
    stack = 0
    L = left(arr)
    R= right(arr)
    width = []
    area = []
    for i in range(0,len(arr)):
        width.append(R[i] - L[i] -1)
    for i in range(len(arr)):
        area.append(width[i]*arr[i])
    return max(area)


# a = max_area_of_histogram([6,2,5,4,5,1,6])
# print(a)

"""NOTES"""
# first key important thing is to find out the nsr(in reversed order) ans nsl 
#second is to find out the width of that graph (nsr-nsl-1)
# third is left most groung is -1 and right most ground is len(arr)
# calculation of area = width[i]*arr[i]
# max(area)