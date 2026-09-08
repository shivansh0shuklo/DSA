min_element = 0
stack = []
def get_min():
    if(len(stack) == 0):
        return -1
    else:
        return min_element
def push(x):
    if(len(stack)==0):
        stack.append(x)
    else:
        if(len(stack)>0 and min_element<=x):
            stack.append(x)
        elif(len(stack)>0 and x<min_element):
            stack.append(2*x-min_element)
            min_element = x
def pop():
    if(len(stack)==0):
        return -1
    else:
        if(len(stack)>0 and stack[-1]>min_element):
            stack.pop()
        elif(len(stack)>0 and stack[-1]<min_element):
            min_element = 2*min_element - stack[-1]
            stack.pop()
def top():
    if(len(stack)==0):
        return -1
    elif(stack[-1]>=min_element):
        return stack[-1]
    elif(stack[-1]<min_element):
        return min_element
    