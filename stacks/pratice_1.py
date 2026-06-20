def nearest_to_left(arr):
    stack = []
    vec = []
    for i in range(0,len(arr)):
        if(len(stack)==0):
            vec.append(-1)
        elif(len(stack)>0 and stack[-1]<arr[i]):
            vec.append(stack[-1])
        elif(len(stack)>0 and stack[-1]>arr[i]):
            while(len(stack)>0 and stack[-1]>arr[i]):
                stack.pop()
            if(len(stack)==0):
                vec.append(-1)
            else:
                vec.append(stack[-1])
        stack.append(arr[i])
    return vec 
print(nearest_to_left([4, 5, 2, 10, 8]))