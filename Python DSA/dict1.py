# gem_qty = {"ruby" : 25,"diamond": 30,"emrald":15,"topaz": 18,"sapphire": 20}
# gem_price = {"ruby": 2000,"diamond": 4000,"emrald":1900,"topaz":500,"sapphire":2500}
# str1 = input().split(',')
# print(str1)
# l1 = input().split(',')
# for i in gem_qty.value():
#     gem_qty(i.int(l1))

# d1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'x':24,'y':25,'z':26}
# s1 = "gzce"
# op = 0
# for i in s1:
#     op += d1[i]
# print(op)
# def findDuplicate(arr:list, n:int):
#     d1 = {}
#     for i in arr:
#         if i not in d1:
#             d1[i] = 1
#         else:
#         	return i
# 2
# 7 3
# 1 4 5 6 6 7 7 
# 9 3
# 10 4 5 2 3 6 1 3 6
# def reverseArray(arr, m):
#     l1 = len(arr) - m - 1
#     print(l1)
#     i = m + 1
#     k = 0
#     while k <= l1//2:
#         arr[i], arr[len(arr)-k-1] = arr[len(arr)-k-1], arr[i]
#         k += 1
#         i += 1
#     print(arr)
#     return arr

# arr = [10,4,5,2,3,6,1,3,6]
# m = 3
# reverseArray(arr, m)
# def sort012(arr, n) : 
#     d1 = {}
#     for i in arr:
#         if i not in d1:
#             d1[i] = 1
#         else:
#             d1[i] += 1
#     arr.clear()
#     while d1[0] != 0:
#         arr.append(0)
#         d1[0] -= 1
#     while d1[1] != 0:
#         arr.append(1)
#         d1[1] -= 1
#     while d1[2] != 0:
#         arr.append(2)
#         d1[2] -= 1
# def sumOrProduct(n, q):
#     if q==1:
#         return n*(n+1)//2
#     else:
#         if n==0:
#             return 1
#         elif n==1:
#             return 1
#         else:
#             return n*sumOrProduct(n-1)



# arr = [3,7,4,1,2,9,10,5,6]
# arr = [1,2,3,4,5,6,7,8,9]
# for i in range(0, len(arr)):
#     flag = False
#     for j in range(0, len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             flag = True
#     if flag == False:
#         break
# print(arr)



# sentence = "this fun is crazy"
# list1 = ['fun', 'crazy']
# op = 'This fun Is crazy'
# l1 = sentence.split()
# l2 = []
# j = 0
# for i in l1:
#     if i not in list1:
#         l1[j] = i.capitalize()
#     j += 1
# sentence = " ".join(l1)
# print(sentence)


# class Human:
#     #class attribute
#     species = "Homo Sapiens"
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
        
# x = Human("Ron",26, "Male") 
# y = Human("Miley", 22, "Female")
# print(x.name)
# print(y.name)

class A:
    def __init__(self):
        print("I am the display of Class A")
 
class B(A):
    def __init__(self):
        print("I am the display of Class B")
 
class C(A):
    def __init__(self):
        print("I am the display of Class C")
 
class D(B, C):
    def __init__(self):
        print("I am the display of Class D")
 
o = D()
print(D.__mro__)     #  METHOD RESOLUTION ORDER 
# METHOD RESOLUTION ORDER is the main reason why DIAMOND PROBLEM doesn't come across in python.
print(D.mro())