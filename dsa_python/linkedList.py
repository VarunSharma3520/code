class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def addBegin(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1 
        
    def addLast(self,value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1
        
    def showLL(self):
        cursor = self.head
        while cursor is not None:
            print(cursor.value)
            cursor = cursor.next
        
    
new_linked_list = LinkedList(10)
print(new_linked_list)
print(new_linked_list.head)
print(new_linked_list.tail)
print(new_linked_list.head.value)
print(new_linked_list.length)