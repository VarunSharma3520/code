'''
NOTES:

Depth First Search
    1. Preorder Traversal = rootNode -> leftNode -> rightNode
    2. Inorder Traversal = leftNode -> rootNode -> rightNode
    3. PostOrder Traversal = leftNode -> rightNode -> rootNode 
Breath First Search
    1. Level First Traversal = Level wise from left to right

Searching in BinaryTree:
We use Level order Traversal in Searching because DFS uses queue instead of stack
    '''
class TreeNode():
    def __init__(self,data = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("1")
leftChild = TreeNode("2")
tea = TreeNode("4")
coffee = TreeNode("5")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("3")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    if rootNode.data is not None:print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted" 

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        queue = []
        queue.append(rootNode)
        while len(queue) !=  0:
            rootNode = queue.pop(0)
            print(rootNode.data)
            if rootNode.leftChild is not None:
                queue.append(rootNode.leftChild)
            if rootNode.rightChild is not None:
                queue.append(rootNode.rightChild)

def find(rootNode, data):
    if not rootNode:
        return -1
    else:
        queue = []
        queue.append(rootNode)
        while len(queue) != 0:
            rootNode = queue.pop(0)
            if rootNode.data == data:
                return 1
            if rootNode.leftChild is not None:
                queue.append(rootNode.leftChild)
            if rootNode.rightChild is not None:
                queue.append(rootNode.rightChild)
        return 0


# print(deleteBT(newBT))
# print(preOrderTraversal(newBT))
print(levelOrderTraversal(newBT))
print(find(newBT,1))
