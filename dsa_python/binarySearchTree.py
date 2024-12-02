class Node():
    def __init__(self, data = None):
        self.pre = None
        self.data = data
        self.next = None

class BinaryTree():
    def __init__(self):
        self.length = 0
        self.root = None

    def insert(self, data, root = None):
        if root is None:
            self.root = Node(data)
            return self.root #! It shall be removed
        cursor = root
        while cursor is not None:
            if cursor.data < data:
                if cursor.next is None:
                    cursor.next = Node(data)
                    return
                cursor = cursor.next
            if cursor.data > data:
                if cursor.pre is None:
                    cursor.pre = Node(data)
                    return
                cursor = cursor.pre
        self.length += 1

    def preOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        else:
            print(rootNode.data)
            self.preOrderTraversal(rootNode.pre)
            self.preOrderTraversal(rootNode.next)

    def inOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        else:
            self.preOrderTraversal(rootNode.pre)
            print(rootNode.data)
            self.preOrderTraversal(rootNode.next)

    def postOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        else:
            self.preOrderTraversal(rootNode.pre)
            self.preOrderTraversal(rootNode.next)
            print(rootNode.data)


    def levelOrderTraversal(self):
        if self.root is None:
            print('No Element Found')
        else:
            queue = []
            queue.append(self.root)
            while len(queue) != 0:
                self.root = queue.pop(0)
                print(self.root.data)
                if self.root.pre is not None:queue.append(self.root.pre)
                if self.root.next is not None:queue.append(self.root.next)

    def remove(self, data):
        pass

    def deleteBT(self):
        self.root.data = None
        self.root.pre = None
        self.root.next = None


bst = BinaryTree()
bst.insert(5)
bst.insert(3,bst.root)
bst.insert(6, bst.root)
bst.insert(2,bst.root)
bst.insert(4,bst.root)
bst.insert(7, bst.root)
# bst.preOrderTraversal(bst.root)
# bst.inOrderTraversal(bst.root)
# bst.postOrderTraversal(bst.root)
bst.levelOrderTraversal()

