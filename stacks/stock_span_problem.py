def stock_span(arr):
    stack  = []
    vec = []
    for i in range(0,len(arr),1):
        while(len(stack)>0 and arr[i]>=stack[-1][0]):
            stack.pop()
        if(len(stack)==0):
            vec.append(i+1)
        elif(len(stack)>0 and arr[i]<stack[-1][0]):
            vec.append(i-stack[-1][1])
        stack.append((arr[i],i))
    return vec
print(stock_span([100,80,60,70,60,75,85]))
