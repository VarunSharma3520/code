class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        
    def showTime(self):
        cursor = self.head
        string = ""
        while cursor is not None:
            string += str(cursor.data) + " -> "
            cursor = cursor.next
        print("head ->", string, "None")

def mergell(l1,l2):
    if l1.head == None and l2.head == None:
        return None
    elif l1.head == None and l2.head != None:
        return l2
    elif l1.head != None and l2.head == None:
        return l2
    
    
linky = LinkedList()
linky.append(2)
linky.append(9)
linky.append(11)
ll = LinkedList()
ll.append(3)
ll.append(6)
ll.append(7)
mergell(linky,ll)

