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
        else:
            pass
        self.length += 1

    def preOrderTraversal(self):
        if self.root is None:
            return 'No Element Found'
        else:
            print(root.data)
            self.preOrderTraversal(root.pre)
            self.preOrderTraversal(root.next)

    def inOrderTraversal(self):
        if self.root is None:
            return 'No Element Found'
        else:
            self.inOrderTraversal(root.pre)
            print(root.data)
            self.inOrderTraversal(root.next)

    def postOrderTraversal(self):
        if self.root is None:
            return 'No Element Found'
        else:
            self.postOrderTraversal(root.pre)
            self.postOrderTraversal(root.next)
            print(root.data)

    def levelOrderTraversal(self):
        if self.root is None:
            return 'No Element Found'
        else:
            queue = []
            queue.append(self.root)
            while len(queue) != 0:
                self.root = queue.pop(0)
                print(self.root.data)
                if self.root.pre is not None:queue.append(self.root.pre)
                if self.root.next is not None:queue.append(self.root.next)

    def remove(self):
        pass

    def deleteBT(self):
        pass

bst = BinaryTree()
bst.insert(1)
bst.preOrderTraversal(bst.root)
bst.inOrderTraversal(bst.root)
bst.postOrderTraversal(bst.root)

