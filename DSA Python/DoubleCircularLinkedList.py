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
        pass
    
    def insert(self,data,index):
        pass

    def append(self,data):
        pass

    def find(self,data):
        
        pass

    def get(self,index):

        pass

    def setat(self,index):
        pass

    def showTime(self):
        pass
    
    def popFirst(self):
        pass

    def pop(self,index):
        pass

    def remove(self,data):
        pass

    def drop(self):
        pass

ll = LinkedList()
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(6)
ll.insert(5)
ll.prepend(1)
ll.showTime()
ll.find(2)
ll.get(2)
ll.setat("Varun Sharma",2)
ll.popFirst()
ll.pop(1)
ll.remove(5)
ll.drop()