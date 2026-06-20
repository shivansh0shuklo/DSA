def NSL(arr):
    stack = []
    vec = []
    for i in range(0,len(arr),1):
        while(len(stack)>0 and arr[i]<= stack[-1]):
            stack.pop()
        if(len(stack)==0):
            vec.append(-1)
        elif(len(stack)>0 and stack[-1]<arr[i]):
            vec.append(stack[-1])
        stack.append(arr[i])
    return vec


def nsl_index(arr):
    stack = []
    left = []
    pseudo_index = -1
    for i in range(0,len(arr),1):
        while(len(stack)>0 and stack[-1][0]>=arr[i]):
            stack.pop()
        if(len(stack) == 0):
            left.append(pseudo_index)
        elif(len(stack)>0 and arr[i]>stack[-1][0]):
            left.append(stack[-1][1])
        stack.append((arr[i],i))
    return left


