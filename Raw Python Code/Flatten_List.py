
# FLATTEN LIST
####################################################################################
# l2=[]
# def listing(l1):
#     for i in l1:
#         if type(i)==list:
#             listing(i)
#         else:
#             l2.append(i)

# l1= [1,2,3,[4,5,[[6,7]]],[[[[8]]],9,[]],[[10]]]
# listing(l1)
# print(l2)



########################################################################################
#MAJORITY ELEMENT

# def majorityElement(self, A, N):
#         #Your code here
#         d = {}
#         for i in A:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] += 1
#         max1 = N//2
#         for i in d:
#             if d[i] > max1:
#                 max1 = i 
#                 break
#         return max1
l1 = [3,2,6,8,10,9,1,0,5,4]
for i in range(0, len(l1)):
    for j in range(0, len(l1)-i-1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]
print(l1)
