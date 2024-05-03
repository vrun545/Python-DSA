class node:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        ch = input()
        while(ch =='Y' or ch =='y'):
            print("Enter details of employee= ")
            id = int(input())
            name = input()
            salary = int(input())
            node.next = node(id,name,salary)

    def delete(self):
        pass

    def traverse(self):
        if(self.head.next==None):
            print("List is Empty")
        else:
            t = self.head
            while(t != None):
                print(t.head.data)
                t = t.next
    
    def update(self):
        pass
    
if __name__ == "__main__":
    emp = Linkedlist()
    

    