class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.pre = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def prepend(self,data):
        node= Node(data)
        if self.head == None:
            node.pre = node
            node.next = node
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.next = self.head
            self.head.pre = node
            node.pre = self.tail
            self.head = self.head.next
            self.length += 1
    
    def insert(self,data,index):
        node= Node(data)
        if self.head == None:
            node.pre = node
            node.next = node
            self.head = node
            self.tail = node
            self.length = 1
        else:
            pass

    def append(self,data):
        node= Node(data)
        if self.head == None:
            node.pre = node
            node.next = node
            self.head = node
            self.tail = node
            self.length = 1
        else:
            pass

    def find(self,data):
        pass

    def get(self,index):
        pass

    def setat(self,index):
        pass

    def showTime(self):
        cursor = self.head
        for i in range(self.length):
            print(cursor.data)
    
    def popFirst(self):
        pass

    def pop(self,index):
        pass

    def remove(self,data):
        pass

    def drop(self):
        pass

ll = LinkedList()
ll.prepend(2)
# ll.prepend(2)
# ll.prepend(3)
ll.showTime()
