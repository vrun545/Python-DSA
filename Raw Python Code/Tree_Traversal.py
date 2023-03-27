# Tree TRaversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def pre_order(root):
    if root:
        print(root.key, end=' ')
        pre_order(root.left)
        pre_order(root.right)
    

def in_order(root):
    if root:
        in_order(root.left)
        print(root.key, end=' ')
        in_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.key, end=' ')


def count_nodes(root):
    if root:
        x = count_nodes(root.left) 
        y = count_nodes(root.right)
        return x+y+1
    return 0


def height_of_tree(root):
    if root:
        x = height_of_tree(root.left)
        y = height_of_tree(root.right)
        if x > y:
            return x+1
        else:
            return y+1
    else:
        return 0
    

# Driver Code
node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.left = Node(4)
node1.left.right = Node(5)
pre_order(node1)
print()
post_order(node1)
print()
in_order(node1)
print("\nTotal No. of Nodes = ", count_nodes(node1))
print("\nTotal Height of Tree = ", height_of_tree(node1))