# # print("hello world!!!!")
# # l1=[1,2,6,4,32,7,0]
# # l1.sort()
# # print(l1)
# # l1.pop()
# # print(l1)
# # str1= "my name is varun i am at psit"
# # print(str1.split())
# # print(str1)
# # l1 = [1,2,4,6,4,3,6,0]
# # l1.sort()
# #  print(l1)
# # str1 = "'Hello!! there i am VARUN'"
# # str1.reverse()
# # print(str1)
# # dict1 = {2:"man",1:"lan",3:"wan",4:"wifi"}
# # print(dict1.items())
# # s1 = "Varun"
# # s2 = "bajpai"
# # s1 = s1 + " " + s2
# # print(s1)
# # s1 = "name is varun"
# # print(s1.capitalize())
# # str1 = "name is varun"
# # print(str1.count('na',0,1))
# # print(str1.endswith('var'))
# # print(str1.find("V"))
# # str = "0000 !string example!!wow..!!!000"
# # print (str.strip( '0' )) # Removes all leading and trailing whitespace of string
# # print (str.lstrip( '0' )) # Removes all leading whitespace of string
# # print (str.rstrip( '0' )) # Removes all trailing whitespace of string
# # print (str.rstrip( '0!.' )) # Removes trailing 0’s,!’s and dots
# # s = "\t\tpython\nj\n\t"
# # print(s.strip()) 
# # st="three cool features in Python"
# # print(st.removesuffix("Python"))
# # print(st.removeprefix("three "))
# # print(st.removesuffix("features"))
# # str = "     pythonjsonc++java     "
# # print(str.split(maxsplit=3)) #splits from left with 3 splits
# # print(str.rsplit(maxsplit=3)) #splits from right with 3 splits
# # a = "Harsh Dev"
# # e = "außen"
# # print(e.casefold())
# # import string
# # print(string.ascii_lowercase) # all lowercase
# # string.ascii_uppercase # all uppercase
# # print(string.punctuation) # all punctuation symbols
# # string.hexdigits
# # str1 = "varun\\\nbajpai"
# # print(str1)
# # str1 = "wy"
# # str2 = "gf" # specify to replace with 
# # str3 = "u" # delete chars
# # trg = "weeksyourweeks" # target string 
# # # using maketrans() to construct translate table 
# # table = trg.maketrans(str1, str2, str3) 
# # print ("original string ", trg) 
# # # using translate() to make translations. 
# # print ("string after translation : ", trg.translate(table))
# # str='੦੩੮'
# # print(str.isnumeric()) 
# # print(str.isdigit()) 
# # print(str.isdecimal())
# # print(str.isnumeric()) 
# # print(str.isdigit()) 
# # print(str.isdecimal())
# # l1 = ["hello"]
# # print(["hello"]*3) # *‘Hello’ , ‘Hello’ , ‘Hello’+
# # [5]*3
# # print(l1)
# # mylist=[10, 20, 30, 'W', 'X', 'Y', 'Z', 60, 70]
# # mylist[3:7] = [99, 98,78,6,5,46,8,4,3]
# # print(mylist)
# # mylist = [10, 20, 30, 40, 50, 60, 70]
# # mylist[3:5] =  'WXYZ'
# # print(mylist)
# # str1 = "varunbajpai"
# # str2 = int(12)
# # print(list(str1))
# # n1 = 1 + 3j
# # print(type(n1))
# # P=[2,3,4,5,6,7]
# # x,*y = P
# # print(x) 
# # print(y)
# # dict = {'Name':'Varun', 'Age': 7,'Class':'First'}
# # print(dict)
# # d={7 : ['ab',34,45.67], 23 : ['rt', 'yt', 'lo']}
# # d[7][1]=90
# # print(d)
# # dict1 = {'Name': 'Zara', 'Age': 7}
# # dict2 ={'City': 'Kanpur'}
# # dict1.update(dict2)
# # print(dict1)
# # s = "abcd "
# # l1 = list(s)
# # for i in range(len(s)//2):
# #     l1[i], l1[len(s)-i-1] = l1[len(s)-i-1], l1[i]
# # s = " ".join(l1)
# # print(s)

# # def reverse_string(s, i, j):
# #     if i > j:
# #         return 
# #     s[i], s[j] = s[j], s[i]
# #     i += 1
# #     j -= 1
# #     reverse_string(s, i, j)

# # s = "abcd"
# # l1 = list(s)
# # reverse_string(l1, 0, len(s)-1)
# # s = "".join(l1)
# # print(s)




