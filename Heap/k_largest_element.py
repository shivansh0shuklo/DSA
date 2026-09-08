import heapq as heap
def kth_largest(arr,n):
    heap1 = []
    for i in arr:
        heap.heappush(heap1,i)
        if(len(heap1)>k):
            heap.heappop(heap1)
    return heap1[0]

arr = [1,2,3,4,5,6]
k = 2
print(kth_largest(arr,k))
