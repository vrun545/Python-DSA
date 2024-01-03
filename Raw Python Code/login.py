# import mechanize 
 
# br = mechanize.Browser() 
# br.set_handle_robots(False) 
# br.open("http://www.gfg.com")	   #Url that contains signin form 
# br.select_form(nr=0) 
# br['username'] = "virj545@gmail.com"	#see what is the name of txt input in form 
# br['password'] ='yxh8hKJ6FAA%W^54a'
 
# result = br.submit().read() 
# f = file('s.html', 'w') 
# f.write(result) 
# # f.close() 
# l1 = ["fd", '5y4sd', 'gdiy', 'sdf76e']
# s1 = ""
# a= [1,2,1,1,1]


# Brute Force Approach

# # a = [1,2,2,1,1,1,3]
# # k = 3
# # cnt = 0
# # for i in range(len(a)):
# #     sum1 = 0
# #     for j in range(i, len(a)):
# #         sum1 += a[j]
# #         if sum1 % k == 0:
# #             cnt += 1
# # print(cnt)


# # Back-tracking

# # def solve(arr, res, i, sum1, k):
# #     if i < len(arr) and sum1 % k == 0:
# #         cnt += 1
# #         return cnt
    
    
# # arr = [1,2,2,1,1,1,3]
# # k = 3
# # n = len(arr)
# # sum1 = 0
# # res = []
# # cnt = solve(arr, res, 0, sum1, k)
# # print(cnt)


# ###################################################################################################################
# #  MINIMUM PLATFORM REQUIRED PROBLEM
# lst = [ (3, 5), (2, 8), (6, 12), (5, 6), (10, 12), (8, 10)]
# # lst.sort(key = lambda x:x[1])
# l1 = []
# for i in lst:
#     l1.append((i[0],'a'))
#     l1.append((i[1], 'd'))
# l1.sort(key = lambda x:x[0])
# l2 = [0]*len(l1)
# j = 0
# for i in l1:
#     if i[1]=='a':
#         l2[j] = l2[j-1] + 1
#     else:
#         l2[j] = l2[j-1] - 1
#     j += 1

# print(max(l2))


# def maxSubarraySum(arr, n) :
#     l1 = []
#     max_sum = float("-inf")
#     curr_sum = 0
#     for i in arr:
#         curr_sum += i
#         max_sum = max(max_sum, curr_sum)
#         curr_sum = max(0, curr_sum)
#     if max_sum == 0:
#         count = 0
#         for i in range(len(arr)):
#             if arr[i]<0:
#                 count += 1
#         if count == len(arr):
#             return max(arr)
#     return max_sum
# l1 = [-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10]
# print(max(l1))

