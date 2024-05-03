class LinkedList():
    def __init__(self):
        self.head = None

class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None
    
    def traverseList(self, head):
        t = head
        while t:
            print(t.data, end = " --> ")
            t = t.next
        print("null")

if __name__ == "__main__":
    list1 = LinkedList()
    first = Node(5)
    list1.head = first
    second = Node(10)
    first.next = second
    third = Node(15)
    second.next = third
    first.traverseList(list1.head)