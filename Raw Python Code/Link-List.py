class Linked_list():
    def __init__(self):
        self.head = None

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self, t):
        while t:
            print(t.data, end=" ")
            t = t.next

if __name__ == "__main__":
    obj1 = Linked_list()
    first = Node(5)
    obj1.head = first
    second = Node(10)
    first.next = second
    third = Node(15)
    second.next = third
    first.traverse(obj1.head)