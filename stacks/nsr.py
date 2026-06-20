def nsr_index(arr):
        stack = []
        right = []
        pseudo_index = len(arr)
        for i in range(len(arr)-1,-1,-1):
            while(len(stack)>0 and stack[-1][0]>=arr[i]):
                stack.pop()
            if(len(stack)==0):
                right.append(pseudo_index)
            else:
                right.append(stack[-1][1])
            stack.append((arr[i],i))
        return right[::-1]

