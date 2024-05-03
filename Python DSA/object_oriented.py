from abc import ABC, abstractmethod

class Vehicle(ABC):  # inherits abstract class
    #abstract method
    @abstractmethod
    def no_of_wheels(self):
        pass

class Bike(Vehicle):
    def no_of_wheels(self):   # provide definition for abstract method
        print("Bike have 2 wheels")  

class Tempo(Vehicle):
    def no_of_wheels(self):   # provide definition for abstract method
        print("Tempo have 3 wheels")

class Truck(Vehicle):   # provide definition for abstract method
    def no_of_wheels(self):
        print("Truck have 4 wheels")


bike = Bike()
bike.no_of_wheels()
tempo = Tempo()
tempo.no_of_wheels()
truck = Truck()
truck.no_of_wheels()






# from collections import deque

# q1 = deque(['sam', 'bob', 3, 8, 21, "it's a string"])
# q1.appendleft(0)
# q1.append(10)
# print(q1)
# q1.pop()
# print(q1)
# q1.popleft()
# print(q1)

# s = "       1  2        3 "
# l1 = s.split()
# l2 = s.split(" ")
# print(l1, l2, end='\n')


