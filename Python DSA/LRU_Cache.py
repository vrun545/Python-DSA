from urllib.parse import _NetlocResultMixinStr

class Node:
    hash = dict()
    def _init__(self, v1, v2):
        self.prev = None
        self.t1 = (v1, v2)
        self.next = None
        self.map = dict()

    def put(self, key, value, size):
        if size < len(self.d1):
            t1 = head.next
            t2 = Node(key, value)
            hash[key] = (value, t2)
            t2.prev = head
            t2.next = t1
            t1.prev = t2
            size += 1
        else:
            tail.prev = tail.prev.prev
            t1 = head.next
            t2 = Node(key, value)
            hash[key] = (value, t2)
            t2.prev = head
            t2.next = t1
            t1.prev = t2


    def get(self, key):
        if key in hash:
            print(f"Value of {key} is: ", hash[key])
        else:
            print(f"{key} is not present in the map")
    

    def Display(self, head):
        p = self.head
        while p.next:
            print(p.t1, end = " ")
            p = p.next
        
if "__name__" == "__main__":
    size = int(input("Enter the size of the LRU Cache: "))
    head = Node(0, 0)
    tail = Node(0, 0)
    head.prev, tail.next = None, None
    head.put(1, 15)
    head.put(4, 4)
    head.put(3, 15)
    head.printDLL(head)
    