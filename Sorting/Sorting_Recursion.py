# # ITERATIVE APPROACH OF BUBBLE SORT

# # arr = [5,4,3,7,8,2,1,9,10]
# # for i in range(len(arr)-1):
# #     for j in range(len(arr)-i-1):
# #         if arr[j] > arr[j+1]:
# #             arr[j], arr[j+1] = arr[j+1], arr[j]
# # print(arr)


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