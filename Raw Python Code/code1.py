#  Inheritance in Python
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = "Apple"
        self.camera = camera
    def getprice(self):  # used to acess private member of class
        print(self.__price)
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    def __init__(self,price,brand,camera, os, ram):
        print("Inside phone constructor")
        Phone().__init__(self,price,brand,camera)
        self.os = os
        self.ram = ram
    def insure(self):
        print("Insurance Done")
    def buy(self):  
        super().but()  # This will call super function
        print("Buying a phone")

s=SmartPhone(2000, "Apple", 12, "Android", 16)
s.insure()
s.buy()
print(s.os)
s.getprice()
print(s.brand)
# print(s.__price) # this will throw error becouse price is  a private member