# # LINEAR SEARCH RECURSIVE APPROACH
# # def linear_search(l1, key, n):
# #     if n < 0:
# #         return False
# #     if key == l1[n]:
# #         return True
# #     else:
# #         ans = linear_search(l1[0:n], key, n-1)
# #     return ans

# # l1 = [4,3,2,8,10,7,5,2]
# # key = 2
# # status = linear_search(l1, key, len(l1)-1)
# # if status == 0:
# #     print("Key Not Found")
# # else:
# #     print("Key Found")


# # def second_lrgst(l1):
# #     largest = float('-inf')
# #     second = float('-inf')
# #     for i in range(len(l1)):
# #         if l1[i] > largest:
# #             second = largest
# #             largest = l1[i]
# #     return second 

# # l1 = [0,3]
# # print("The 2nd Largest Element is = ", second_lrgst(l1))
 
# # hash1 = {}
# # s = "This is a simple program" 
# # for i in s:
# #     if i not in hash1:
# #         hash1[i] = 1
# #     else:
# #         hash1[i] += 1
# # print(len(hash1))
# # l1 = []
# # for i in hash1:
# #     if hash1[i] == 1:
# #         l1.append(i)
# # for i in l1:
# #     del hash1[i]
# # print(hash1)

# # class Linked_list():
# #     def __init__(self):
# #         self.head = None

# # class Node():
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None

# #     def traverse(self, t):
# #         while t:
# #             print(t.data, end=" ")
# #             t = t.next

# # if __name__ == "__main__":
# #     obj1 = Linked_list()
# #     first = Node(5)
# #     obj1.head = first
# #     second = Node(10)
# #     first.next = second
# #     third = Node(15)
# #     second.next = third
# #     first.traverse(obj1.head)
# # matrix = [[1,1,1],[1,0,1],[1,1,1]]
# # # op = [[1,0,1],[0,0,0],[1,0,1]]
# # l1 = []
# # for i in range(len(matrix)):
# #     for j in range(len(matrix[0])):
# #         if matrix[i][j] == 0:5
# #             l1.append([i, j])
# # def fibbo(n, a, b, i):
# #     print(a+b, end= ' ')
# #     if i == n:
# #         return 
# #     fibbo(n, b, a+b, i+1)

# # n = int(input("Enter a no. = "))
# # print(0, 1, end=" ")
# # fibbo(n, 0, 1, 3)


# # def fibbo(fibb, n):
# #     if n == 0:
# #         return 0
# #     if n == 1:
# #         return 1
# #     fibb[n] = fibbo(fibb, n-1) + fibbo(fibb, n-2)

# # n = int(input("Enter a no. = "))
# # fibb = [0]*(n+1)
# # fibb[0], fibb[1] = 0, 1
# # fibbo(fibb, n)
# # print(fibb)

# # def leaders(arr, size):
# #         l1 = []
# #         max_from_right = arr[size-1]   
# #         l1.append(max_from_right)    
# #         for i in range( size-2, -1, -1):        
# #             if max_from_right < arr[i]:        
# #                 l1.append(arr[i])
# #                 print(arr[i])
# #                 max_from_right = arr[i]
# #         return l1[::-1]

# # arr = [16,17,4,3,5,2]
# # l1 = leaders(arr, len(arr))
# # print(l1)



# def sortArr(arr, n):
#     beg, mid, end = 0, 0, n-1
#     while mid <= end:
#         if arr[mid] == 0:
#             arr[beg], arr[mid] = arr[mid], arr[beg]
#             beg += 1
#             mid += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:
#             arr[mid], arr[end] = arr[end], arr[mid]
#             end -= 1

# arr = [1, 0, 1, 0, 1, 2, 2, 1, 1, 0, 1, 2, 2, 1, 0, 1, 2, 0, 0, 0, 1]
# n = len(arr)
# sortArr(arr, n)
# print(arr)


# # def quicksort(arr, beg, end):
# #     if beg < end:
# #         pi = partition(arr, beg, end)
# #         quicksort(arr, beg, pi-1)
# #         quicksort(arr, pi+1, end)

# # def partition(arr, beg, end):
# #     i, j, pi = beg, end, beg
# #     while i < j:
# #         while i < end and arr[i] <= arr[pi]:
# #             i += 1
# #         while j > 0 and arr[j] > arr[pi]:
# #             j -= 1
# #         if i < j:
# #             arr[i], arr[j] = arr[j], arr[i]
    
# #     arr[pi], arr[j] = arr[j], arr[pi]
# #     return j
    
# # if __name__ == "__main__":
# #     arr = [4,3,5,6,7,8,10,192,12,32,34,52,635,75,74,32,113,21,11,2]
# #     quicksort(arr, 0, len(arr)-1)
# #     print(arr)

