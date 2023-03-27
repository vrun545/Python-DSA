# a={"a":1,"b":2,"c":3}
# b=dict(zip(a.values(),a.keys()))
# print(b)

# a = ("john","doe")
# b = ("kevin","Brein")
# x = zip(a,b)
# print(tuple(x))
# print(a)
# print(b)

# def foo(*var):
#     if len(var)==1:
#         print(var)
#     if len(var)==2:
#         print(var)
#     else:
#         print(var)

# foo("ram")

# def foo(*var):
#     print(*var)

# d = {1,2,3,4,5}
# foo(d)
from abc import ABC, abstractmethod   
class Car(ABC):
    @abstractmethod
    def mileage(self):   
        print("car class")
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code  
t = Tesla ()   
t.mileage()   
p = Suzuki()
p.mileage()