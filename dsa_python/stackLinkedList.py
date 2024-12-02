# it is more efficient using linked list as comparedto list
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack():
    def __init__(self):
        self.head = None
        self.length = 0
    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
    def isEmpty(self):
        if self.length == 0:
            return True
        return False
    def peek(self):
        return self.head.data
    def showTime(self):
        cursor = self.head
        while cursor is not None:
            print(cursor.data)
            cursor = cursor.next
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.showTime()