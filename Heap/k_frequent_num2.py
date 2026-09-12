#different approach to the k frequent numbers

# import heapq as heap

def k_freq(arr,k):
    dict_store = {}
    for ele in arr:
        dict_store[ele] =  dict_store.get(ele,0) + 1
    sorted_dict = dict(sorted(dict_store.items(),key=lambda item: item[1],reverse=True))
    result = []
    count = 0
    for keys in sorted_dict:
        if(count == k):
            break
        result.append(keys)
        count+=1
    return result

arr = [3,0,1,0]
k  = 1
print(k_freq(arr,k))
