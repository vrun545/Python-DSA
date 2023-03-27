# # class destructiondemo:
# #     def __init__(self):
# #         print("you're welcome!!!")
# #     def __del__(self):
# #         print("Destruct execute successfully!!!")
# # obj1=destructiondemo()
# # obj2 = obj1
# # obj3 = obj1
# # print("id of object 1",id(obj1))
# # print("id of object 2",id(obj2))
# # print("id of object 3",id(obj3))
# # del obj1
# # del obj2
# # del obj3
# # a=input("Input string:")
# # print(a)
# # x = list(map(int, input("Enter multiple values: ").split()))
# # print("List of students: ", x)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         l1 = []
#         i, j = 0, 0
        
#         if 0 in nums1:
#             while 0 in nums1:
#                 nums1.remove(0)
        
#         if 0 in nums2:
#             while 0 in nums2:
#                 nums2.remove(0)
                
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] <= nums2[j]:
#                 l1.append(nums1[i])
#                 i += 1
#             else:
#                 l1.append(nums2[j])
#                 j += 1
        
#         if i == len(nums1):
#             while j < len(nums2):
#                 l1.append(nums2[j])
#                 j += 1
                
#         if j == len(nums2):
#             while i < len(nums1):
#                 l1.append(nums1[i])
#                 i += 1
                
#         nums1.clear()
#         nums1 = [0]*len(l1)
#         for i in range(len(l1)):
#             nums1[i] = l1[i]
            
#         print(nums1)
# print((4+5)//2)
################################################################################
# s = "Let's take LeetCode contest"
# Output = "s'teL ekat edoCteeL tsetnoc"
# l1 = s.split(' ')
# op = [i[::-1] for i in l1]
# op1 = []
# for i in l1:
#     op1.append(i[::-1])
# s1 = " ".join(op1)
# print(op1)
# print(s1)
##############################################################################
s = "A16DC34"
# l1=[]
# l2=[]
# for i in s:
#     if i.isalpha():
# #         l1.append(i)
# #     else:
# #         l2.append(i)
# # op1 = "".join(sorted(l1))
# # op1 += "".join(sorted(l2)) 
# # print(op1)
# # 33#######################################################################
# # from collections import Counter
# # s = "aaabdchuddghhds"
# # my_counter = Counter(s)
# # print(my_counter.items())

# import sys

# def swap(str,i,j):
#     if i>j:
#         return
#     temp = str[i]
#     str[i] = str[j]
#     str[j] = temp
#     i += 1
#     j -= 1
#     swap(str,i,j)
    
# def reverseString(string):
#     # Write your code here.
#     i, j = 0, len(string)-1
#     l1 = list(string)
#     swap(l1,i,j)
#     string = "".join(l1)
#     return string

# t = int(sys.stdin.readline().strip())

# for i in range(t):
    
#     string = str(sys.stdin.readline().strip())
    
#     for i in (reverseString(string)):
#         print(i, end = '')
        
#     print()

# import itertools
 
# if __name__ == '__main__':
#     s = 'ABC'
    
#     nums = list(s)
#     permutations = list(itertools.permutations(nums))
 
#     print([''.join(permutation) for permutation in permutations])

# Function to swap two characters in a character array
def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp
 
# Recursive function to generate all permutations of a string
def permutations(ch, curr_index=0):
 
    if curr_index == len(ch) - 1:
        l1.append(''.join(ch))
        return

    for i in range(curr_index, len(ch)):

        # including characters
        swap(ch, curr_index, i)

        # recursive relation
        permutations(ch, curr_index + 1)
        
        # backtracking
        swap(ch, curr_index, i)
    
    return l1
 
if __name__ == '__main__':
    l1 = []
    s = 'ABC'
    l1 = permutations(list(s))
    print(l1)