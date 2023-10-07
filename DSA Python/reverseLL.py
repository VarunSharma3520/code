class Node():
    def __inti__(self,value):
        self.value = value
        self.next = None
        self.pre = None
        
class Linked List():

    def __inti__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    

linky = LinkedList
linky.append(2)
linky.append(3)
linky.append(4)
linky.append(5)
linky.append(6)
linky.append(7)
linky.showTime()