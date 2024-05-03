class employee:
   count = 0
   def __init__(self,id,first_name,last_name): 
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        employee.count = employee.count + 1
   def get_full_name(self):                  #getter function
       return self.__first_name + " " + self.__last_name
   def set_last_name(self,new_last_name):    #setter function
       self.__last_name = new_last_name

emp1 = employee(101,"Jordan","Pele")
emp2 = employee(102,"Conor","Mcgragor")
emp3 = employee(103,"Kevin","O'Brien")

print("Total no. of instance variables in class employee=",employee.count)
print("Total no. of instance variables in class employee=",emp1.count)

print(emp2.get_full_name())

emp3.set_last_name("Peterson")
print(emp3.get_full_name())

print(emp1)

print(emp1.__dict__)