# ##################################################################################################

# s = "This is my college psit"
# s1 = ""
# stack = []
# for i in range(len(s)):
#     if s[i] == " " :
#         stack.append(s1)
#         s1 = ""
#     else:
#         s1 += s[i]

# stack.append(s1)

# for i in range(len(stack)):
#     j = stack.pop()
#     print(j, end=' ')


# #############################################################################################
# def subsets(arr, k, index):
#     if index == len(arr):
#         ans.append(output[:])
#     subsets(arr, k, index+1)


# arr = [2,3,4,5,6]
# k = 6
# output = []
# ans = []
# subsets(arr, k, 0, output, ans)

# #######################################################################################################

# my_tuple = (i for i in (1, 2, 3))
# print(my_tuple)
# import time
# currenttime = time.localtime(time.time())
# print("Current time is", currenttime)
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)
# print(list(x))

# d1 = {i:i+1 for i in range(1, 10)}
# print(d1)
# value1 = [float("-inf"), float("-inf")]
# value2 = [float("-inf"), float("-inf")]
# for i in d1:
#     if d1[i] > value1[1]:
#         value2[0], value2[1] = value1[0], value1[1]
#         value1[0], value1[1] = i, d1[i] 
# print(value2)



# def subArraySum(arr, n, s):
#         ind1, ind2, j, sum1 = -1, -1, 0, 0
#         for i in range(len(arr)):
#             sum1 += arr[i]
#             if sum1 > s:
#                 while sum1 > s: 
#                     sum1 -= arr[j]
#                     j += 1
#             if sum1 == s:
#                 ind2, ind1 = i, j
#                 break
#         l1 = []
#         if ind1 == -1:
#             l1.append(-1)
#             return l1
#         l1.append(ind1+1)
#         l1.append(ind2+1)
#         return l1

# arr = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183,
#         22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
# n = 42
# s = 468
# # op = 1, 5
# l1 = subArraySum(arr, n, s)
# for i in l1:
#     print(i, end=" ")



# s = "zvvo"
# d1 = {}
# for i in range(len(s)):
#     if i not in d1:
#         d1[s[i]] = 1
# str1 = ""
# for i in d1:
#     str1 += i
# print(str1)

# s = "varunv"
# d1 = {}
# for i in range(len(s)):
#     if s[i] not in d1:
#         l1 = []
#         l1.append(i)
#         d1[s[i]] = l1
#     else:
#         d1[s[i]].append(i)
# d2 = d1.copy()
# for i in d1:
#     if len(d1[i]) == 1:
#         del(d2[i])
# value1 = float("inf")
# for i in d2:
#     if d2[i][0] < value1:
#         value1 = i
# dp = [[0]*3 for _ in range(3)]
# dp[0][1] = 5
# dp[0][0] = 10
# print(dp)
# d1 = {}
# arr = [105,120, 136, 44, 26, 122, 65, 108, 16, 82, 58, 124, 37, 62, 24, 0,36, 52, 99, 179, 150, 68, 71 ,173 ,131 ,81 ,130 ,133 ,94 ,60 ,163 ,199 ,181 ,196 ,159 ,13 ,190 ,95 ,126 ,66 ,84 ,140 ,90 ,176 ,142 ,107 ,45 ,156 ,18 ,87 ,12 ,148 ,172 ,59 ,9 ,10 ,187 ,6 ,101 ,113 ,121 ,55 ,19 ,104 ,139 ,11 ,67 ,28 ,127 ,184 ,22 ,69 ,30 ,92 ,72 ,50 ,25 ,185,40]
# s1 = set(arr)
# max_cnt = 1
# for i in range(len(arr)):
#     cnt = 0
#     t = arr[i]
#     while t in s1:
#         cnt += 1
#         t -= 1
#     max_cnt = max(max_cnt, cnt)
# print(max_cnt)
# d = {chr(x): 0 for x in range(ord('a'), ord('z')+1)}
# print(d)
# arr = [0,3,9,0,7]
# arr.sort()
# arr.reverse()
# str1 = ""
# for i in arr:
#     str1 += str(i)

# num = int(str1)
# print(num)
# matrix2 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# # for i in range(len(matrix2[0])):
# #         for j in range(len(matrix2[0])):
# #             matrix2[i][j] = matrix2[j][i]
            
# for i in range(len(matrix2)//2):
#     matrix2[i], matrix2[len(matrix2)-i-1] = matrix2[len(matrix2)-i-1], matrix2[i]
# print(matrix2)

