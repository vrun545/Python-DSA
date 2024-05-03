class Employee:
    def __init__(self, name, employeeId, salary):
        self.name = name    #making employee name public
        self._empID = employeeId  #making employee ID protected
        self.__salary = salary  #making salary private

    def getSalary(self):
        print(f"The salary of Employee is {self.__salary}")

employee1 = Employee("John Gates", 110514, "$1500")

print(f"The Employee's name is {employee1.name}")
print(f"The Employee's ID is {employee1._empID}")
print(f"The Employee's salary is {employee1.getSalary()}") # will throw an error because salary is defined as private
