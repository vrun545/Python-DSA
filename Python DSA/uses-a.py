
class  computer:
    def writecode(self,text):
        print("written code for",text)
    def execute(self):
        print("code executed")

class student:
    def dolabassignment(self,computer,assignment):
        computer.writecode(assignment)
        computer.execute()


if __name__ == "__main__":        
    s1 = student()
    c1 = computer()
    s1.dolabassignment(c1,"sorting") 