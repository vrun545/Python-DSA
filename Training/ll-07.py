class Node: 
    def __init__(self, id,nm,sal):
        self.id = id
        self.name = nm
        self.salary = sal
        self.next = None
	
class LinkedList: 
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    # Function to print LL....
    def printList(self): 
        temp = self.head
        while (temp): 
            print(temp.id," ",temp.name," ",temp.salary) 
            temp = temp.next
        print()

    # Insert a new node at the beginning 
    def push(self, id,nm,sal):
        new_node = Node(id,nm,sal)
        new_node.next = self.head
        self.head = new_node
    
	


# Code execution starts here 
if __name__=='__main__':
    
    # Start with the empty list 
    llist = LinkedList()
    n=int(input("Enter no. of records:"))
    for i in range(n):
        id=int(input("Enter id"))
        nm=input("Enter name")
        sal=int(input("Enter salary"))
        llist.push(id,nm,sal)

    llist.printList()

        
