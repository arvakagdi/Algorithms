'''Simple tree with In Order Traversal Printing and insertion'''

class Node(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insertNode(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root  = Node (12)
root.insertNode(8)
root.insertNode(7)
root.insertNode(9)
root.insertNode(20)

root.PrintTree()

