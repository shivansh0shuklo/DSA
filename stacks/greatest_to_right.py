import numpy as np 
array = [1,3,2,4]
print(f"original array: {array}")
def nearest_to_right(arr):
    stack = []
    vec = []
    for i in range(len(arr)-1,-1,-1):
        if(len(stack)==0):
            vec.append(-1)
        elif(len(stack)>0 and stack[-1]>arr[i]):
            vec.append(stack[-1])
        elif(len(stack)>0 and stack[-1]<arr[i]):
            while(len(stack)>0 and stack[-1]<=arr[i]):
                stack.pop()
            if(len(stack)==0):
                vec.append(-1)
            else:
                vec.append(stack[-1])
        stack.append(arr[i])
    return [stack[::-1], vec[::-1]]
list_1= nearest_to_right(array)
print(list_1)
print(f"stack - {list_1[0]}\nvector - {list_1[1]}")