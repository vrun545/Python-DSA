
# # BUBBLE SORT RECURSIVE APPROACH
# def bubble_sort(l1,n):
#     if n==0:
#         return
#     if n==1:
#         return 
    
#     for i in range(len(l1)-1):
#         if l1[i]>l1[i+1]:
#             l1[i], l1[i+1] = l1[i+1], l1[i]
    
#     bubble_sort(l1,n-1)

# if __name__ == "__main__":
#     l1 = [1,0,6,4,3,7,9,2,5,8]
#     bubble_sort(l1,len(l1))
#     print(l1)

# # ------------------------------------------------------------------------------

# # ITERATIVE APPROACH OF BUBBLE SORT

# # arr = [5,4,3,7,8,2,1,9,10]
# # for i in range(len(arr)-1):
# #     for j in range(len(arr)-i-1):
# #         if arr[j] > arr[j+1]:
# #             arr[j], arr[j+1] = arr[j+1], arr[j]
# # print(arr)


# # -------------------------------------------------------------------------------

# # SELECTION SORT RECURSIVE APPROACH

# # def selection_sort(l1,n):
# #     # Base Case
# #     if n == 1:
# #         return 

# #     # Processing
# #     max1 = -3789374765
# #     max_index = -1
# #     for i in range(n):
# #         if max1 < l1[i]:
# #             max1 = l1[i]
# #             max_index = i
# #     if max_index != -1:
# #         l1[n-1], l1[max_index] = l1[max_index], l1[n-1]

# #     # Recursive Relation
# #     selection_sort(l1,n-1)

# # if __name__ == "__main__":
# #     l1 = [4,3,2,1,74,321,4,325,5233,3423]
# #     selection_sort(l1,len(l1))
# #     print(l1)

# # -----------------------------------------------------------------------------------------------
# # ITERATIVE APPROACH OF SELECTION SORT
# arr = [3,2,5,6,9,7,10,1,4,8]
# for i in range(len(arr)-1):
#     min1 = i
#     mine = arr[i]
#     for j in range(i+1, len(arr)):
#         if mine > arr[j]:
#             mine = arr[j]
#             min1 = j
#     if min1 != i:
#         arr[i], arr[min1]  = arr[min1], arr[i]

# print(arr)

##################################################################################################

