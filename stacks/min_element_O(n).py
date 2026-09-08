def min_element_in_stack_with_spaces(arr):
    stack = []
    supporting_stack = []
    def get_min():
        if(len(stack)==0):
            return -1
        else:
            return supporting_stack[-1]
    def push(num):
        stack.append(num)
        if(len(supporting_stack)==0 or supporting_stack[-1]>=num):
            stack.append(num)
        return 
    def pop():
        if(len(stack)==0):
            return -1
        ans = stack[-1]
        stack.pop()
        if(supporting_stack[-1]==ans):
            supporting_stack.pop()
        return ans
    
