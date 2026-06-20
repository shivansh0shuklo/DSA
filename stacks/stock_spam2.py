# def stock_spam(arr):
#     stack = []
#     vec = []
#     for i in range (0,len(arr),1):
#         while(len(stack)>0 and arr[i]>=stack[-1]):
#             stack.pop()
#         if(len(stack)==0):
#             vec.append(i-(-1))
#         else:
#             vec.append(i-arr.index(stack[-1]))
#         stack.append(arr[i])
#     return vec

# a = stock_spam([100,80,60,70,60,75,85])
# print(a)


# def stoock_span(arr):
#     stack = []
#     vec = []
#     for i in range (0,len(arr),1):
#         while(len(stack)>0 and arr[i]>=stack[-1][0]):
#             stack.pop()
#         if(len(stack)==0):
#             vec.append(i-(-1))
#         elif(len(stack)>0 and stack[-1][0]>arr[i]):
#             vec.append(i-stack[-1][1])
#         stack.append([arr[i],i])
#     return vec,stack
# a,b = stoock_span([80,100,60,70,60,75,85])
# print(a,"\n",b)

'''#notes'''
#  the main thing is (I eth day - nearest greatest to left index)
#if stack is empty then (i-(-1))
#question is if its high span stock is performing well and if its low span(like 1 ) it crashed or did 
#not perform well compare to previous days

