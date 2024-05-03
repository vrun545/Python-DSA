# # # # class Example:
# # # #     num=10
# # # #     @staticmethod
# # # #     def add(num1,num2):
# # # #         result=(num1+num2)*Example.num
# # # #         return result 
# # # # print(Example.add(100,200))
# class student:
#     def __init__(self,name,roll):
#         self.__name = name
#         self.roll = roll
#     def getname(self):
#         return self.__name
#     @staticmethod
#     def check_age(roll):
#         if roll >= 18:
#             print("you're eligible")
#         else:
#             print("you're not eligible")
# s1 = student("Varun",101)
# s2 = student("Viraj",102)
# s1.age = 20
# print(s1.__dict__)
# # # print(s1.getname())
# # # s1.check_age(s1.age)
# # s = "PYTHON TEST"
# # for i in range(len(s)/2):
# #     print(s[i])
# # def solve():
# #     x=0
# #     pass
# # @a
# # @f
# # def solve():
# #     return
# l = list(map(int, input().split(',')))
# print(l)
# l1 = dict()
# for i in range(0,5):
#     n = int(input())
#     l1[i] = n
# print(l1)
# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)
print(li)
heapq.heappush(7)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))
