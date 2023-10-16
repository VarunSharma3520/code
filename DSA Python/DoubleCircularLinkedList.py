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
            node.pre = self.tail
            self.head.pre = node
            self.tail.next = node
            self.head = self.head.pre
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
            cursor = cursor.next
    
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
ll.prepend(99)
ll.prepend(3)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(6)
# ll.insert(5)
ll.prepend(1)
ll.showTime()
# ll.find(2)
# ll.get(2)-
# ll.setat("Varun Sharma",2)
# ll.popFirst()
# ll.pop(1)
# ll.remove(5)
ll.drop()
