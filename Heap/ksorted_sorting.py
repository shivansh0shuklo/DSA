import heapq as heap
def ksorted_array_sorting(karr,k):
    vec = []
    heap1 = []
    heap.heapify(heap1)
    for i in karr:
        heap.heappush(heap1,i)
        if(len(heap1)>k+1):
            vec.append(heap1[0])
            heap.heappop(heap1)
    while heap1: vec.append(heap.heappop(heap1))
    return vec
arr = [6,5,3,2,8,10,9]
k = 3
output =  ksorted_array_sorting(arr,k)
print(output)

