import heapq as heap

def kth_smallest(arr,k):
    heap_l = []
    for element in arr:
        heap.heappush(heap_l,-element)
        if(len(heap_l)>k):
            heap.heappop(heap_l)
    return -heap_l[0]


arr = [7,10,4,3,15,20]
k = 3
print(f"the kth smallest element is the - {kth_smallest(arr,k)}")