# arr = ["budxdu", "budxdu", "akfwn", "akfwn", "budxdu", "akfwn", "suoko", "akfwn", "budxdu", "dhxeg", "suoko",
#  "akfwn", "dhxeg"]
# d1 = {}
# for i in range(len(arr)):
#     if arr[i] not in d1:
#         d1[arr[i]] = [1, i]
#     else: 
#         d1[arr[i]][0] += 1
# print(d1)
# key, value, ind = -1, 0, -1

# for i in range(len(arr)):
#     if d1[arr[i]][0] >= value and d1[arr[i]][1] > ind:
#         key = arr[i]
#         value = d1[arr[i]][0]
#         ind = d1[arr[i]][1]
        
# print(key)


# A = [225, 17, 18, 20, 11, 20, 25, 7, 27, 11, 22, 21, 22, 10, 13, 12, 9, 9, 28, 28, 20]
# B = [27, 33, 19, 26, 20, 32, 17, 38, 25, 31, 18, 18, 32, 24, 28, 11, 35, 29]
# d1 = {}
# for i in range(len(A)):
#     if A[i] not in d1:
#         d1[A[i]] = 1
#     else:
#         d1[A[i]] += 1
    
# for i in range(len(B)):
#     if B[i] in d1:
#         d1[B[i]] -= 1
# l1 = []
# for i in range(len(A)):
#     if d1[A[i]] > 0:
#         l1.append(A[i])
# print(l1)
# str1 = "23"
# str1 = str1*2
# print(str1)

# s = "3[a3[b]1[ab]]"
# # o/p = abbbab abbbab abbbab
# stack = []
# str1 = ""
# t = ''
# for i in range(len(s)):
#     if s[i] == ']':
#         while t != '[':
#             t = stack.pop()
#             if t != '[':
#                 str1 += t
#         t = stack.pop()
#         str1 = str1*int(t)
#     else:
#         stack.append(s[i])
# str1 = str1[::-1]
# print(str1)
# arr= [4,5,7,8]
# def largestNumber(self, arr: List[int]) -> str:
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             str1, str2 = str(arr[i]), str(arr[j])
#             n1, n2 = str1+str2, str2+str1
#             if int(n1) < int(n2):
#                 arr[i], arr[j] = arr[j], arr[i]
            
#     if arr[0] == 0 and arr[1] == 0:
#         return "0"

#     str1 = "" 
#     for i in range(len(arr)):
#         str1 += str(arr[i])
#     return str1
# event1 = list(map(int, input().split(',')))
# event2 = list(map(int, input().split(',')))

# if len(event2) > len(event1):
#     event1, event2 = event2[:], event1[:]

# d1= {}
# for i in event1:
#     if i not in d1:
#         d1[i] = 1
# for i in event2:
#     if i in d1:
#         d1[i] += 1
# cnt = 0
# for i in d1:
#     if d1[i] == 2:
#         cnt += 1
# print(cnt)



# n = 5
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if (i==1 or i==n-1):
#             print("*", end=" ")
#         if j==1 and i>=j:
#             print("*", end=" ")
#         if j==n-1 and i>=j:
#             print("*", end=" ")
        
#     print()



# t = int(input())
# str1 = ""
# l1= []
# while t > 0:
#     if x >= 40 and x <= 125:
#         x = int(input()) 
#         l1.append(x)
#     t -= 1 
# for i in l1:
#     str1 += chr(i)
# print(str1)


# class stack:
#     def __init__(self):
#         self.stk1 = []

#     def push(self, ele):
#         self.stk1.append(ele)

#     def pop(self):
#         t = self.stk1.pop()
#         return t

#     def size(self):
#         return f"Size of stack is {len(self.stk1)}"

#     def top(self):
#         return f"{self.stk1[-1]} is at the Top of stack"

# stk = stack()
# stk.push(1)
# stk.push(2)
# stk.push(3)
# print(stk.top())
# print(stk.pop())
# print(stk.top())
# print(stk.size())



# n = 12345
# sum1 = 0
# while n>0:
#     n1 = n%10
#     sum1 = sum1*10+n1
#     n = n//10
# print(sum1)

# def sum1(a, b):
#     if a > b:
#         return
#     else:
#         sum1(a+1, b)
#         print(a, end=" ")
        
# a = 1
# b = 10
# sum1(a,b)


# class Beans(): 
#      def type(self): 
#        print("Vegetable") 
#      def color(self):
#        print("Green") 
# class Mango(): 
#      def type(self): 
#        print("Fruit") 
#      def color(self): 
#        print("Yellow")      
# def func(obj): 
#     obj.type() 
#     obj.color()

# #creating objects
# obj_beans = Beans() 
# obj_mango = Mango() 
# # func(obj_beans) 
# # func(obj_mango)
# print(func(obj_mango))
