
# BINARY TREE TRAVERSAL AND CALCULATE NO. OF NODES AND HEIGHT OR DEPTH
# from msilib.schema import Binary
#                                   #      BINARY TREE
                                    #             6
                                    #           /    \
                                    #         8        9 
                                    #      /     \   /    \
                                    # NUll      10  13      15
                                    #                      /  \
                                    #                     /    \
                                    #                   NULL    17
class Binary_Tree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Preorder_Traversal(self, root):
        if root:
            print(root.data, end = " ")
            self.Preorder_Traversal(root.left)
            self.Preorder_Traversal(root.right)
    

    def Inorder_Traversal(self, root):
        if root:
            self.Inorder_Traversal(root.left)
            print(root.data, end = " ")
            self.Inorder_Traversal(root.right)
    

    def Post_Order(self, root):
        if root:
            self.Post_Order(root.left)
            self.Post_Order(root.right)
            print(root.data, end = " ")
    

    def Level_Order(self, root):
        q = []
        q.append(root)
        while q:
            temp = q.pop(0)
            print(temp.data, end = " ")
        
            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)


    # def Tree_Input(self):
    #     rootdata = int(input())
    #     if rootdata == -1:
    #         return None

    #     root = Binary_Tree(rootdata)
    #     left_child = self.Tree_Input()
    #     right_child = self.Tree_Input()
    #     root.left = left_child
    #     root.right = right_child
    #     return root

    def No_of_Nodes(self, root):
        if root:
            leftCount = self.No_of_Nodes(root.left)
            rightCount = self.No_of_Nodes(root.right)
            return leftCount + rightCount + 1
        else:
            return 0


    def right_view_of_tree(self,root, level=0):
        stack = []
        self.right_view(root, level, stack)
        return stack


    def right_view(self, root, level, stack):
        if root == None:
            return
        if level == len(stack):
            stack.append(root.data)
        self.right_view(root.right, level+1, stack)
        self.right_view(root.left, level+1, stack)


    def left_view(self, root, level, stack):
        if root == None:
            return
        if level == len(stack):
            stack.append(root.data)
        self.left_view(root.left, level+1, stack)
        self.left_view(root.right, level+1, stack)
        return stack

    def vertical_traversal(self, root):
        pass

if __name__ == "__main__":
    root = Binary_Tree(6)
    node1 = Binary_Tree(8)
    node2 = Binary_Tree(9)
    root.left = node1
    root.right = node2
    node3 = Binary_Tree(10)
    node1.right = node3
    node4 = Binary_Tree(13)
    node5 = Binary_Tree(15)
    node5.right = Binary_Tree(17)
    node2.left = node4
    node2.right = node5
    # root.Inorder_Traversal(root)
    # print("Total No. of Nodes = ", root.No_of_Nodes(root))
    # print(root.right_view_of_tree(root, 0))
    # root.left_view(root, 0, stack)
    # root.Level_Order(root)
    root.vertical_traversal(root)