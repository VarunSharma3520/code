class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def reverseLL(self):
        if self.head == None:
            return -1
        else:
            cursor = self.head
            prev = None
            while cursor is not None:
                next_node = cursor.next
                cursor.next = prev
                prev = cursor
                cursor = next_node
            self.head = prev
    
    def showTime(self):
        cursor = self.head
        string = ""
        while cursor is not None:
            string += str(cursor.value) + " -> "
            cursor = cursor.next
        print("head ->", string, "None")

linky = LinkedList()
linky.append(2)
linky.append(3)
linky.append(4)
linky.append(5)
linky.append(6)
linky.append(7)
linky.showTime()
linky.reverseLL()
linky.showTime()
